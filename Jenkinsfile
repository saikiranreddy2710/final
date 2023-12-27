pipeline {
    agent any

     environment {
        REMOTE_HOST = '98.70.25.254'
        REMOTE_USER = 'sai'
        PRIVATE_KEY_PATH = '/var/jenkins/ssh-keys/my-ssh-key'
        SSH_CREDENTIALS_ID = 'key'
        PROJECT_PATH = '/path/to/your/project'
        DOCKER_IMAGE_NAME = 'final'
        DOCKER_IMAGE_TAG = 'latest'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Connecting to Remote Server'){
            steps {
                script{
                    sshagent(['${env.SSH_CREDENTIALS_ID}']) {
                        sh "ssh -i /path/to/private/key user@host 'echo connected'"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "cd RecommendationEngine_Movies_Docker-Kubernetes"
                    sh "docker build -t (env.DOCKER_IMAGE_NAME) ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.example.com', 'docker-id') {
                        docker.image(env.DOCKER_IMAGE).push()
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
                        docker.run("-p 8081:5000 --name ${env.CONTAINER_NAME} -d ${env.DOCKER_IMAGE}")
                    } else {
                        echo "Stopping and removing the existing container..."
                        sh "docker stop ${env.CONTAINER_NAME}"
                        sh "docker rm ${env.CONTAINER_NAME}"

                        echo "Starting a new container with the latest image..."
                        docker.run("-p 8081:5000 --name ${env.CONTAINER_NAME} -d ${env.DOCKER_IMAGE}")
                    }
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
