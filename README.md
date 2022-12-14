# Flight Management Web Application for Air Whakatū 


#### Student Name: Shan Lu
#### Student ID: 1149887
#### Student Email: shan.lu@lincolnuni.ac.nz

#### ---------------------------------------------------------------------------------------------------
# Assignment Background:

The app is developed to provide an airline flight management web application for Air Whakatū. It has been deployed in my local server as well as my Pythonanywhere public server at "http://woshipanda2022.pythonanywhere.com/".

1. Database and project structure 


   1.1 The database was created from "Airline_create_schema_web_app.sql" file provided, and imported into both my local MySQL database and Pythonanywhere server. The database schema in MySQL database shown as below:
  
  ![image](https://user-images.githubusercontent.com/109211264/198868731-5a39e34f-e8a4-460b-a671-bab792b48f15.png)
  
   A similar database was created in Pythonanywhere
  
  ![image](https://user-images.githubusercontent.com/109211264/198868811-550886c9-9d03-4672-9a87-882e7affd151.png)

  1.2 The project structure 
  
  
  My assumption is as the web app is built by Python Flask, so a standard project structure should be created clearly for further maintenance and developed, for example, in the main project repository, the python files only appear to cover all the main functions or database connection; all the html pages should be saved in the 'templates' folder. So the structure of project repository was built as below:
  
    - Project repository
      - app.py
      - connect.py
      - templates
        - html files
        - supportive image & other files
   
   - app.py file includes the main function of the Flask app, all the functions, variables and methods to call all the html files.
   - connecy.py file saves the varibles (e.g. host, databasename, user and password) to connect database. 
   Assumption: since the data source connection is different between my local MySQL database and the data deployed in Pythonanywhere, so there should be a difference of data connect configuration file.
   - Variables to connect my local database:
   
   ```
  dbuser = "root"
  dbpass = "Welcome123" 
  dbhost = "localhost"
  dbport = "3306"
  dbname = "airline"
  ```
   - Variables to use the data in PythonAnywhere:
   ```
  dbuser = "woshipanda2022" 
  dbpass = "woyaofacai2022$" 
  dbhost = "woshipanda2022.mysql.pythonanywhere-services.com"
  dbname = "woshipanda2022$airline"
  ```
   
   - Folder 'templates' saves all the html files for the web app, supportive image, css file and js file.
   
   

2. Web application

Home page design. My assumption is the home page should include all the main and general functions, and easy to use for the new visitors, as well as clear to show the general airline information of air Whakatū. For instance a new visitor first time uses the website or in a rush time and does not ant to take a long time to register, so the basic information of the airline and the arrival and departure information should be easily accessed. As a result, on the home page it is easily to nevigate to the arrival and departure information. And my home page is designed as below:
 
  - Home page can be accessed via typing url: http://woshipanda2022.pythonanywhere.com/ or local server: http://127.0.0.1:5000/
    - Home page shows the general information of Air Whakatū
    - Airport Arrivals & Departures
    - Customer Login
    - New passenger registration
  The screenshot shows as below:
   
   ![image](https://user-images.githubusercontent.com/109211264/198869596-40d7e8fe-2263-4068-bccf-9c83c330dc54.png)  



   - Passengers can check the arrival and departure flights information by clicking the "Arrival Flights" & "Departure Flights" individually to nevigate to the corresponding pages as below:
  
   ![image](https://user-images.githubusercontent.com/109211264/198832635-84cd98d3-1ae9-4fb4-8866-bf4afe47dd01.png)
   
   - Page footer shows the contact information of Air Whakatū.
  
   - On the top of the page shows the current system time "Friday 28 Oct 2022, 5.00pm"
  

3. Administrative system for staff

My assumption is since the administrative system is only for the staff use only, so the visitors or passengers cannot access the system, however, there is no staff password data and no confidential information required, so a different access to passenger and staff was not developed. Furthermore, all the admin urls should be differentiated from the normal website routes, so all the admin page addresses begin with admin/xxx. The admin pages are designed as below:

   - The airline staff can access the administrative system by typing url https://woshipanda2022.pythonanywhere.com/admin/xx or local server http://127.0.0.1:5000/admin/xx to the pages. The main page of system admin is at 'admin/management' where lists all the staff, including names and position, manager or staff, the screenshot shows as below:
   
   
     ![image](https://user-images.githubusercontent.com/109211264/198833763-7237ff9e-eeb8-4daf-96c8-ffabea70a4da.png)
 
   - Staff can login by selecting their name from the list;
   
   - Each staff can check/edit passengers' list and information by clicking the "Check Passenger List" buttom; also staff can check/edit flight list by clicking the "Check Flight List" buttom:
   
     ![image](https://user-images.githubusercontent.com/109211264/198833910-eee97c76-ed99-4df3-b3c7-2215fea5e151.png)

  3.1 Staff check/update/filter passengers' information
  - Staff can see a list of all the passengers booking information by an alphabetical order, on the top of the list, staff can filter the key words to select the targeted passenger's name.
   
     ![image](https://user-images.githubusercontent.com/109211264/198834219-d05c4d7a-ad8f-4e30-adc3-af9cac82c59c.png)
   
   - Passenger's personal information can be edited by staff via typing the url e.g. "https://woshipanda2022.pythonanywhere.com/admin/updatebooking?passengerid=1664" or local server "http://127.0.0.1:5000/admin/updatebooking?passengerid=1687":
   
     ![image](https://user-images.githubusercontent.com/109211264/198859604-caab5055-a672-44b4-9a6b-86608c5c3f5b.png)

   
  3.2 Staff view/update/filter flight information
  
  This page shows the staff's function after login the system. My assumption is since each staff can have many operations in the system, so it is better to separate the basic staff information and the other functions in different pages rather than having all the information together, for example, on the staff login page, it only shows the basic details of the staff, then the other functions can be nevigated from each staff page, the structure  of staff system is designed shown as below:
  
  
    - Staff login
      - basic information
      - other information
         - Edit/check passenger details
         - Edit/check flight manifest

  
  
  - After staff login the system, click the "Check Flights List" button to view a list of all flights by flight date, time and departure airport, also including the aircraft detials e.g. Reg mark, seating capacity and available seating numbers.
  
    ![image](https://user-images.githubusercontent.com/109211264/198859876-87ac28c6-d3ee-474c-9c9e-66a2e70c81eb.png)
   
  - Then staff enters the flight list page (url: https://woshipanda2022.pythonanywhere.com/admin/flights_list or local server http://127.0.0.1:5000/admin/flights_list), showing all the flights to and from all airports from the current date up to 7 days. The flight list also can be filtered by date range, departure or arrival airports (or a combination of both). See screenshot below:
  
    ![image](https://user-images.githubusercontent.com/109211264/198859998-e262463c-f622-49af-b518-080236d885a3.png)


  - Staff can view or edit flight manifest details by clicking the flight ID from the previous page, including the seating capacity and a list of all of the passengers on the selected flight, for example flight id = 10435 (AW1001):
  
  - The flight manifest list is numbered in order from 1 for the first in the list until the last passenger on the flight list, shown in column 1 "Sequence Order". Passengers are also listed in alphabetical order by last name (column 9) followed by first name (column 8).
  
   ![image](https://user-images.githubusercontent.com/109211264/198860193-cd9e2ff2-df77-40b0-b6b6-b832441aaaa2.png)

  Here is a request that to show the list is numbered in order, my assumption is the code should be easily maintained and updated, and if there is any new or large information required on the page, then it would take a complex process and long time to update the html page, so my decision is to create the sequence order from the MySQL side via using a variable and loop for each row by adding 1, then pass the row order to the page. The output is generated from the SQL query and saved in the app.py file by passing the selected flight id.
  
```python
def flight_manifest():
    flightid = request.args.get('flightid')
    cur = getCursor()
    cur.execute("Select @n:=(@n := @n +1) AS Seq_Num, t.FlightID, t.FlightNum, 
    t.FlightDate, t.Aircraft, t.DepTime, t.FlightStatus, t.Seating, t.PassengerID, t.FirstName, t.LastName, t.EmailAddress "
                "from (Select fl.FlightID, fl.FlightNum, fl.FlightDate, fl.Aircraft, fl.DepTime,
                fl.FlightStatus, ac.Seating, ps.PassengerID, ps.FirstName, ps.LastName, ps.EmailAddress "
                "from airline.flight fl "
                "left join airline.passengerFlight pasf on fl.FlightID = pasf.FlightID "
                "left join airline.passenger ps on pasf.PassengerID = ps.PassengerID "
                "left join airline.aircraft ac on fl.Aircraft = ac.RegMark "
                "Where fl.FlightID = %s Order by ps.LastName asc, ps.FirstName asc) t Cross join (SELECT @n:= 0) AS parameter", (str(flightid),))
```


  
  - Staff can update/edit passengers' details by clicking the passenger's email address on the page, same as tge passenger list mentioned above.
  
  - Managers can edit the details of a flight by clicking the flight number from from the flight list page. Click submit to save the new information in the database.
  
  ![image](https://user-images.githubusercontent.com/109211264/198876044-9208fac0-9bd1-4564-aebe-f5a6c632b1b9.png)

  
  
4. Public system for customers - New Customer Registration, Login and Update information

  - Customer can login the system via email address on the home page, then nevigate to the passenger welcome page.
  
  ![image](https://user-images.githubusercontent.com/109211264/198833149-dd7f0095-da68-44f9-9630-a18dd9110a79.png)
  
  - If the inpout email address cannot be found in the system, it will be nevigate to the new customer register page, which is shown below:
  
  ![image](https://user-images.githubusercontent.com/109211264/198870091-2be750dd-b985-4f0d-968b-5ca86b3c6c47.png)

  - The register information requires valid inputs for email address e.g. xxxx@xxx and phone number e.g. +/0064 123 123, if invalid values input into the page, it shows alert message as below:
 
   ![image](https://user-images.githubusercontent.com/109211264/198873305-7d00bbbd-20fb-4fdf-b558-c77006c2a9dc.png)

  
  
  - login page shows the passenger's basic information including first name, last name, email and contact number. On the bottom of the page lists the current and history booking information.
  
  ![image](https://user-images.githubusercontent.com/109211264/198833254-d429eafd-0d83-4ab5-a885-f9f4e5aa97fa.png)

  - Passenger can logout the account by clicking the "Logout" bottom to the home page.
  
  - Passenger can edit the personal information by clicking the first name to the update page where passengers can update their basic contact information and submit to system, or reset back to the original information.
  
  ![image](https://user-images.githubusercontent.com/109211264/198833460-e3f15c07-7c51-437e-8bb0-5f95262b8865.png)
  
  
  
  
  

  
  



