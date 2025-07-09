FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    git ffmpeg libsm6 libxext6 libglib2.0-0 libgl1-mesa-glx \
    && apt-get clean

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install flask flask-cors numpy opencv-python mediapipe==0.10.9

EXPOSE 5000

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000"]
