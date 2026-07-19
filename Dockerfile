FROM python:3.12-slim

WORKDIR /app

COPY requirements-pip.txt .
RUN pip install --no-cache-dir -r requirements-pip.txt

COPY server.py .
COPY requirements.txt .

EXPOSE 8000

CMD ["python", "server.py"]
