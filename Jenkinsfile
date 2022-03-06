node {
	//stage('Get Source') {
      	//	git ('https://github.com/serena-victor/data_engineering_project_M2_2.git')
      	//	if (!fileExists("Dockerfile")) {
        // 		error('Dockerfile missing.')
      	//	}
   	//}
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
