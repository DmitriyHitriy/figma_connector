FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements-pip.txt .
RUN pip install --no-cache-dir -r requirements-pip.txt

COPY server.py .
COPY requirements.txt .

EXPOSE 8000

CMD ["python", "server.py"]
