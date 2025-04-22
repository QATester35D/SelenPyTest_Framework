pipeline {
    agent any

    environment {
        // Ensures Python can find the QATests package
        PYTHONPATH = 'QATests'
    }

    stages {
        stage('Clone Repo') {
            steps {
                // If you're pulling from GitHub, this is done automatically
                echo 'Repository cloned by Jenkins'
            }
        }

        stage('Set up Python environment') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r QATests/requirements.txt
                '''
            }
        }

        stage('Run Tests with Pytest') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest QATests/tests \
                        --html=QATests/reports/test_report.html \
                        --self-contained-html \
                        --tb=short -v
                '''
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'QATests/reports/test_report.html', onlyIfSuccessful: true
            }
        }
    }

    post {
        always {
            junit '**/TEST-*.xml' allowEmptyResults: true
        }

        failure {
            echo 'Tests failed! Check the HTML report for details.'
        }
    }
}

