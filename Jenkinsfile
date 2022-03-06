node {
	//stage('Get Source') {
      	//	git ('https://github.com/serena-victor/data_engineering_project_M2_2.git')
      	//	if (!fileExists("Dockerfile")) {
        // 		error('Dockerfile missing.')
      	//	}
   	//}
	stage('Build Docker'){
        	bat 'docker-compose build'
	}
	
	stage('Deploy Docker'){
        	bat 'docker-compose down --volumes'
		bat 'docker-compose up -d'
	}
	
	stage('Testing'){
		bat 'docker exec -it de2_m2_2_pipeline_webapp python app_test.py --verbose'
	}
}
