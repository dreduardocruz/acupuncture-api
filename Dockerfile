FROM python:3.11.11

WORKDIR /app

# Install system dependencies first
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    gcc \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Install base pip packages first
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install wheel setuptools

# Install requirements in separate steps for better error tracking
RUN pip install --no-cache-dir numpy pandas
RUN pip install --no-cache-dir flask gunicorn
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8080
EXPOSE 8080

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8080", "app:app", "--access-logfile", "-", "--error-logfile", "-", "--log-level", "info"]
