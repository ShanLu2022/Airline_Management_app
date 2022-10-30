import pandas as pd
import mysql.connector
from flask import Flask
from flask import render_template
from flask import request, session
from flask import redirect
from flask import url_for
import mysql.connector
import connect
import uuid


pd.set_option('display.width', 1280)
pd.set_option('display.max_columns', 20)


current_time = pd.to_datetime('2022-10-28 17:00:00')
print(current_time)

"""Test connection below"""
# mydb = mysql.connector.connect(
#     host="localhost",
#     database='airline',
#     user="root",
#     password="Welcome123"
# )
#
# print(mydb)
#
# query = "select * from airline.flight;"
# output = pd.read_sql(query, mydb)
# print(output)


arrival = """Select ar.FlightNum, ar.ArrCode, ap.AirportName, af.FlightDate, af.DepTime, af.DepEstAct, 
af.FlightStatus from airline.route ar left join airline.flight af on ar.FlightNum = af.FlightNum left join 
airline.airport ap on ap.AirportCode = ar.ArrCode Where af.FlightDate >=DATE_ADD('2022-10-28 17:00:00', interval -2 
day) and af.FlightDate <=DATE_ADD('2022-10-28 17:00:00', interval 5 day) Order by af.FlightDate desc """

depart = """Select ar.FlightNum, ar.depCode, ap.AirportName, af.FlightDate, af.ArrTime, af.ArrEstAct, af.FlightStatus
from airline.route ar
left join airline.flight af on ar.FlightNum = af.FlightNum
left join airline.airport ap on ap.AirportCode = ar.depCode
Where af.FlightDate >=DATE_ADD('2022-10-28 17:00:00', interval -2 day) and af.FlightDate <=DATE_ADD('2022-10-28 17:00:00', interval 5 day)
Order by af.FlightDate desc"""


dbconn = None

app = Flask(__name__)

"""Create function to connect database"""
def getCursor():
    global dbconn
    global connection
    if dbconn == None:
        connection = mysql.connector.connect(user=connect.dbuser, \
        password=connect.dbpass, host=connect.dbhost, \
        database=connect.dbname, autocommit=True)
        dbconn = connection.cursor(buffered=True)
        return dbconn
    else:
        return dbconn


"""Use UUID to generate primary key for passenger ID"""
def genID():
    return uuid.uuid4().fields[1]


"""Main page of the website"""
@app.route("/")
def Main_Page():
    # return "Test"
    return render_template('index.html')


"""Shows the arrival page and departure flights"""
@app.route("/arr_info")
def flight_arr():
    cur = getCursor()
    cur.execute(arrival)
    arr_result = cur.fetchall()

    column_names = [item[0] for item in cur.description]

    return render_template('arrivals_info.html', data=arr_result, name='Arrival Flights')


"""Shows the departure page and departure flights"""
@app.route("/dep_info")
def flight_dep():
    cur = getCursor()
    cur.execute(depart)
    dep_result = cur.fetchall()
    return render_template('dep_info.html', data=dep_result, name='Departure Flights')


"""Customer login function"""
@app.route("/customer", methods=['GET', 'POST'])
def cust_login():
    cur = getCursor()

    login_log = ''
    if request.method=='POST':
        customer_email = request.form['email_address']
        cur.execute("Select pas.PassengerID, pas.FirstName, pas.LastName, pas.EmailAddress, pas.PhoneNumber, pas.DateOfBirth, "
                    "apt.AirportName, af.FlightNum, af.FlightDate, af.DepTime, af.ArrTime, af.FlightStatus, af.Aircraft "
                    "from airline.passenger pas left join airline.passengerFlight psf on pas.PassengerID = psf.PassengerID "
                    "left join airline.flight  af on psf.FlightID = af.FlightID  "
                    "left join airline.route rt on af.FlightNum = rt.FlightNum "
                    "left join airline.airport apt on rt.DepCode = apt.AirportCode "
                    "where pas.EmailAddress=%s order by af.FlightDate desc", (customer_email,))
        cus_record = cur.fetchall()

        if cus_record:
            # session['EmailAddress'] = cus_record[3]
            return render_template('customer_page.html', data=cus_record, name=cus_record)
            # return redirect(url_for('customer_page'))
        else:
            login_log = 'Email address cannot be found, please register a new account.'
            return render_template('passenger_register.html', login_log=login_log)


"""Register Passenger information"""
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("passenger_register.html")
    else:
        passengerid = genID()
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        emailaddress = request.form['emailaddress']
        phonenumber = request.form['phonenumber']
        passportnumber = request.form['passportnumber']
        dateofbirth = request.form['dateofbirth']

        cur = getCursor()
        cur.execute("INSERT INTO airline.passenger (PassengerID, FirstName, LastName, EmailAddress, PhoneNumber, PassportNumber, DateOfBirth, LoyaltyTier) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, 1)", (str(passengerid), firstname, lastname, emailaddress, phonenumber, passportnumber, dateofbirth, ))
        connection = mysql.connector.connect(user=connect.dbuser, password=connect.dbpass, host=connect.dbhost, database=connect.dbname, autocommit=True)
        connection.commit()

        return redirect(url_for('Main_Page'))


"""Logout function"""
@app.route('/logout')
def logout():
    # return redirect(url_for('index'))
    return render_template('index.html')


"""Passenger Update Contact function"""
@app.route('/customer/update', methods=['GET', 'POST'])
def customer_update():
    if request.method == 'POST':
        passengerid = request.form.get('passengerid')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        phonenumber = request.form.get('phonenumber')
        dateofbirth = request.form.get('dateofbirth')
        cur = getCursor()

        print(str(passengerid), firstname, lastname, phonenumber, dateofbirth)
        cur.execute("Update airline.passenger Set FirstName = %s, LastName = %s, PhoneNumber= %s, DateOfBirth=%s Where PassengerID=%s", (firstname, lastname, phonenumber, dateofbirth, str(passengerid),))
        return redirect(url_for("Main_Page"))
        # return render_template('customer_page.html')
    else:
        id = request.args.get('passengerid')
        if id == '':
            return redirect('customer_page')
        else:
            cur = getCursor()
            cur.execute("Select pas.PassengerID, pas.FirstName, pas.LastName, pas.EmailAddress, pas.PhoneNumber, pas.DateOfBirth, "
                    "af.FlightNum, af.FlightDate, af.DepTime, af.ArrTime, af.FlightStatus, af.Aircraft "
                    "from airline.passenger pas left join airline.passengerFlight psf on pas.PassengerID = psf.PassengerID "
                    "left join airline.flight  af on psf.FlightID = af.FlightID  "
                    "where pas.PassengerID=%s order by af.FlightDate desc", (str(id),))
            select_result = cur.fetchone()
            return render_template('customer_form.html', customerdetails=select_result)


"""Customer check available flights by selecting the """
@app.route('/admin/manifest')
def flight_manifest():
    flightid = request.args.get('flightid')
    cur = getCursor()
    cur.execute("Select @n:=(@n := @n +1) AS Seq_Num, t.FlightID, t.FlightNum, t.FlightDate, t.Aircraft, t.DepTime, t.FlightStatus, t.Seating, t.PassengerID, t.FirstName, t.LastName, t.EmailAddress "
                "from (Select fl.FlightID, fl.FlightNum, fl.FlightDate, fl.Aircraft, fl.DepTime,fl.FlightStatus, ac.Seating, ps.PassengerID, ps.FirstName, ps.LastName, ps.EmailAddress "
                "from airline.flight fl "
                "left join airline.passengerFlight pasf on fl.FlightID = pasf.FlightID "
                "left join airline.passenger ps on pasf.PassengerID = ps.PassengerID "
                "left join airline.aircraft ac on fl.Aircraft = ac.RegMark "
                "Where fl.FlightID = %s Order by ps.LastName asc, ps.FirstName asc) t Cross join (SELECT @n:= 0) AS parameter", (str(flightid),))
    select_result = cur.fetchall()
    return render_template('flight_manifest.html', data=select_result, name=select_result)


"""Admin page - first showing the management page"""
@app.route('/admin/management')
def management():
    cur = getCursor()
    login_admin = ''
    cur.execute("Select sf.FirstName, sf.LastName, "
                    "Case When (sf.IsManager = 0) Then 'Staff' when (sf.IsManager = 1) Then 'Manager' End as 'Position' "
                    "From airline.staff sf ")
    management_record = cur.fetchall()
    if management_record:

        return render_template('management.html', data=management_record, name='management_record')


"""Staff login by clicking the their last name"""
@app.route('/admin/staff')
def search_staff():
    lastname = request.args.get('lastname')
    print(lastname)
    cur = getCursor()
    cur.execute("Select sf.FirstName, sf.LastName, sf.EmailAddress, "
                "Case When (sf.IsManager = 0) Then 'Staff' when (sf.IsManager = 1) Then 'Manager' End as 'Position' "
                "from airline.staff sf Where sf.LastName=%s ", (lastname,))
    select_result = cur.fetchone()
    return render_template('staff_page.html', data=select_result, name=select_result)


"""Show a list of all the flights to the selected staff"""
sql_flight_list = """Select t.Dep_Airport, t.Arr_Airport, t.FlightDate, t.DepTime, t.ArrTime, t.FlightStatus, t.RegMark, t.Total_Seating, t.Seat_Booked, t.Available_Seats, t.FlightNum, t.FlightID
                        From (
                        Select fl.FlightID, fl.FlightNum, rt.DepCode, rt.arrCode, ap.AirportName as 'Dep_Airport', arr_p.AirportName as 'Arr_Airport', fl.FlightDate, fl.DepTime, fl.ArrTime, fl.FlightStatus, fl.Aircraft as 'RegMark', ac.Seating as 'Total_Seating', COUNT(psf.PassengerID) as 'Seat_Booked', (ac.Seating - COUNT(psf.PassengerID)) as 'Available_Seats'
                        from airline.flight fl
                        left join airline.route rt on fl.FlightNum = rt.FlightNum
                        left join airline.airport ap on rt.DepCode = ap.AirportCode
                        left join airline.airport arr_p on rt.ArrCode = arr_p.AirportCode
                        left join airline.aircraft ac on fl.Aircraft = ac.RegMark
                        left join airline.passengerFlight psf on fl.FlightID = psf.FlightID
                        Group by fl.FlightID, fl.FlightNum, rt.DepCode, ap.AirportName, fl.FlightDate, fl.DepTime, fl.ArrTime, fl.FlightStatus, fl.Aircraft, ac.Seating) as t
                        Where t.Available_Seats >=0 and t.FlightDate <= DATE_ADD('2022-10-28 17:00:00', interval 7 day) and t.FlightDate >= '2022-10-28'
                        Order by t.FlightDate, t.DepTime, t.Dep_Airport"""
@app.route('/admin/flights_list')
def show_flight_list():
    cur = getCursor()
    cur.execute(sql_flight_list)

    flight_info = cur.fetchall()

    return render_template('flight_info.html', data=flight_info, name=flight_info)


"""Show a list of all passengers to the selected staff, including all the information"""
@app.route('/admin/information')
def check_passenger_list():
    cur = getCursor()
    cur.execute(
        "Select pas.PassengerID, pas.FirstName, pas.LastName, pas.EmailAddress, pas.PhoneNumber,"
        "af.FlightDate, af.DepTime, af.ArrTime, af.FlightStatus, af.Aircraft "
        "from airline.passenger pas left join airline.passengerFlight psf on pas.PassengerID = psf.PassengerID "
        "left join airline.flight  af on psf.FlightID = af.FlightID "
        "Where af.FlightDate is not null and af.FlightDate >= '2022-10-28'"
        "order by pas.LastName, pas.FirstName asc")

    passenger_info = cur.fetchall()

    return render_template('passenger_info.html', data=passenger_info, name=passenger_info)


"""Staff edit passenger details"""
@app.route('/admin/updatebooking', methods=['GET', 'POST'])
def updatebooking():
    if request.method == 'POST':
        passengerid = request.form.get('passengerid')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        phonenumber = request.form.get('phonenumber')
        dateofbirth = request.form.get('dateofbirth')
        cur = getCursor()

        print(str(passengerid), firstname, lastname, phonenumber, dateofbirth)
        cur.execute("Update airline.passenger Set FirstName = %s, LastName = %s, PhoneNumber= %s, DateOfBirth=%s Where PassengerID=%s", (firstname, lastname, phonenumber, dateofbirth, str(passengerid),))
        return redirect(url_for("Main_Page"))
        # return render_template('customer_page.html')
    else:
        id = request.args.get('passengerid')
        if id == '':
            return redirect('customer_page')
        else:
            cur = getCursor()
            cur.execute("Select pas.PassengerID, pas.FirstName, pas.LastName, pas.EmailAddress, pas.PhoneNumber, pas.DateOfBirth, "
                    "af.FlightNum, af.FlightDate, af.DepTime, af.ArrTime, af.FlightStatus, af.Aircraft "
                    "from airline.passenger pas left join airline.passengerFlight psf on pas.PassengerID = psf.PassengerID "
                    "left join airline.flight  af on psf.FlightID = af.FlightID  "
                    "where pas.PassengerID=%s order by af.FlightDate desc", (str(id),))
            select_result = cur.fetchone()
            return render_template('passenger_form.html', customerdetails=select_result)


"""Edit flight details"""
@app.route('/admin/editflight', methods=['GET', 'POST'])
def editflight():
    if request.method == 'POST':
        flightid = request.form.get('flightid')
        flightdate = request.form.get('flightdate')
        deptime = request.form.get('deptime')
        arrtime = request.form.get('arrtime')
        flightstatus = request.form.get('flightstatus')
        aircraft = request.form.get('aircraft')
        cur = getCursor()

        print(str(flightid), flightdate, deptime, arrtime, flightstatus)
        cur.execute("Update airline.flight Set FlightDate = %s, DepTime = %s, ArrTime = %s, FlightStatus=%s, Aircraft=%s "
                    "Where FlightID = %s", (flightdate, deptime, arrtime, flightstatus, aircraft, str(flightid),))
        return redirect(url_for("show_flight_list"))

    else:
        flightid = request.args.get('flightid')
        if id == '':
            return redirect('customer_page')
        else:
            cur = getCursor()
            cur.execute("Select  FlightID, FlightNum, FlightDate, DepTime, ArrTime, FlightStatus, Aircraft "
                        "from airline.flight Where FlightID=%s", (str(flightid),))
            select_result = cur.fetchone()
            return render_template('flight_form.html', flightdetails=select_result)



if __name__ == "__main__":
    app.run(debug=True)
