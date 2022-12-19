FROM python:3.8


WORKDIR /app

COPY requirements.txt .


RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 80
CMD ["gunicorn", "--workers", "10", "--max-requests", "10000", "--worker-connections", "1000", "--preload", "--log-level", "debug", "server:app"]