"""番茄钟 · 专注计时 —— Flask 版

静态页面由 Flask 提供渲染，/api/time 为后端实时计算的接口，
用来演示"页面内容由 Python 服务端动态生成"的动态网站形态。
"""
import os
import datetime

from flask import Flask, jsonify, render_template

app = Flask(__name__)

WEEKDAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


@app.route("/")
def index():
    """渲染番茄钟主页面"""
    return render_template("index.html")


@app.route("/api/time")
def server_time():
    """后端接口：实时返回服务器时间（每次请求由 Python 现场计算）"""
    now = datetime.datetime.now()
    return jsonify(
        iso=now.isoformat(timespec="seconds"),
        weekday=WEEKDAYS[now.weekday()],
        version="v2",
    )


@app.route("/healthz")
def healthz():
    """健康检查，部署平台探活用"""
    return "ok", 200


if __name__ == "__main__":
    # 本地开发用；端口尊重环境变量 PORT（部署平台会注入）
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
