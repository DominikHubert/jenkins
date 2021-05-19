pipeline {
    agent any

    stages {
        stage('linting') {
            steps {
                // Get some code from a GitHub repository
                 // git 'https://github.com/DominikHubert/jenkins.git'
                 sh 'ls'
                 //sh 'pylint pylint --disable=R,C0305 test.py'
                sh 'flake8 --format=pylint --exit-zero'
           
            }
        }
        stage('build') {
            steps {
                echo "Build"
            }
        }
        

            post {
                always{
                // If Maven was able to run the tests, even if some of the test
                // failed, record the test results and archive the jar file.
                recordIssues(tools: [flake8()])
                }
            }
        }
}
