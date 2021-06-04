pipeline {
    agent { docker { image 'python:3.8' } }
    stages {
        stage('build') {
            steps {
                sh '''#!/usr/bin/env bash
                    python3 -m venv env
                    source env/bin/activate
                    pip install -r requirements-test.txt
                    cd student_board
                    rm django.sqlite3
                    python3 manage.py migrate --settings=student_board.test_settings
                    coverage run --source='.' manage.py test --settings=student_board.test_settings
                    coverage report
                '''
            }
        }
    }
}
