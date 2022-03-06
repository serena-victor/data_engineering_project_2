node {
	stage('Build Docker') {
        	bat 'docker-compose build'
	}
	stage('Deploy Docker'){
        	bat 'docker-compose down'
		bat 'docker-compose up'
	}
	stage('Cleanup Docker'){
		bat 'docker-compose stop'
	}
}
