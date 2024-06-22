from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Functions to generate fake data
def ACCOUNTNAME():
    return fake.name()

def ACCOUNTNUMBER():
    return fake.iban()

def AGE():
    return fake.random_int(min=18, max=90)

def AMOUNT():
    return fake.random_number(digits=4)

def BIC():
    return fake.swift()

def BITCOINADDRESS():
    bitcoin_address = fake.sha256(raw_output=False)[:34]  # Generate a random SHA256 hash and truncate to 34 characters
    return bitcoin_address

def BUILDINGNUMBER():
    return fake.building_number()

def CITY():
    return fake.city()

def COMPANYNAME():
    return fake.company()

def COUNTY():
    return fake.country()

def CREDITCARDCVV():
    return fake.credit_card_security_code()

def CREDITCARDISSUER():
    return fake.credit_card_provider()

def CREDITCARDNUMBER():
    return fake.credit_card_number()

def CURRENCY():
    return fake.currency_name()

def CURRENCYCODE():
    return fake.currency_code()

def CURRENCYNAME():
    return fake.currency_name()

def CURRENCYSYMBOL():
    return fake.currency_symbol()

def DATE():
    return fake.date_this_year()

def DOB():
    return fake.date_of_birth()

def EMAIL():
    return fake.email()

def ETHEREUMADDRESS():
    ethereum_address = '0x' + fake.sha256(raw_output=False)[:40]  # Generate a random SHA256 hash and use first 40 characters
    return ethereum_address

def EYECOLOR():
    return fake.color_name()

def FIRSTNAME():
    return fake.first_name()

def GENDER():
    return fake.random_element(elements=('Male', 'Female', 'Other'))

def HEIGHT():
    return fake.random_int(min=150, max=200)

def IBAN():
    return fake.iban()

def IP():
    return fake.ipv4()

def IPV4():
    return fake.ipv4()

def IPV6():
    return fake.ipv6()

def JOBAREA():
    return fake.job()

def JOBTITLE():
    return fake.job()

def JOBTYPE():
    job_types = ["Full-time", "Part-time", "Contract", "Temporary", "Internship", "Freelance"]
    job_type = random.choice(job_types)
    return job_type

def LASTNAME():
    return fake.last_name()

def LITECOINADDRESS():
    Litecoin_address = fake.sha256(raw_output=False)[:26]  # Generate a random SHA256 hash and truncate to 34 characters
    return Litecoin_address

def MAC():
    return fake.mac_address()

def MASKEDNUMBER():
    return fake.credit_card_number(card_type=None)  # generates a masked credit card number

def MIDDLENAME():
    return fake.first_name()

def NEARBYGPSCOORDINATE():
    return fake.local_latlng(country_code="US", coords_only=True)

def ORDINALDIRECTION():
    directions = ["North", "East", "South", "West"]
    direction = random.choice(directions)
    return direction

def PASSWORD():
    return fake.password()

def PHONEIMEI():
    imei_number = fake.numerify(text='##############')  # 15 digits IMEI-like number
    return imei_number

def PHONENUMBER():
    return fake.phone_number()

def PIN():
    return fake.random_number(digits=4)

def PREFIX():
    return fake.prefix()

def SECONDARYADDRESS():
    return fake.secondary_address()

def SEX():
    return fake.random_element(elements=('Male', 'Female'))

def SSN():
    return fake.ssn()

def STATE():
    return fake.state()

def STREET():
    return fake.street_name()

def TIME():
    return fake.time()

def URL():
    return fake.url()

def USERAGENT():
    return fake.user_agent()

def USERNAME():
    return fake.user_name()

def VEHICLEVIN():
    return fake.hexify(text='^'*17)

def VEHICLEVRM():
    return fake.license_plate()

def ZIPCODE():
    return fake.zipcode()

def get_random_unisex_name():
    unisex_names = [
        "Avery", "Taylor", "Jordan", "Alex", "Riley", "Quinn", "Casey", "Jamie",
        "Morgan", "Skyler", "Dakota", "Cameron", "Jesse", "Devon", "Reese", "Finley",
        "Sawyer", "Peyton", "Kendall", "Rowan", "Parker", "Drew", "Bailey", "Emerson",
        "Sage", "Ellis", "Remy", "Charlie", "Harper", "Frankie", "Phoenix", "Rory",
        "Payton", "Jessie", "Alex", "Jordan", "Taylor", "Dakota", "Casey", "Jamie",
        "Skyler", "Morgan", "Reese", "Avery", "Finley", "Bailey", "Sage", "Rowan",
        "Emerson", "Parker", "Drew", "Harper", "Phoenix", "Sage", "Ellis", "Remy",
        "Charlie", "Rory", "Payton", "Cameron", "Jordan", "Avery", "Casey", "Reese",
        "Morgan", "Skyler", "Quinn", "Jamie", "Taylor", "Dakota", "Jessie", "Finley",
        "Bailey", "Sage", "Rowan", "Emerson", "Parker", "Drew", "Harper", "Phoenix",
        "Sage", "Ellis", "Remy", "Alex", "Charlie", "Rory", "Payton", "Cameron",
        "Jordan", "Avery", "Casey", "Reese", "Morgan", "Skyler", "Quinn", "Jamie",
        "Taylor", "Dakota", "Jessie", "Finley", "Bailey", "Sage", "Rowan", "Emerson",
        "Parker", "Drew", "Harper", "Phoenix", "Sage", "Ellis", "Remy", "Alex",
        "Charlie", "Rory", "Payton", "Cameron", "Jordan", "Avery", "Casey", "Reese"
    ]
    return random.choice(unisex_names)

# Example usage
print(get_random_unisex_name())

import random

def alter_random_digits(number_string):
    length = len(number_string)
    # Determine the starting point for the last third of the number
    start_index = 0
    
    # Convert the number string to a list for easier manipulation
    number_list = list(number_string)
    
    # Alter some random digits in the last third of the number
    for i in range(start_index, length):
        if number_list[i].isdigit():  # Only alter digit characters
            number_list[i] = str(random.randint(0, 9))
    
    # Convert the list back to a string and return
    return ''.join(number_list)

# Example usage
print(alter_random_digits("12345678901234567890"))


# # Example usage:
# print("Fake Account Number:", Accountnumber())
# print("Fake Age:", Age())
# print("Fake Amount:", Amount())
# print("Fake BIC:", Bic())
# print("Fake Bitcoin Address:", Bitcoinaddress())
# print("Fake Building Number:", Buildingnumber())
# print("Fake City:", City())
# print("Fake Company Name:", Companyname())
# print("Fake County:", County())
# print("Fake Credit Card CVV:", Creditcardcvv())
# print("Fake Credit Card Issuer:", Creditcardissuer())
# print("Fake Credit Card Number:", Creditcardnumber())
# print("Fake Currency:", Currency())
# print("Fake Currency Code:", Currencycode())
# print("Fake Currency Name:", Currencyname())
# print("Fake Currency Symbol:", Currencysymbol())
# print("Fake Date:", Date())
# print("Fake Date of Birth:", Dob())
# print("Fake Email:", Email())
# print("Fake Ethereum Address:", Ethereumaddress())
# print("Fake Eye Color:", Eyecolor())
# print("Fake First Name:", Firstname())
# print("Fake Gender:", Gender())
# print("Fake Height:", Height())
# print("Fake IBAN:", Iban())
# print("Fake IP Address:", Ip())
# print("Fake IPv4 Address:", Ipv4())
# print("Fake IPv6 Address:", Ipv6())
# print("Fake Job Area:", Jobarea())
# print("Fake Job Title:", Jobtitle())
# print("Fake Job Type:", Jobtype())
# print("Fake Last Name:", Lastname())
# print("Fake Litecoin Address:", Litecoinaddress())
# print("Fake MAC Address:", Mac())
# print("Fake Masked Credit Card Number:", Maskednumber())
# print("Fake Middle Name:", Middlename())
# print("Fake Nearby GPS Coordinate:", Nearbygpscoordinate())
# print("Fake Ordinal Direction:", Ordinaldirection())
# print("Fake Password:", Password())
# print("Fake Phone IMEI:", Phoneimei())
# print("Fake Phone Number:", Phonenumber())
# print("Fake PIN:", Pin())
# print("Fake Prefix:", Prefix())
# print("Fake Secondary Address:", Secondaryaddress())
# print("Fake Sex:", Sex())
# print("Fake SSN:", Ssn())
# print("Fake State:", State())
# print("Fake Street:", Street())
# print("Fake Time:", Time())
# print("Fake URL:", Url())
# print("Fake User Agent:", Useragent())
# print("Fake Username:", Username())
# print("Fake Vehicle VIN:", Vehiclevin())
# print("Fake Vehicle VRM:", Vehiclevrm())
# print("Fake Zip Code:", Zipcode())
