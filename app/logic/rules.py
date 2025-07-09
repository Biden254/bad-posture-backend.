import math

def calculate_angle(a, b, c):
    """ Returns the angle between three points """
    ang = math.degrees(math.atan2(c.y - b.y, c.x - b.x) -
                       math.atan2(a.y - b.y, a.x - b.x))
    return abs(ang if ang >= 0 else 360 + ang)

def evaluate_posture(landmarks):
    feedback = {}

    left_shoulder = landmarks[11]
    left_hip = landmarks[23]
    left_knee = landmarks[25]
    left_ankle = landmarks[27]
    left_eye = landmarks[1]

    back_angle = calculate_angle(left_shoulder, left_hip, left_knee)
    neck_angle = calculate_angle(left_eye, left_shoulder, left_hip)

    # Example: Sitting posture detection
    if back_angle < 150:
        feedback['issue'] = 'Slouched Back'
    elif neck_angle > 30:
        feedback['issue'] = 'Neck Bent Forward'
    else:
        feedback['issue'] = 'Good posture'

    feedback['frame'] = request_frame_number()
    return feedback

def request_frame_number():
    # For now just return dummy frame number (increment later if needed)
    from time import time
    return int(time())  # Can be customized to track frame numbers properly
