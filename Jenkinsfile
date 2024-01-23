pipeline {
  agent {docker {
            image 'python:alpine3.19'
            args '-v jenkins_home:/var/jenkins_home'
        }
        }
  stages {
    stage('checkout code- github') {
      steps {
        git(url: 'https://github.com/giladouzan1/AdvancedProject.git', branch: 'main')
      }
    }

    stage('run rest_app') {
      steps {
        sh 'pip3 install -r requirements.txt'
        sh 'nohup python3 rest_app.py &'
      }
    }

    stage('run web_app') {
      steps {
        sh 'nohup python3 web_app.py &'
      }
    }

    stage('run backend_testing') {
      steps {
        sh 'pwd'
        sh 'python3 backend_testing.py'
      }
    }

    stage('run frontend_testing') {
      steps {
        sh 'python3 frontend_testing.py'
      }
    }

    stage('run combined_testing') {
      steps {
        sh 'python3 combined_testing.py'
      }
    }

    stage('run clean_environment') {
      steps {
        sh 'python3 clean_environment.py'
      }
    }

  }
}
