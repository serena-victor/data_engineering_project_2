pipeline {
	agent any  
    
    tools {nodejs "node"}

	stages {
		stage('Build Docker') {
			steps {
				bat 'docker-compose down'
				bat 'docker-compose up -d'
                echo 'success -> deployement'
			}
		}
	}
}
