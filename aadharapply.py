import random
import time
import re

randomchars = "1234567890"

def generate_id():
    """Generate a random Aadhar ID consisting of three parts of 4 digits each."""
    part1 = ''.join(random.choices(randomchars, k=4))
    part2 = ''.join(random.choices(randomchars, k=4))
    part3 = ''.join(random.choices(randomchars, k=4))
    return f"{part1} {part2} {part3}"

def validate_pincode(pincode):
    """Check if the pincode is a 6-digit number."""
    return pincode.isdigit() and len(pincode) == 6

def validate_phone_number(phone_number):
    """Check if the phone number is a 10-digit number."""
    return phone_number.isdigit() and len(phone_number) == 10

def validate_dob(dob):
    """Validate date of birth format (DD/MM/YYYY)."""
    return bool(re.match(r'\d{2}/\d{2}/\d{4}', dob))

def aadhar_apply():
    print("Welcome to the Aadhar card application system.")
    print("**********************************************")
    
    
    name = input("Name: ")
    
    while True:
        dob = input("Date of Birth (DD/MM/YYYY): ")
        if validate_dob(dob):
            break
        else:
            print("Invalid Date of Birth format. Please enter in DD/MM/YYYY format.")
    
    gender = input("Gender (M/F/Other): ")
    father_name = input("Father's Name: ")
    mother_name = input("Mother's Name: ")
    nationality = input("Nationality: ")
    religion = input("Religion: ")
    id_proff = input("Any id_proff: ")
    
    while True:
        phone_number = input("Phone Number: ")
        if validate_phone_number(phone_number):
            break
        else:
            print("Invalid phone number. It should be a 10-digit number.")
    
    address = input("Address: ")
    
    while True:
        pincode = input("Pincode: ")
        if validate_pincode(pincode):
            break
        else:
            print("Invalid pincode. It should be a 6-digit number.")
    
    district = input("District: ")
    
  
    user_id = generate_id()

    print("\nProcessing your details, please wait...")
    time.sleep(15)  
    
    print("\nAadhar Card Details:")
    print("\n********************")
    print(f"Aadhar ID: {user_id}")
    print(f"Name: {name}")
    print(f"DOB: {dob}")
    print(f"Gender: {gender}")
    print(f"Nationality: {nationality}")
    print(f"Address: s/o : {father_name},\n{address},\n{pincode},{district }")

aadhar_apply()