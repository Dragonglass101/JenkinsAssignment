pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Dragonglass101/JenkinsAssignment.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x modulus.py"
                sh "./modulus.py"
            }
        }
        stage('Test Code Passed') {
            steps {
                sh "chmod u+x unit_test_1.py"
                sh "./unit_test_1.py"
            }
        }
        stage('Test Code extra stage') {
            steps {
                sh "chmod u+x unit_test_2.py"
                sh "./unit_test_2.py"
            }
        }
        stage('Test Code Failed') {
            steps {
                sh "chmod u+x unit_test_2.py"
                sh "./unit_test_2.py"
            }
        }
    } 
}
