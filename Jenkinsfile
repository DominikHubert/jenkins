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
             

            post {
                always{
                // If Maven was able to run the tests, even if some of the test
                // failed, record the test results and archive the jar file.
                recordIssues(tools: [flake8()], qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]], healthy: 10, unhealthy: 100, minimumSeverity: 'HIGH')
                }
            }
        }
        stage('build') {
            steps {
                echo "Build"
                docker.build "app"
                //sh 'docker build . -t demosite'
            }
        }
        stage('deploy') {
            steps {
                echo "deploy"
            }
        }
        stage('dynamic test') {
            steps {
                echo "dynamic test"
            }
        }
       
        }
}
