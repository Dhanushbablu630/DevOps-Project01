pipeline {
    agent any

    environment {
        IMAGE_NAME = "dhanushdocker56/devops_project01"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Dhanushbablu630/DevOps-Project01.git'
            }
        }

        stage('Debug') {
            steps {
                sh '''
                    echo "Listing files after checkout..."
                    ls -l
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                // Since Dockerfile is at repo root, just build from "."
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $IMAGE_NAME:latest
                    '''
                }
            }
        }

        stage('Deploy on EC2') {
            steps {
                sh '''
                    docker stop devops_project01 || true
                    docker rm devops_project01 || true
                    docker run -d --name devops_project01 -p 80:3000 $IMAGE_NAME:latest
                '''
            }
        }
    }
}
