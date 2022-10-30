# Flight Management Web Application for Air Whakatū 


#### Student Name: Shan Lu
#### Student ID: 1149887
#### Student Email: shan.lu@lincolnuni.ac.nz

#### ---------------------------------------------------------------------------------------------------
## Assignment Background:

The app is developed to provide an airline flight management web application for Air Whakatū. 

1. The main page contains the following functions:

  
  - Home page & general information
    - Home page shows the general information of Air Whakatū
    - Airport Arrivals & Departures
    - Customer Login
    - New passenger registration
  The screenshot shows as below:
   
  ![image](https://user-images.githubusercontent.com/109211264/198832823-126ed784-9543-4917-a85b-ce5845809ead.png)


   - Passengers can check the arrival and departure flights information by clicking the "Arrival Flights" & "Departure Flights" individually to nevigate to the corresponding pages as below:
  
  ![image](https://user-images.githubusercontent.com/109211264/198832635-84cd98d3-1ae9-4fb4-8866-bf4afe47dd01.png)
   - Page footer shows the contact information of Air Whakatū.
  
   - On the top of the page shows the current system time "Friday 28 Oct 2022, 5.00pm"

2. Administrative system for staff
   - The airline staff can access the administrative system by typing url http://127.0.0.1:5000/admin/xx to the pages. The main page of admin system is 'admin/management' where lists all the staff, including names and position, manager or staff, the screenshot shows as below:
   
   
   ![image](https://user-images.githubusercontent.com/109211264/198833763-7237ff9e-eeb8-4daf-96c8-ffabea70a4da.png)
 
   - Staff can login by selecting their name from the list;
   
   - Each staff can check/edit passengers' list and information by clicking the "Check Passenger List" buttom; also staff can check/edit flight list by clicking the "Check Flight List" buttom:
   
   ![image](https://user-images.githubusercontent.com/109211264/198833910-eee97c76-ed99-4df3-b3c7-2215fea5e151.png)

  2.1 Staff check/update/filter passengers' information
  - Staff can see a list of all the passengers booking information by an alphabetical order, on the top of the list, staff can filter the key words to select the targeted passenger's name.
   
   ![image](https://user-images.githubusercontent.com/109211264/198834219-d05c4d7a-ad8f-4e30-adc3-af9cac82c59c.png)
   
   - Passenger's personal information can be edited by staff via typing the url e.g. "http://127.0.0.1:5000/admin/updatebooking?passengerid=1687":
   
   ![image](https://user-images.githubusercontent.com/109211264/198859604-caab5055-a672-44b4-9a6b-86608c5c3f5b.png)

   
  2.2 Staff view/update/filter flight information
  - After staff login the system, click the "Check Flights List" button to view a list of all flights by flight date, time and departure airport, also including the aircraft detials e.g. Reg mark, seating capacity and available seating numbers.
  
   ![image](https://user-images.githubusercontent.com/109211264/198859876-87ac28c6-d3ee-474c-9c9e-66a2e70c81eb.png)
   
  - Then staff enters the flight list page (url: http://127.0.0.1:5000/admin/flights_list), showing all the flights to and from all airports from the current date up to 7 days. The flight list also can be filtered by date range, departure or arrival airports (or a combination of both). See screenshot below:
  
  ![image](https://user-images.githubusercontent.com/109211264/198859998-e262463c-f622-49af-b518-080236d885a3.png)


  - Staff can view or edit flight manifest details by clicking the flight ID from the previous page, including the seating capacity and a list of all of the passengers on the selected flight, for example flight id = 10435 (AW1001):
  
  - The flight manifest list is numbered in order from 1 for the first in the list until the last passenger on the flight list, shown in column 1 "Sequence Order". Passengers are also listed in alphabetical order by last name (column 9) followed by first name (column 8).
  
  ![image](https://user-images.githubusercontent.com/109211264/198860193-cd9e2ff2-df77-40b0-b6b6-b832441aaaa2.png)

  - The output is generated from the SQL query from the back end:
  


  
  




  
3. Public system for customers - New Customer Registration, Login and Update information

  - Customer can login the system via email address on the home page, then nevigate to the login page.
  ![image](https://user-images.githubusercontent.com/109211264/198833149-dd7f0095-da68-44f9-9630-a18dd9110a79.png)
  
  - login page shows the passenger's basic information including first name, last name, email and contact number. On the bottom of the page lists the current and history booking information.
  ![image](https://user-images.githubusercontent.com/109211264/198833254-d429eafd-0d83-4ab5-a885-f9f4e5aa97fa.png)

  - Passenger can logout the account by clicking the "Logout" bottom to the main page.
  - Passenger can edit the personal information by clicking the first name to the update page where passengers can update their basic contact information and submit to system, or reset the original information.
  ![image](https://user-images.githubusercontent.com/109211264/198833460-e3f15c07-7c51-437e-8bb0-5f95262b8865.png)
  
  
  

  
  



