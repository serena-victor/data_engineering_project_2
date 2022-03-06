pipeline {
	agent any

	stage('Build and start services'){
		bat 'docker-compose down'
		bat 'docker-compose up -d'
	}
	
	stage('Testing'){
		bat 'docker exec flask-app python app_test.py --verbose'
	}

	stage('Deploy'){
		input "Deploy?"
		node{
			echo "Deploying..."
			echo "Sucess"
		}
	}
}
