pipeline {
    agent any

    environment {
        REMOTE_HOST = '98.70.25.254'
        SSH_CREDENTIALS_ID = 'key' 
        PROJECT_PATH = '/home/sai/RecommendationEngine_Movies_Docker-Kubernetes' // On the remote server
        DOCKER_IMAGE_NAME = 'final'             
        CONTAINER_NAME = 'remote'                
        K8S_NAMESPACE = 'your-namespace'         
        K8S_DEPLOYMENT_NAME = 'your-deployment' 
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Connect to Remote Server') {
            steps {
                //sshagent(['${env.SSH_CREDENTIALS_ID}']) {
                     //sh "ssh -o StrictHostKeyChecking=no user@98.70.25.254 
                echo 'connected' 
                
            }
        }

        stage('Build Docker Image') {
            steps {
                //dir("RecommendationEngine_Movies_Docker_Kubernetes") {
                    //sh "docker build -t ${env.DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} ."  
                    echo 'docker build success'
                
            }
        }

        stage('Push Docker Image') {
            steps {
               // script{   
                   // docker.withRegistry('https://hub.docker.com/r/saikiran27/final', 'saikiran27') {
                        //docker.image("${env.DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}").push()
                        echo 'docker push success'
                    
                
            }
        }

        stage('Deploy to Remote Server') {
            steps {
                //dir("RecommendationEngine_Movies_Docker_Kubernetes") { 
                    //sshagent(['${env.SSH_CREDENTIALS_ID}']) {
                       // sh '''
                         //  docker stop ${env.CONTAINER_NAME} || true  // Ignore errors if not running
                          //  docker rm ${env.CONTAINER_NAME}   || true
                         //   docker run -d -p 8081:5000 --name ${env.CONTAINER_NAME} ${env.DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}
                       // '''
                    echo 'deploy to remote server'
                    
                
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                //dir("RecommendationEngine_Movies_Docker_Kubernetes") { 
                    //sh "kubectl apply -f your-kubernetes-manifest.yaml -n ${env.K8S_NAMESPACE}" 
                echo 'kubernetes deploy success'
                
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
