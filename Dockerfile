FROM python:3.11.11

WORKDIR /app

# Install pre-built wheels for numpy and other dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --prefer-binary numpy && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "app.py"]
