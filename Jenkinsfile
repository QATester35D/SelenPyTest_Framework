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

        stage('Setup and Run Tests') {
            steps {
                bat '''
                    set PYTHONPATH=%CD%\\QATests
                    python -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    python -m pip install -r QATests\\requirements.txt
                    REM pytest QATests\\tests --html=QATests\\reports\\test_report.html --junitxml=QATests\\reports\\TEST-results.xml --self-contained-html --tb=short -v
                    pytest QATests\\tests\\test_form_page.py ^
                       --html=QATests\\reports\\test_report.html ^
                       --junitxml=QATests\\reports\\TEST-results.xml ^
                       --self-contained-html ^
                       --tb=short -v ^
                       -o soft_asserts=false
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

