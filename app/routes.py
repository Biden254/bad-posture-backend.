from flask import Blueprint, request, jsonify
from app.logic.pose_estimation import extract_pose, extract_pose_from_frame
from app.logic.rules import evaluate_posture
import cv2
import tempfile
import os

main = Blueprint('main', __name__)

@main.route('/frame', methods=['POST'])
def analyze_frame():
    if 'frame' not in request.files:
        return jsonify({'error': 'No frame provided'}), 400

    file = request.files['frame']
    feedback = {}

    landmarks = extract_pose(file)
    if landmarks:
        feedback = evaluate_posture(landmarks)

    return jsonify(feedback)


@main.route('/upload', methods=['POST'])
def analyze_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video provided'}), 400

    video = request.files['video']
    
    # Save video temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp:
        video.save(temp.name)
        temp_path = temp.name

    feedback_list = []
    issue_counts = {}
    total_frames = 0
    bad_frames = 0

    cap = cv2.VideoCapture(temp_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        total_frames += 1

        # Resize and convert to RGB
        frame = cv2.resize(frame, (640, 480))
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        landmarks = extract_pose_from_frame(rgb)
        if landmarks:
            feedback = evaluate_posture(landmarks)
            feedback['frame'] = total_frames - 1
            feedback_list.append(feedback)

            # Count issue types
            issue = feedback.get('issue', 'Unknown')
            if issue != 'Good posture':
                bad_frames += 1
                issue_counts[issue] = issue_counts.get(issue, 0) + 1

    cap.release()
    os.remove(temp_path)

    summary = {
        'total_frames': total_frames,
        'bad_posture_frames': bad_frames,
        'issues_breakdown': issue_counts,
        'feedback': feedback_list  # optional: you can exclude this if too long
    }

    return jsonify(summary)

