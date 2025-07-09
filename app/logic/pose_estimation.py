import os
import mediapipe as mp
import cv2
import numpy as np

# Disable GPU for compatibility with non-GPU environments like Render
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

mp_pose = mp.solutions.pose

def extract_pose(image_file):
    """Extract pose landmarks from an uploaded image file (e.g., webcam snapshot)."""
    image_bytes = np.frombuffer(image_file.read(), np.uint8)
    image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

    with mp_pose.Pose(
        static_image_mode=True,
        model_complexity=1,
        enable_segmentation=False,
        min_detection_confidence=0.5
    ) as pose:
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if not results.pose_landmarks:
            return None
        return results.pose_landmarks.landmark


def extract_pose_from_frame(frame):
    """Extract pose landmarks from an OpenCV frame (e.g., video frame)."""
    with mp_pose.Pose(
        static_image_mode=True,
        model_complexity=1,
        enable_segmentation=False,
        min_detection_confidence=0.5
    ) as pose:
        results = pose.process(frame)
        if not results.pose_landmarks:
            return None
        return results.pose_landmarks.landmark
