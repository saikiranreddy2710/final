pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'final:latest'
        CONTAINER_NAME = 'container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build env.DOCKER_IMAGE
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.example.com', 'docker-credentials-id') {
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
                docker.run("-p 8080:80 --name ${env.CONTAINER_NAME} -d ${env.DOCKER_IMAGE}")
            } else {
                echo "Stopping and removing the existing container..."
                sh "docker stop ${env.CONTAINER_NAME}"
                sh "docker rm ${env.CONTAINER_NAME}"

                echo "Starting a new container with the latest image..."
                docker.run("-p 8080:80 --name ${env.CONTAINER_NAME} -d ${env.DOCKER_IMAGE}")
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
