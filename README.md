# University-Management-System
#### This is Course project for CS-258. Project Number - P012 
  
Krishanu Saini 190001029 
Rahul Kumar 190001049 
Kuldeep Singh 190001030  
Deepkamal Singh 190001011    
<hr>

Visit {link to be added} for live demo. Frontend and Backend working.

Clone this project  
  
## Installing Requirements  
      1. Mysql (preferably use Mysql Workbench 8.0)  
      
      2. Python 3.8 / 3.7 / 3.6 ( Not compatible with python 3.9 )  
 <br ><br ><br > 
        
## STEP 1  ( IMPORTING MYSQL DATABASE)
      1. Run DDL commands in university.ddl in /sql folder  
      
      2. Put host / port / password / database name in db.yaml  
      
       Note the above step is necessary to ensure database works on your system 
<br ><br ><br >

## STEP 2  ( STARTING FLASK SERVER )  
### WINDOWS -- EVERYTHING IS AUTOMATED  

      Double click on makefile.bat -> will do all steps below  
        
      Ensure you are using python 3.7 and db.yaml is edited


### MANUAL  

      if possible use venv

      pip install -r requirements.txt

      Ensure you have edited db.yaml and imported mysql  

      Run the application by executing the command python app.py

      Use python 3.7 u

      The application runs on localhost:5000

