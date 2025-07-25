FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git ffmpeg libsm6 libxext6 libglib2.0-0 libgl1-mesa-glx \
    && apt-get clean

# Set working directory to /backend because that's where your code lives
WORKDIR /backend

# Copy everything into the image
COPY . .

# Ensure Python can find the app/ module
ENV PYTHONPATH="${PYTHONPATH}:/backend"

# Install Python packages
RUN pip install --upgrade pip
RUN pip install flask flask-cors numpy opencv-python mediapipe==0.10.9 gunicorn

EXPOSE 5000

# Start the app using gunicorn
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000", "--log-level", "debug"]
