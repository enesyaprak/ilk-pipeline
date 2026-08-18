pipeline {
    agent any

    environment {
        UYGULAMA = 'ilk-pipeline'
    }

    stages {
        stage('Test') {
            agent { docker { image 'python:3.12-slim' } }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest -v'
            }
        }
        stage('Lint') {
            steps {
                sh 'echo "lint asamasi"'
            }
        }

        stage('Build') {
            when {
                branch 'main'
            }
            steps {
                sh 'echo "${UYGULAMA} build ediliyor..."'
            }
        }
    }

    post {
        success {
            echo 'Pipeline yesil'
        }
        failure {
            echo 'Pipeline patladi - normalde buraya Slack/mail bildirimi konur'
        }
        always {
            echo 'Her durumda calisir - temizlik islemleri buraya'
        }
    }
}
