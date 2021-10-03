# students-data-apis


 <br/>
 
 ## Setup the Project
 
 1. Install Python 3.8 or above
 
 2. Create a virtualenv and activate it
 
    ```
    pip install virtualenv
    virtualenv venv
    venv\Scripts\activate        # For Windows
    source venv/bin/activate     # For Linux
    ```
 
 3. Install dependencies
    ```
    pip install -r requirements.txt
    ```
    
 4. Make .env file (reference: example.env) 
    ``` 
    Provide all environments variable values in .env file
    ```
    
 5. Project structure

    1. **Root**

        **./**

        ├── `api` APIs of project

        ├── `service` for helper functions
       
        ├── `questions.py` Question answers file
       
        ├── `main.py` file to run project

        ├── `.gitignore` list files and folders to be ignored in git

        ├── `config.py` file to handle configuration parameters

        ├── `README.md` Instruction file

        ├── `example.env` example of environment file

        ├── `.pylintrc` pylint configuration file
        
        ├── `requirements.txt` python package file

    2. **APIs**

        **api/v1/**

        ├── `classes` APIs related to classes endpoint
        
        ├── `student` APIs related to student endpoint
        
        ├── `student_class.py` APIs related to student + class endpoint
        
        ├── `__init__.py` package file
    
    3. **services**

        **services/**

        ├── `common_helper.py` common helper functions
        
        ├── `database.py` file to perform operation related database
        
        ├── `logger.py` to save logs of process

        ├── `__init__.py` package file
    
 
 <br/>
 
 ## Run the Project

    
 * Go to project directory in terminal and run the command
    
    ```
    python main.py
    ```
