FROM python:3.11.11

WORKDIR /app

# Install pre-built wheels for numpy and other dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --prefer-binary numpy && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# Configure Gunicorn
ENV PORT=8080
EXPOSE 8080

# Use Gunicorn with proper production settings
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8080", "app:app", "--access-logfile", "-", "--error-logfile", "-", "--log-level", "info"]
