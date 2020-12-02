# ProgramLibraryAPI
PreRequisites:
1. Install Python 3.x.x ( I have installed Python 3.9.0).
2. Install pip (I have installed pip 20.2.3 ).
3. Execute sudo pip3 install flask (Flask 1.1.2).
4. Execute sudo pip3 install flask_restful.
5. Download and install "MySQL Connector".

To setup database
1. Install MySQL (I have used MySQL 5.7 from GCP Console).
2. Create MySQL instance.
3. To create database and tables, execute the database scripts located at (../database_scripts/create_tbl.sql).
4. To insert data in the tables, execute the insert database script located at (../database_scripts/insert_tbl.sql).

To host the server
1. Update the configuration details in config.py file in ProgramLibraryAPI/src. Configuration details involves mysql database host name, port number(if any), userid and password).
2. Navigate to the project folder(ProgramLibraryAPI) through command line (cd /ProgramLibraryAPI/src).
3. Run Python server code using command python3 program_library_resources.py.

To execute the API from client.
1. Update the configuration details in config.py file in ProgramLibraryAPI/ProgramLibraryAPIClient. Configuration details involves python server base url.
2. Navigate to the project folder(ProgramLibraryAPIClient) through a new command line (cd /ProgramLibraryAPIClient).
3. Execute the test python code using ProgramLibrary_client.py.

To execute unit test
1. Navigate to the project folder ProgramLibraryAPI/.
2. Make sure the server is up and running.
3. Execute python3 -m src.test.test_url_validator. (validates the api urls).
4. Execute python3 -m src.test.query_helper_test. (validates the database queries used).
5. Execute python3 -m src.test.result_formatter_test. (validates the json output that is returned by the api).


Future enhancements:
1. Exception handling 
2. POST methods for each entities.
3. Automated test cases for creating database entries and testing api.
4. Pagination for retrives.
5. Automate server hosting for unit tests.
