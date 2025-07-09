import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Use Render's provided PORT if available, fallback to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

# This is the main entry point of the backend application.
# It creates an instance of the Flask application and runs it on port 8000 in debug mode.
# The `create_app` function initializes the application with the necessary configurations and routes.