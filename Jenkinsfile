@Library("shared") _
pipeline {
    agent any
    
    stages {
        stage('Hello'){
            steps{
                script{
                    hello()
                }
            }
        }
        stage('Clone Repository') {
            steps {
                script {
                   git credentialsId: '5edb027f-4905-41b0-9c4e-ba09a19549e7', url: "https://github.com/srujanaa6/docker-test.git", branch: "main"
            }
        }
        }
        stage('Test Docker Access') {
            steps {
                script {
                    sh 'docker ps'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t flask-test-app:latest .'
                    echo "docker built.."
                }
            }
        }
        stage('push to dockerhub'){
            steps{
                script{
                    echo "pushing to docker hub ..."
                withCredentials([usernamePassword('credentialsId':"docker-hub-cred",
                passwordVariable:"dockerhubpass",
                usernameVariable:"dockerhubuser")]){
                sh "docker login -u ${env.dockerhubuser} -p ${env.dockerhubpass}"
                sh "docker image tag flask-test-app:latest ${env.dockerhubuser}/flask-test-app:latest"
                sh "docker push ${env.dockerhubuser}/flask-test-app:latest" 
                echo "successfully pushed to docker hub ..."
                } 
                }
               
            }
        }

    }
    }
