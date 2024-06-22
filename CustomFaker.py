import string
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

def generate_fake_alphabets(length):
    fake_alphabets = "ABCDXYMNOPQRjghuvwxz"
    result = ''.join(random.choice(fake_alphabets) for _ in range(length))
    return result

def generate_fake_alphanumeric(length):
    fake_alphanumeric = "1B2C4D5X8Y9M0N3O7P6QRTWSZj6huv7w8x9z"
    result = ''.join(random.choice(fake_alphanumeric) for _ in range(length))
    return result

def generate_fake_numeric(length):
    fake_numeric = "0123456789"
    result = ''.join(random.choice(fake_numeric) for _ in range(length))
    return result

###### Presidio Entity types #######

def CREDIT_CARD():
    return fake.credit_card_number()

def CRYPTO():
    presidio_bitcoin_address = fake.sha256(raw_output=False)[:34]  # Generate a random SHA256 hash and truncate to 34 characters
    return presidio_bitcoin_address

def DATE_TIME():
    return fake.date_time()

def EMAIL_ADDRESS():
    return fake.email()

def IBAN_CODE():
    return fake.iban()

def IP_ADDRESS():
    return fake.ipv4()

def NRP():
    components = ['Nationality', 'Religion', 'Political Group']
    chosen_component = random.choice(components)

    if chosen_component == 'Nationality':
        nationalities = ['American', 'British', 'French', 'German', 'Japanese', 'Chinese', 'Indian', 'Russian']
        return f"Nationality: {random.choice(nationalities)}"
    elif chosen_component == 'Religion':
        religions = ['Christian', 'Muslim', 'Buddhist', 'Hindu', 'Jewish', 'Atheist']
        return f"Religion: {random.choice(religions)}"
    elif chosen_component == 'Political Group':
        political_groups = ['Liberal', 'Conservative', 'Socialist', 'Green Party', 'Republican', 'Democrat']
        return f"Political Group: {random.choice(political_groups)}"


def LOCATION():
    return fake.city()

def PERSON():
    return get_random_unisex_name()

def PHONE_NUMBER():
    return fake.phone_number()

def MEDICAL_LICENSE():
    return fake.license_plate()

def URL():
    return fake.url()

def US_BANK_NUMBER():
    return fake.bban()

def US_DRIVER_LICENSE():
    return fake.license_plate()

def US_ITIN():
    first_digit = "9"
    second_to_fourth_digits = str(random.randint(100, 999))  # Random three-digit number
    fourth_digit = random.choice(['7', '8'])
    remaining_digits = str(random.randint(1000, 9999))  # Random four-digit number

    us_itin = f"{first_digit}{second_to_fourth_digits}{fourth_digit}{remaining_digits}"
    return us_itin

def US_PASSPORT():
    passport_number = ''.join(random.choices('0123456789', k=9))
    return passport_number

def US_SSN():
    return fake.ssn()

def UK_NHS():
    nhs_number = ''.join(random.choices('0123456789', k=10))
    return nhs_number

def ES_NIF():
    numbers = ''.join(random.choices('0123456789', k=8))
    verification_letters = 'TRWAGMYFPDXBNJZSQVHLCKE'
    verification_letter = random.choice(verification_letters)
    return f"{numbers}{verification_letter}"

def IT_FISCAL_CODE():
    letters = string.ascii_uppercase
    numbers = string.digits
    return ''.join(random.choices(letters, k=6)) + ''.join(random.choices(numbers, k=2)) + \
           ''.join(random.choices(letters, k=1)) + ''.join(random.choices(numbers, k=2)) + \
           ''.join(random.choices(letters, k=4))

def IT_DRIVER_LICENSE():
    letters = string.ascii_uppercase
    numbers = string.digits
    return ''.join(random.choices(letters, k=2)) + ''.join(random.choices(numbers, k=7))

def IT_VAT_CODE():
    return 'IT' + ''.join(random.choices(string.digits, k=11))

def IT_PASSPORT():
    letters = string.ascii_uppercase
    numbers = string.digits
    return ''.join(random.choices(letters, k=2)) + ''.join(random.choices(numbers, k=6))

def IT_IDENTITY_CARD():
    letters = string.ascii_uppercase
    numbers = string.digits
    return ''.join(random.choices(letters, k=2)) + ''.join(random.choices(numbers, k=7))

def PL_PESEL():
    first_10_digits = [random.randint(0, 9) for _ in range(10)]

    # Calculate the checksum (last digit)
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = sum(digit * weight for digit, weight in zip(first_10_digits, weights)) % 10
    if checksum != 0:
        checksum = 10 - checksum

    # Construct the PESEL number
    pesel_number = ''.join(map(str, first_10_digits)) + str(checksum)

    return pesel_number

def SG_NRIC_FIN():
    first_char = random.choice('STFG')
    second_digit = random.randint(0, 9)
    third_to_eighth_digits = ''.join(random.choices('0123456789', k=7))
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_char = random.choice(alphabet)
    
    return f"{first_char}{second_digit}{third_to_eighth_digits}{last_char}"


def SG_UEN():
    entity_type = random.choice(['S', 'T', 'R', 'U'])
    digits = ''.join(random.choices('0123456789', k=8))
    return f"{entity_type}{digits}"

def AU_ABN():
    abn = ''.join(random.choices('0123456789', k=10))  # First 10 digits
    return '0' + abn

def AU_ACN():
    acn = ''.join(random.choices('0123456789', k=8))  # First 8 digits
    return '0' + acn

def AU_TFN():
    tfn = ''.join(random.choices('0123456789', k=8))  # First 8 digits
    return tfn

def AU_MEDICARE():
    medicare = ''.join(random.choices('0123456789', k=10))  # First 10 digits
    return medicare

def IN_PAN():
    # First 5 characters (uppercase letters)
    first_five = ''.join(random.choices(string.ascii_uppercase, k=5))
    
    # Next 4 characters (digits)
    next_four = ''.join(random.choices(string.digits, k=4))
    
    # Last character (uppercase letter)
    last_char = random.choice(string.ascii_uppercase)
    
    # Combine parts to form PAN
    pan = f"{first_five}{next_four}{last_char}"
    
    return pan

def IN_AADHAAR():
    aadhaar = ''.join(random.choices('0123456789', k=12))  # 12 digits
    return aadhaar

def IN_VEHICLE_REGISTRATION():
    state_code = random.choice(['AP', 'AR', 'AS', 'BR', 'CG', 'GA', 'GJ', 'HR', 'HP', 'JH', 
                                'KA', 'KL', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OD', 'PB', 
                                'RJ', 'SK', 'TN', 'TS', 'TR', 'UK', 'UP', 'WB'])
    district_code = ''.join(random.choices(string.ascii_uppercase, k=2))
    registration_number = ''.join(random.choices(string.digits, k=4))
    
    return f"{state_code}{district_code}{registration_number}"



def print_method_result(method_name, result):
    print(f"{method_name}: {result}")


# print_method_result("CREDIT_CARD", CREDIT_CARD())
# print_method_result("CRYPTO", CRYPTO())
# print_method_result("DATE_TIME", DATE_TIME())
# print_method_result("EMAIL_ADDRESS", EMAIL_ADDRESS())
# print_method_result("IBAN_CODE", IBAN_CODE())
# print_method_result("IP_ADDRESS", IP_ADDRESS())
# print_method_result("NRP", NRP())
# print_method_result("LOCATION", LOCATION())
# print_method_result("PERSON", PERSON())
# print_method_result("PHONE_NUMBER", PHONE_NUMBER())
# print_method_result("MEDICAL_LICENSE", MEDICAL_LICENSE())
# print_method_result("URL", URL())
# print_method_result("US_BANK_NUMBER", US_BANK_NUMBER())
# print_method_result("US_DRIVER_LICENSE", US_DRIVER_LICENSE())
# print_method_result("US_ITIN", US_ITIN())
# print_method_result("US_PASSPORT", US_PASSPORT())
# print_method_result("US_SSN", US_SSN())
# print_method_result("UK_NHS", UK_NHS())
# print_method_result("ES_NIF", ES_NIF())
# print_method_result("IT_FISCAL_CODE", IT_FISCAL_CODE())
# print_method_result("IT_DRIVER_LICENSE", IT_DRIVER_LICENSE())
# print_method_result("IT_VAT_CODE", IT_VAT_CODE())
# print_method_result("IT_PASSPORT", IT_PASSPORT())
# print_method_result("IT_IDENTITY_CARD", IT_IDENTITY_CARD())
# print_method_result("PL_PESEL", PL_PESEL())
# print_method_result("SG_NRIC_FIN", SG_NRIC_FIN())
# print_method_result("SG_UEN", SG_UEN())
# print_method_result("AU_ABN", AU_ABN())
# print_method_result("AU_ACN", AU_ACN())
# print_method_result("AU_TFN", AU_TFN())
# print_method_result("AU_MEDICARE", AU_MEDICARE())
# print_method_result("IN_PAN", IN_PAN())
# print_method_result("IN_AADHAAR", IN_AADHAAR())
# print_method_result("IN_VEHICLE_REGISTRATION", IN_VEHICLE_REGISTRATION())