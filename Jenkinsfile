
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --user -r requirements.txt'
                sh 'python3 -m pip install --user pytest'
            }
        }

        stage('Build and Test') {
            steps {
                sh 'python3 -m py_compile app.py'
                sh 'python3 -m pytest -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t aceest-fitness .'
            }
        }
    }
}
