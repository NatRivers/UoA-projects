#About this project
This project is divided into 2: Back-end and Front-end. 

##Back-End 
We are tasked to use C# and .Net to implement the back-end part. Additionally, we used SQLite Studio software to get the overview of our database entry and also to implement our database. To import and update (populate) the database into our C# project, dotnet installation is required in order to run the project, it can be installed using the following command in the terminal:
```
dotnet new tool-manifest
dotnet tool install dotnet-ef
```
After installing dotnet, run the following in the terminal within the project directory to populate the database:
```
dotnet ef migrations add initial
dotnet ef databse update
```
The database information will be located in the migrations directory that should now appear within the project directory.

To test the back-end part, we are required to use Postman software using JSON requests.

##Front-End
Independent from the back-end, we were given a finished server file to construct a website using HTML, CSS and JavaScript. SQLite Studio software is recommended to see the overall database data entry and their format. To run the given server, dotnet is required then run the following codes located in the server directory:
```
dotnet A3.dll
```
Once the server runs, we can now open the HTML file with all data populated.
