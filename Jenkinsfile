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
                    python3 manage.py migrate --settings=student_board.test_settings
                    python3 manage.py test --settings=student_board.test_settings
                '''
            }
        }
    }
}
