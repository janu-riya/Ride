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
    first_name : str
    last_name : str
    aadhar_id: str
    location: str
    password : str
    mobile_number: str
    gst_number: str = None
    firm_pan_number : str = None
    natureof_business : str = None

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

#___________________________________________________________________________________________________________________________________________________
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

#Creating trips model......................................................

class Trip(BaseModel):
    id : str = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    starting_point:str
    ending_point:str
    distance:float
    customer_id:str
    driver_id:str
    vehicle_id:str
    fare:float = 50.0
    status: str = "initiated"
    


@app.get("/trip")
async def get_trip(id:str):
    try:
         filter ={
        'id' : id,
        }
         project = {
        '_id':0,
        }
         return dict(client.uber.trip.find_one(filter=filter,projection=project))
         
    except Exception as e:
        print(str(e))
        return False

@app.post("/trip")
async def create_trip(trip:Trip):
    
    try:
        filter={
        'email': trip.driver_id
        }
        ufilter = {
            "email": trip.customer_id
        }
        if(client.uber.driver.count_documents(filter)) == 1 and client.uber.user.count_documents(ufilter) == 1:
            client.uber.trip.insert_one(dict(trip))
            return trip.id
        else:
            return "not initiated"
            
    except Exception as e:
        print(str(e))
        return False
class CTrip(BaseModel):
    query :dict ={}
    key: str
    value:str 

@app.put("/trip")
async def change_trip(trip: CTrip):
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
    
@app.delete("/trip")
async def delete_trip(trip_id:str):
    try:
        filter = {
            'id' :id,

        }
        client.uber.trip.delete_one(filter=filter)
        return True
    except Exception as e:
        print(str(e))
        return False
    
#________________________________________________________CAR REGISTRATION________________________________________________________________

class Car(BaseModel):
    car_model : str
    registration_no : str
    insurance : str

@app.get("/car")
async def get_car(registration_no : str):
    try:
        filter ={
        
        'registration_no' : registration_no,
        
        }
        project = {
        '_id':0,
        }
        client.uber.car.find_one(filter=filter, project=project)
        return True
    except Exception as e:
        print(str(e))
        return False    

@app.post("/car")
async def create_car(car: Car):
    try:
        client.uber.car.insert_one(dict(car))
        return True
    except Exception as e:
        print(str(e))
        return False
    

class Ccar(BaseModel):
    query :dict ={}
    key: str
    value:str 

@app.put("/car")
async def change_car(car: Ccar):
    try:
        filter= car.query
        update={
            '$set' :{
            car.key :car.value
            }
        }
        client.uber.car.update(filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False    

@app.delete("/car")
async def delete_car(registration_no:str):
    try:
        filter = {
            'registration_no' : registration_no,

        }
        client.uber.car.delete_one(filter=filter)
        return True
    except Exception as e:
        print(str(e))
        return False  

@app.post("/car_upload_files")
def car_upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}       
  
   #Bike REGISTRATION

class bike(BaseModel):
    bike_model : str
    bike_registration_number : str
    bike_insurance_number : str
    bike_number:str

@app.get("/bike")
async def get_bike(bike_registration_number : str):
    try:
        filter ={
        
        'bike_registration_number' : bike_registration_number,
        
        }
        project = {
        '_id':0,
        }
        client.uber.bike.find_one(filter=filter, project=project)
        return True
    except Exception as e:
        print(str(e))
        return False    

@app.post("/bike")
async def create_bike(bike: bike):
    try:
        client.uber.bike.insert_one(dict(bike))
        return True
    except Exception as e:
        print(str(e))
        return False
    

class Cbike(BaseModel):
    query :dict ={}
    key: str
    value:str 

@app.put("/bike")
async def change_bike(bike: Cbike):
    try:
        filter= bike.query
        update={
            '$set' :{
            bike.key :bike.value
            }
        }
        client.uber.bike.update(filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False    

@app.delete("/bike")
async def delete_bike(bike_model:str):
    try:
        filter = {
            'bike_model' : bike_model,

        }
        client.uber.bike.delete_one(filter=filter)
        return True
    except Exception as e:
        print(str(e))
        return False 

@app.post("/bike_upload_files")
def bike_upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}
 #Auto REGISTRATION

class Auto(BaseModel):
    Auto_model : str
    Auto_registration_number : str
    Auto_insurance_number : str
    Auto_number:str

@app.get("/Auto")
async def get_Auto(Auto_registration_number : str):
    try:
        filter ={
        
        'Auto_registration_number' : Auto_registration_number,
        
        }
        project = {
        '_id':0,
        }
        client.uber.Auto.find_one(filter=filter, project=project)
        return True
    except Exception as e:
        print(str(e))
        return False    

@app.post("/Auto")
async def create_Auto(Auto: Auto):
    try:
        client.uber.Auto.insert_one(dict(Auto))
        return True
    except Exception as e:
        print(str(e))
        return False
    

class CAuto(BaseModel):
    query :dict ={}
    key: str
    value:str 

@app.put("/Auto")
async def change_Auto(Auto: CAuto):
    try:
        filter= Auto.query
        update={
            '$set' :{
            Auto.key :Auto.value
            }
        }
        client.uber.Auto.update(filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False    

@app.delete("/Auto")
async def delete_Auto(Auto_model:str):
    try:
        filter = {
            'Auto_model' : Auto_model,

        }
        client.uber.Auto.delete_one(filter=filter)
        return True
    except Exception as e:
        print(str(e))
        return False 

@app.post("/Auto_upload_files")
def Auto_upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}
