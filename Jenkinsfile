pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'your-docker-image:latest'
        CONTAINER_NAME = 'your-container-name'
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
