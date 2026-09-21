# 番茄钟 Flask 版 —— 通用容器化模板
# Python 项目照抄改端口即可；Java 项目换基础镜像（如 eclipse-temurin:21-jre）
FROM python:3.12-slim

WORKDIR /app

# 先装依赖（利用 Docker 层缓存：代码改了不用重装依赖）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 再拷贝代码
COPY . .

# 容器对外监听端口（Zeabur 会注入 PORT，默认 8080）
ENV PORT=8080
EXPOSE 8080

# gunicorn 生产级启动
CMD ["sh", "-c", "gunicorn app:app --bind 0.0.0.0:${PORT:-8080} --workers 2"]
