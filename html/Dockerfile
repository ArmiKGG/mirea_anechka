FROM python:3.8


WORKDIR /app

COPY requirements.txt .


RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 9090
CMD ["gunicorn", "--workers", "10", "-b", "localhost:9090", "--max-requests", "10000", "--worker-connections", "1000", "--preload", "--log-level", "debug", "server:app"]