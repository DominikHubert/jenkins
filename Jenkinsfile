pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                 git 'https://github.com/DominikHubert/jenkins.git'
                 sh 'python -m pylint --rcfile=.pylintrc --exit-zero ${MODULE} > ${WORKSPACE}/testreport/pylint.log'
            withMaven {
                // sh "mvn clean install checkstyle:checkstyle"
                // some block
                }
                // Run Maven on a Unix agent.
               

                // To run Maven on a Windows agent, use
                // bat "mvn -Dmaven.test.failure.ignore=true clean package"
            }

            post {
                // If Maven was able to run the tests, even if some of the test
                // failed, record the test results and archive the jar file.
                success {
                    recordIssues(tools: [checkStyle()])
                }
            }
        }
    }
}
