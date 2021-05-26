pipeline {
    agent any

    stages {
        stage ("lint dockerfile") {
    agent {
        docker {
            image 'hadolint/hadolint:latest-debian'
            //image 'ghcr.io/hadolint/hadolint:latest-debian'
        }
    }
    steps {
        sh 'hadolint Dockerfile | tee -a hadolint_lint.xml'
    }
    post {
        always {
            recordIssues(tools: [hadoLint(pattern: 'hadolint.json')], qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]], healthy: 10, unhealthy: 100, minimumSeverity: 'HIGH')
                
            archiveArtifacts 'hadolint_lint.xml'
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
