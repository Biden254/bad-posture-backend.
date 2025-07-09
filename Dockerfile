FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    git ffmpeg libsm6 libxext6 libglib2.0-0 libgl1-mesa-glx \
    && apt-get clean

# Set working directory
WORKDIR /app
COPY . .

# Python dependencies
RUN pip install --upgrade pip
RUN pip install flask flask-cors numpy opencv-python
RUN pip install git+https://github.com/google/mediapipe.git

EXPOSE 5000

# Start the server
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000"]
