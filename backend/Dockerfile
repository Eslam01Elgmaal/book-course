FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install system dependencies (important for moviepy + postgres)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    ffmpeg \                     
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files first (best practice for Docker cache)
COPY requirements.txt requirements.lock.txt ./

# Install from the **locked** file only
RUN pip install --no-cache-dir -r requirements.lock.txt

# Copy the rest of the application code
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]