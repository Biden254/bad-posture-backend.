# Use official Python image
FROM python:3.10-slim

# Install system dependencies needed by OpenCV & MediaPipe
RUN apt-get update && apt-get install -y \
    ffmpeg libsm6 libxext6 libglib2.0-0 libgl1-mesa-glx \
    && apt-get clean

# Set the working directory
WORKDIR /app

# Copy all project files
COPY . .

# Upgrade pip and install Python packages
RUN pip install --upgrade pip
RUN pip install flask flask-cors numpy opencv-python
RUN pip install git+https://github.com/google/mediapipe.git

# Expose port Flask will run on
EXPOSE 5000

# Start the app using Gunicorn
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000"]
