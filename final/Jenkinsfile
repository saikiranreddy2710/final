pipeline {
  agent any
  
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t myimage .'
      }
    }
    
    stage('Deploy') {
      steps {
        script {
          def sshCommand = "ssh sai@98.25.10.254 'docker build -t myimage . && docker run -d -p 80:80 --name mycontainer myimage'"
          sh sshCommand
        }
      }
    }
  }
}

