# Base Image
FROM python:3.12-slim

# Django settings
ENV DEBUG=True
ENV SECRET_KEY=38CDE7EDB4F436B5CF3F2455BBFF8
ENV ALLOWED_HOSTS=localhost,127.0.0.1,filepocket.onrender.com

# Database settings (hostdagi PostgreSQL)
ENV DATABASE_NAME=filepocket
ENV DATABASE_USER=filepocket
ENV DATABASE_PASSWORD=pass6666
ENV DATABASE_HOST=host.docker.internal
ENV DATABASE_PORT=6666

# Work directory
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic --noinput

# Copy project
COPY . .

# Expose port
EXPOSE 8000

# Start Django
CMD ["gunicorn", "FilePocket.wsgi:application", "--bind", "0.0.0.0:8000"]

