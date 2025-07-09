from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=8000)
# This is the main entry point of the backend application.
# It creates an instance of the Flask application and runs it on port 8000 in debug mode.
# The `create_app` function initializes the application with the necessary configurations and routes.