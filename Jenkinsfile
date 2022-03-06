pipeline {
	agent any

	stages {
 		stage('Build and start services'){
 			steps {
 				bat 'docker-compose up -d'
 				bat 'powershell -command "Start-Sleep -s 5"'
 			}
 		}

		stage('Testing'){
			steps {
				bat 'docker exec flask-app python app_test.py --verbose'
			}
		}

		stage('Deploy'){
			steps {
				input "Deploy?"
			}
		}
	}

	post {
		success {
			echo "Deploying"
		}
	}


}
