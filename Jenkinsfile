pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install playwright behave
                playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Behave Tests...'
                sh '''
                source venv/bin/activate
                behave features/login.feature
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline Execution Finished'
            archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
        }
        success {
            echo 'Tests Passed Successfully!'
        }
        failure {
            echo 'Tests Failed. Check logs for details.'
        }
    }
}
