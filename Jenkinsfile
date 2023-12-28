pipeline {
    agent any

    environment {
        REMOTE_HOST = '98.70.25.254'
        SSH_CREDENTIALS_ID = 'key'
        PROJECT_PATH = '/path/to/your/project'
        DOCKER_IMAGE_NAME = 'final'
        DOCKER_IMAGE_TAG = 'latest'
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

        stage('Connecting to Remote Server') {
            steps {
                script {
                    sshagent(['${env.SSH_CREDENTIALS_ID}']) {
                        
                        sh "ssh user@${env.REMOTE_HOST} 'echo "connected"'"
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                     dir("RecommendationEngine_Movies_Docker_Kubernetes") {
                       sh "docker build -t ${env.DOCKER_IMAGE_NAME} ."
                 
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://your-docker-registry-url', 'docker-id') {
                        docker.image(env.DOCKER_IMAGE_NAME).push()
                    }
                }
            }
        }

        stage('Deploy Docker Container') {
            steps {
                script {
                    def containerStatus = sh(script: "docker ps -q --filter name=${env.CONTAINER_NAME}", returnStatus: true).trim()

                    if (containerStatus.isEmpty()) {
                        echo "Container is not running. Starting a new container..."
                        docker.run("-p 8081:5000 --name ${env.CONTAINER_NAME} -d ${env.DOCKER_IMAGE_NAME}")
                    } else {
                        echo "Stopping and removing the existing container..."
                        sh "docker stop ${env.CONTAINER_NAME}"
                        sh "docker rm ${env.CONTAINER_NAME}"

                        echo "Starting a new container with the latest image..."
                        docker.run("-p 8081:5000 --name ${env.CONTAINER_NAME} -d ${env.DOCKER_IMAGE_NAME}")
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh "kubectl apply -f your-kubernetes-manifest.yaml -n ${env.K8S_NAMESPACE}"
                }
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
