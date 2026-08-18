pipeline {
    agent any

    environment {
        UYGULAMA = 'ilk-pipeline'
    }

    stages {
        stage('Test') {
            steps {
                sh 'python3 --version'
                sh 'echo "test asamasi calisti - build no: ${BUILD_NUMBER}"'
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
