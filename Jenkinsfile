pipeline {
    agent any

    stages {
        stage ("lint dockerfile") {
            agent {
                docker {
                    image 'hadolint/hadolint:latest-debian'
                }
            }
            steps {
                sh 'hadolint Dockerfile | tee -a hadolint.xml'
            }
            post {
                always {
                    archiveArtifacts 'hadolint.xml'
                }
            }
        }
        stage ("lint dockerfile") {
            agent {
                docker {
                    image 'hadolint/hadolint:latest-debian'
                }
            }
            steps {
                sh 'hadolint Dockerfile | tee -a hadolint.xml'
            }
            post {
                always {
                    archiveArtifacts 'hadolint.xml'
                }
            }
        }
        stage('linting') {
            steps {
                // Get some code from a GitHub repository
                 // git 'https://github.com/DominikHubert/jenkins.git'
                 sh 'ls'
                 //sh 'pylint pylint --disable=R,C0305 test.py'
                sh 'csslint mystyle.css'
                
            }
             

            post {
                always{
                // If Maven was able to run the tests, even if some of the test
                // failed, record the test results and archive the jar file.
                recordIssues(tools: [cssLint()], qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]], healthy: 10, unhealthy: 100, minimumSeverity: 'HIGH')
                }
            }
        }
        stage('build') {
            steps {
                script {
                echo "Build"
                app = docker.build "dkowatsch/app"
                //sh 'docker build . -t demosite'
                
                }
                
            }
        }
        stage('deploy and test') {
           
                    steps {
                        script {
                        echo "deploy"
                    
                        docker.image('dkowatsch/app').withRun('-p 8081:80') {
                            sh 'curl localhost:8081'
                            }
                        }      
                    }
                
            
        }
        stage('dynamic test') {
            steps {
                script { 
                docker.withRegistry('https://registry.hub.docker.com', 'docker') {  
                app.push("latest")     
                }   
              }    
            }
        }
       
    }
}
