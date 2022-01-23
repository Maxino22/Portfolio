# My Personal Website
 This website is available at [maxino.xyz](https://maxino.xyz)
  ![Maxwell Muhanda](https://github.com/Maxino22/Portfolio/blob/master/Screenshot%20(86).png)
 This project combines the following technologies:
  1.Django (REST Framework)
  2.Vanilla Javascript (Fetch API, Es6 classes)
  3.Running applications inside dockerized containers
  4. Image cloud storage (cloudinary)
  
 # Running the application
 
 To run this application you will need to add environment variables providing database configurations as referenced in the docker-compose file as follows:
 
 # .env file
   ![maxino env](https://github.com/Maxino22/Portfolio/blob/master/env_variables.png)
   
  When all environment variables are added correctly run  
   # docker-compose up --build -d
   This will build the images required and run the application(ps you have to install Docker)
