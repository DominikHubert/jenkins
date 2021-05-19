pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                 // git 'https://github.com/DominikHubert/jenkins.git'
                 sh 'ls'
                 //sh 'pylint pylint --disable=R,C0305 test.py'
                sh 'flake8 --format=pylint --exit-zero'
            withMaven {
                // sh "mvn clean install checkstyle:checkstyle"
                // some block
                }
                // Run Maven on a Unix agent.
               

                // To run Maven on a Windows agent, use
                // bat "mvn -Dmaven.test.failure.ignore=true clean package"
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
}
