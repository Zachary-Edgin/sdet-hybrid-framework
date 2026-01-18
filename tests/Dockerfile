FROM mcr.microsoft.com/playwright/python:v1.49.0-jammy

WORKDIR /work
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["pytest", "-q"]