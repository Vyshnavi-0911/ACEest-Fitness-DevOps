
# ACEest Fitness & Gym

A Flask-based fitness and gym member management application built for the Introduction to DevOps assignment.

## Features
- Welcome page
- Health check endpoint
- View gym members
- Add a gym member
- Retrieve a member by ID
- Automated tests with pytest
- Docker container support
- Jenkins pipeline
- GitHub Actions CI workflow

## Requirements
- Python 3.11 or compatible version
- pip
- Docker for container builds

## Run locally
Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

Open http://127.0.0.1:5000

## Run tests

```bash
python -m pytest -v
```

## API endpoints
- GET `/` - welcome message
- GET `/health` - health status
- GET `/members` - list members
- POST `/members` - add a member using JSON such as `{"name":"Ravi"}`
- GET `/members/1` - retrieve a member by ID

## Docker

```bash
docker build -t aceest-fitness .
docker run --rm -p 5000:5000 aceest-fitness
```

## CI/CD
GitHub Actions runs syntax checks, pytest tests, Docker image build, and a health check inside the container on pushes and pull requests to main.

The Jenkinsfile provides checkout, dependency installation, test, and Docker build stages.

## Manual testing
1. Open the home page in a browser.
2. Open `/health` and confirm the status is healthy.
3. Run pytest and check the test results.
4. Build and run the Docker image if Docker is available.
5. Check the GitHub Actions workflow result.
