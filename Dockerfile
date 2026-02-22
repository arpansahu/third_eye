FROM python:3.10.7

WORKDIR /app

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose necessary ports
EXPOSE 8008

# Start the application
# Note: For Kubernetes deployments, migrations are handled by Jenkins (see Jenkinsfile-deploy)
#       For Docker Compose deployments, migrations run here on container startup
CMD python manage.py migrate --noinput && \
    echo "Running collectstatic..." && \
    python manage.py collectstatic --noinput --verbosity 2 && \
    echo "✅ Collectstatic completed successfully" && \
    gunicorn --bind 0.0.0.0:8008 third_eye.wsgi