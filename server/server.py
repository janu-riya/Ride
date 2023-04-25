from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from random import choice
import random, string

app = FastAPI()
client = MongoClient("mongodb://localhost:27017")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#user
#___________________________________________________USER_____REGISTRATION_______________________________________________________________________
class customer(BaseModel):
    first_name : str
    last_name : str
    aadhar_id: str
    location: str
    password : str
    mobile_number: str
    gst_number: str = None
    firm_pan_number : str = None
    natureof_business : str = None


@app.get("/customer")
async def get_customer(mobile_number: str):
    try:
        filter ={
        'mobile_number' : mobile_number,
        }
        project = {
        '_id':0,
        }
        return dict(client.uber.customer.find_one(filter=filter,projection=project))
    except Exception as e:
        print(str(e))
        return False
    
@app.delete("/customer")
async def delete_customer(mobile_number:str):
    try:
        filter = {
            'mobile_number' :mobile_number,
        }
        client.uber.customer.delete_one(filter=filter)
        return True
    except Exception as e:
        print(str(e))
        return False


@app.post("/customer")
async def create_customer(customer: customer):
    try:
        client.uber.customer.insert_one(dict(customer))
        return True
    except Exception as e:
        print(str(e))
        return False
    
class Ccustomer(BaseModel):
    query :dict ={}
    key: str
    value:str 

@app.put("/customer")
async def change_customer(customer: Ccustomer):
    try:
        filter= customer.query
        update={
            '$set' :{
            customer.key :customer.value
            }
        }
        client.uber.customer.update(filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False

#____________________________________________________________________USER___LOGIN______________________________________________________________

@app.get("/customer_login")
async def customer_login(mobile_number: str, password: str):
    try:
        filter={
            'mobile_number': mobile_number,
            'password': password,
        }

        if (client.uber.customer.count_documents(filter)==1):
            return True
        else:
            return False
    except Exception as e:
        print(str(e))
        return False

#____________________________________________________________CORPORATE_REGISTRATION_____________________________________________________   
class corporate(BaseModel):
    first_name : str
    last_name : str
    firm_name : str
    email: str
    location : str
    password : str
    mobile_number: str
    gst_number: str = None
    firm_pan_no : str = None
    nature_of_business : str = None


@app.get("/corporate")
async def get_corporate(mobile_number: str):
    try:
        filter ={
        'mobile_number' : mobile_number,
        }
        project = {
        '_id':0,
        }
        return dict(client.uber.corporate.find_one(filter=filter,projection=project))
    except Exception as e:
        print(str(e))
        return False
    
@app.delete("/corporate")
async def delete_corporate(mobile_number:str):
    try:
        filter = {
            'mobile_number' :mobile_number,
        }
        client.uber.corporate.delete_one(filter=filter)
        return True
    except Exception as e:
        print(str(e))
        return False


@app.post("/corporate")
async def create_corporate(corporate: corporate):
    try:
        client.uber.corporate.insert_one(dict(corporate))
        return True
    except Exception as e:
        print(str(e))
        return False
    
class Ccorporate(BaseModel):
    query :dict ={}
    key: str
    value:str 

@app.put("/corporate")
async def change_corporate(corporate: Ccorporate):
    try:
        filter= corporate.query
        update={
            '$set' :{
            corporate.key :corporate.value
            }
        }
        client.uber.corporate.update(filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False
    
#____________________________________________________________________CORPORATE_LOGIN______________________________________________________________
@app.get("/corporate_login")
async def corporate_login(mobile_number: str, password: str):
    try:
        filter={
            'mobile_number': mobile_number,
            'password': password,
        }

        if (client.uber.corporate.count_documents(filter)==1):
            return True
        else:
            return False
    except Exception as e:
        print(str(e))
        return False
    
#__________________________________________________________________OTP API_________________________________________________________________________________________

@app.get('/otp')
async def otp(mobile_number: str):
    number =['0','1','2','3','4','5','6','7','8','9']
    otp =''
    for i in range(6):
        otp+=choice(number)
    return otp 

#________________________________________________________CORPORATE_LOGIN____________________________________________________________________    
@app.get("/corporate_login")
async def corporate_login(mobile_number: str, password: str):
    try:
        filter={
            'mobile_number': mobile_number,
        }
        pfilter={
            'password': password,
        }
        if client.uber.corporate.count_documents(filter)==0 and client.uber.corporate.count_documents(pfilter)==0:
            return "Login Successful"
        else:
            return "error in login"
    except Exception as e:
        print(str(e))
        return False
        client.uber.customer.insert_one(dict(customer))
        return True
    except Exception as e:
        print(str(e))
        return False
#Driver registration Model.....................................................

class Driver(BaseModel):
    corporate_mobile : str
    first_name : str
    last_name : str
    aadhar_id: str
    location: str
    password : str
    mobile_number: str
@app.post("/driver")
async def create_driver(driver: Driver):
    try:
        client.uber.driver.insert_one(dict(driver))
        return True
    except Exception as e:
        print(str(e))
        return False

@app.get("/driver")
async def get_driver(mobile_number:str):
    try:
        filter ={
        'mobile_number' : mobile_number,
        }
        project = {
        '_id':0,
        }
        return dict(client.uber.driver.find_one(filter=filter, projection=project))
        return True
    except Exception as e:
        print(str(e))
        return False

class CDriver(BaseModel):
    query :dict ={}
    key: str
    value:str 

@app.put("/driver")
async def change_driver(driver: CDriver):
    try:
        filter= driver.query
        update={
            '$set' :{
            driver.key :driver.value
            }
        }
        client.uber.driver.update(filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.delete("/driver")
async def delete_driver(mobile_number:str):
    try:
        filter = {
            'email' :mobile_number,

        }
        client.uber.driver.delete_one(filter=filter)
        return True
    except Exception as e:
        print(str(e))
        return False
#________________________________________________________________Driver_login_________________________________________________________________

@app.get("/driver_login")
async def driver_login(mobile_number: str, password: str):
    try:
        filter={
            'mobile_number': mobile_number,
            'password': password,
        }

        if (client.uber.driver.count_documents(filter)==1):
            return True
        else:
            return False
    except Exception as e:
        print(str(e))
        return False


#______________________________________________________________CORPORATE_BANK_API_____________________________________________________________________________

class CorporateBank(BaseModel):
    mobile_number: str
    pan_number : str
    select_bank : str
    account_name: str
    account_number : str
    ifsc_code: str

@app.post("/corporate_bank")
async def create_corporate_bank(CorporateBank: CorporateBank):
    try:
        client.uber.CorporateBank.insert_one(dict(CorporateBank))
        return True
    except Exception as e:
        print(str(e))
        return False

@app.get("/corporate_bank")
async def get_corporate_bank(account_number:str):
    try:
        filter ={
        'account_number' : account_number,
        }
        project = {
        '_id':0,
        }
        return dict(client.uber.CorporateBank.find_one(filter=filter, projection=project))
        return True
    except Exception as e:
        print(str(e))
        return False

class Ccorporate_bank(BaseModel):
    query :dict ={}
    key: str
    value:str 

@app.put("/corporate_bank")
async def change_corporate_bank(CorporateBank: Ccorporate_bank):
    try:
        filter= CorporateBank.query
        update={
            '$set' :{
            CorporateBank.key :CorporateBank.value
            }
        }
        client.uber.CorporateBank.update(filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.delete("/corporate_bank")
async def delete_corporate_bank(account_number:str):
    try:
        filter = {
            'email' :account_number,

        }
        client.uber.CorporateBank.delete_one(filter=filter)
        return True
    except Exception as e:
        print(str(e))
        return False

#____________________________________________________________VEHICLE REGISTRATION_______________________________________________________________________________________
class Vehicle(BaseModel):
    mobile_number:str
    owner_name : str
    supplier_type : str
    vehicle_type: str
    fuel_type: str
    vehicle_capacity: str
    registration_no: str
    insurance_no: str
    issue_date: str
    expiry_date: str
    

@app.post("/vehicle")
async def create_vehicle(Vehicle: Vehicle):
    try:
        client.uber.Vehicle.insert_one(dict(Vehicle))
        return True
    except Exception as e:
        print(str(e))
        return False

@app.get("/vehicle")
async def get_vehicle(owner_name:str):
    try:
        filter ={
        'owner_name' : owner_name,
        }
        project = {
        '_id':0,
        }
        return dict(client.uber.vehicle.find_one(filter=filter, projection=project))
        return True
    except Exception as e:
        print(str(e))
        return False

class V_vehicle(BaseModel):
    query :dict ={}
    key: str
    value:str 

@app.put("/Vehicle")
async def change_vehicle(Vehicle: V_vehicle):
    try:
        filter= Vehicle.query
        update={
            '$set' :{
            Vehicle.key :Vehicle.value
            }
        }
        client.uber.Vehicle.update(filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.delete("/Vehicle")
async def delete_vehicle(registration_no:str):
    try:
        filter = {
            'registration_no' :registration_no,

        }
        client.uber.Vehicle.delete_one(filter=filter)
        return True
    except Exception as e:
        print(str(e))
        return False

#_____________________________________________________________________BANK___API____________________________________________________________________
class Bank(BaseModel):
    pan_number : str
    select_bank : str
    account_name: str
    account_number : str
    ifsc_code: str

@app.post("/bank")
async def create_bank(bank: Bank):
    try:
        client.uber.bank.insert_one(dict(bank))
        return True
    except Exception as e:
        print(str(e))
        return False

@app.get("/bank")
async def get_bank(account_number:str):
    try:
        filter ={
        'account_number' : account_number,
        }
        project = {
        '_id':0,
        }
        return dict(client.uber.bank.find_one(filter=filter, projection=project))
        return True
    except Exception as e:
        print(str(e))
        return False

class Cbank(BaseModel):
    query :dict ={}
    key: str
    value:str 

@app.put("/bank")
async def change_bank(bank: Cbank):
    try:
        filter= bank.query
        update={
            '$set' :{
            bank.key :bank.value
            }
        }
        client.uber.bank.update(filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.delete("/bank")
async def delete_bank(account_number:str):
    try:
        filter = {
            'account_number' :account_number,

        }
        client.uber.bank.delete_one(filter=filter)
        return True
    except Exception as e:
        print(str(e))
        return False
#_____________________________________________________________________________________________________________________________________________________________
class trip(BaseModel):
    id : str = ""
    mobile_number:str
    current_location: str
    Select_Your_destination: str
    Number_of_Seats: str
    select_car: str
    date: str
    time:str

@app.get("/trip")
async def get_trip(id: str):
    try:
        filter ={
        'id' : id,
        }
        project = {
        '_id':0,
        }
        return list(client.uber.trip.find(filter=filter,projection=project))
    except Exception as e:
        print(str(e))
        return False
    
@app.delete("/trip")
async def delete_trip(id:str):
    try:
        filter = {
            'id' : id,
        }
        client.uber.trip.delete_one(filter=filter)
        return True
    except Exception as e:
        print(str(e))
        return False


@app.post("/trip")
async def create_trip(trip: trip):
    try:
        trip.id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        client.uber.trip.insert_one(dict(trip))
        return True
    except Exception as e:
        print(str(e))
        return False
    
class Ctrip(BaseModel):
    query :dict ={}
    key: str
    value:str 

@app.put("/trip")
async def change_Trip(trip: Ctrip):
    try:
        filter= trip.query
        update={
            '$set' :{
            trip.key :trip.value
            }
        }
        client.uber.trip.update(filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False
    
#_______________________________________________________________________________________________________________________
@app.get("/trip/user/all")
async def user_trips(mobile_number: str):
    try:
        filter={
            'mobile_number': mobile_number,
        }
        project={'_id':0}
        return list(client.uber.trip.find(filter=filter,projection=project))
        
        
    except Exception as e:
        print(str(e))
        return False    
#______________________________________________________________________________

@app.get("/trip/all")
async def get_all_trip():
    
    try:
        filter={}
        project={
            '_id': 0
        }
        return list(client.uber.trip.find(filter=filter,projection=project))
        
    except Exception as e:
        print(str(e))
        return False

@app.delete("/trip/all")
async def delete_trip(id: str):
    try:
        filter={
            'id': id,
        }
        project={
            
        }
        client.uber.trip.delete_one(filter=filter,projection=project)
        return True
    except Exception as e:
        print(str(e))
        return False
#Creating quote model......................................................
class quote(BaseModel):
    id: str
    mobile_number: str
    driver_number: str
    Select_the_vehicle: str
    Select_the_driver: str
    waiting_charge: str
    total_amount: str
    car_number: str

@app.get("/quote")
async def get_quote(car_number: str):
    try:
        filter ={
        'car_number' : car_number,
        }
        project = {
        '_id':0,
        }
        return dict(client.uber.quote.find_one(filter=filter,projection=project))
    except Exception as e:
        print(str(e))
        return False
    
@app.delete("/quote")
async def delete_quote(car_number:str):
    try:
        filter = {
            'car_number' :car_number,
        }
        client.uber.quote.delete_one(filter=filter)
        return True
    except Exception as e:
        print(str(e))
        return False


@app.post("/quote")
async def create_quote(quote: quote):
    try:
        client.uber.quote.insert_one(dict(quote))
        return True
    except Exception as e:
        print(str(e))
        return False
    
class Cquote(BaseModel):
    query :dict ={}
    key: str
    value:str 

@app.put("/quote")
async def change_Quote(quote: Cquote):
    try:
        filter= quote.query
        update={
            '$set' :{
            quote.key :quote.value
            }
        }
        client.uber.quote.update(filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False
    
@app.get("/quote/user/all")
async def get_all_quotes(mobile_number: str):
    
    try:
        filter={
            'mobile_number': mobile_number,
        }
        project={
            '_id': 0,
        }
        return list(client.uber.quote.find(filter=filter,projection=project))
        
    except Exception as e:
        print(str(e))
        return False
    
@app.get("/quote/driver/all")
async def get_all_quotes(driver_number: str):
    
    try:
        filter={
            'driver_number': driver_number,
        }
        project={
            '_id': 0,
        }
        return list(client.uber.quote.find(filter=filter,projection=project))
        
    except Exception as e:
        print(str(e))
        return False
    
#____________________________________________________________PAYMENT_______________________________________________________

class Payment(BaseModel):
    name: str
    mobile_number:str
    card_number: str
    exp_month: str
    exp_date: str
    cvv: str

# Define a route to handle payment requests
@app.post("/payment")
async def process_payment(payment: Payment):
    try:
        client.uber.payment.insert_one(dict(payment))
        return True
    except Exception as e:
        print(str(e))
        return False
    