Project Description
This is the Flask backend for the Bad Posture Detection App. It receives video frames from the frontend (uploaded or via webcam), processes them using MediaPipe and OpenCV, applies rule-based logic, and returns posture feedback.
Live Backend API
https://posture-backend.onrender.com
Tech Stack
| Component    | Tech Used     |
|--------------|---------------|
| Backend      | Flask         |
| Pose Logic   | MediaPipe     |
| Processing   | OpenCV, NumPy |
| Deployment   | Render        |
Folder Structure
/backend
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── logic/
│       ├── pose_estimation.py
│       └── rules.py
├── main.py
├── requirements.txt
└── README.md
Local Setup Instructions
1. Clone the backend repo:
   git clone https://github.com/Biden254/bad-posture-backend.git
   cd bad-posture-backend

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  (Linux/macOS)
   venv\Scripts\activate     (Windows)

3. Install dependencies:
   pip install -r requirements.txt

4. Run the app:
   python main.py

> The backend will run at http://localhost:5000
Rule-Based Posture Logic
- **Squat**: Flags when knees go beyond toes or back angle < 150°
- **Desk Sitting**: Flags when neck bend > 30° or back isn’t straight
Deployment on Render
1. Push backend code to a public GitHub repository
2. Go to https://render.com and click 'New Web Service'
3. Connect your GitHub repo
4. Set:
   - Build command: pip install -r requirements.txt
   - Start command: gunicorn main:app
5. Deploy and use the generated Render URL as your API endpoint
License
MIT License – feel free to fork or build upon this project!
Credits
Built by Loren Deklerk — https://github.com/Biden254 • http://www.linkedin.com/in/loren-deklerk-81a7312a5
