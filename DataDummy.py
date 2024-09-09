### This project was created by Clifford (C.J.) Melton

import random
import datetime
import calendar
import pandas as pd
from names import get_first_name, get_last_name
from faker import Faker as fake

# Universal date
current_year = datetime.date.today().year

# Generate a fake phone number
def generate_random_phone_number():
  area_code = random.randint(200, 999)
  prefix = random.randint(200, 999)
  line_number = random.randint(1000, 9999)
  phone_number = f"{area_code}-{prefix}-{line_number}"
  return phone_number

# Generate a fake address
def generate_address():
  fake_street_address = fake().street_address()
  fake_city = fake().city()
  fake_state = fake().state()
  fake_zip = fake().zipcode()
  fake_address = f"{fake_street_address}, {fake_city}, {fake_state} {fake_zip}"
  return fake_address

# Generating the bank ownership probability
def generate_bankDob():
    value = random.randint(1,10)
    if value <= 2:
       numYears = random.randint(15,21)
    elif 3 <= value <= 7:
       numYears = random.randint(22,50)
    elif 6 <= value <= 9:
       numYears = random.randint(51,65)
    else:
       numYears = random.randint(66,92)

    birth_year = current_year - numYears
    
    birth_month = random.randint(1,12)

    if birth_month in (1,3,5,7,8,10,12):
       birth_month = random.randint(1,12)
       birth_day = random.randint(1,31)
    elif birth_month == 2:
       if calendar.isleap(birth_year):
          birth_day = random.randint(1,29)
       else:
          birth_day = random.randint(1,28)
    else:
       birth_day = random.randint(1,30)

    try: 
      birth_date = datetime.date(birth_year, birth_month, birth_day)
    except ValueError:
      last_day = calendar.monthrange(birth_year, birth_month)[1]
      birth_date = datetime.date(birth_year, birth_month, last_day) 

    return birth_date

# Formatting the data in the csv file
def create_banking_data(num_entries, account_number_length, account_types):
  data = []
  for _ in range(num_entries):
    account_number = f"{random.randint(10 ** (account_number_length - 1), 10**account_number_length - 1)}"
    first_name = get_first_name()
    last_name = get_last_name()
    ssn = fake().ssn()
    account_type = random.choice(account_types)
    address = generate_address()
    email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])}"
    phone = generate_random_phone_number()
    dob = generate_bankDob()

    age = current_year - dob.year

    age_ranges = [(15,22),(23,27),(28,40),(41,50),(51,60),(61,92)]
    balance_ranges = [(500,5000),(1100,10999),(5001,40000),(4999,200000),(30000,300000),(30000,450000)]

    for i, (low_age, high_age) in enumerate(age_ranges):
      if low_age <= age <= high_age:
        balance_low, balance_high = balance_ranges[i]
        balance = random.randint(balance_low, balance_high)
        break

    data.append({
      "Account Number": account_number,
      "First Name": first_name,
      "Last Name": last_name,
      "SSN": ssn,
      "Account Type": account_type,
      "Balance": balance,
      "Address": address,
      "Email": email,
      "Phone": phone,
      "Birthdate": dob,
    })

  df = pd.DataFrame(data)
  return df

# User inputs and controls
def main():
  while True:
   agreement = input("Do you understand the file being created contains synthetic, fictitious data and is not intended for real-world use?\nType 'Yes' or 'No': ")
   
   if agreement.lower() == "yes":
         file_name = input("Enter the desired CSV file name: ")
         num_entries = int(input("Enter the number of entries: "))
         account_number_length = int(input("Enter the desired length of the account numbers: "))
         account_types = input("Enter the available account types (comma-separated): ").split(",")
         df = create_banking_data(num_entries, account_number_length, account_types)
         df.to_csv(f"{file_name}.csv", index=False)  # Save to CSV without index column
         print(f"The financial data has been generated & saved in the {file_name}.csv file.")
         break
         
   elif agreement.lower() == "no":
      print("The file cannot be created for you until you agree that this file entails false information.")
      while True:
         choice = input("Type 'Previous' to or 'Exit' to leave the program.\n")
         if choice.lower() == "previous":
             break
         elif choice.lower() == "exit":
            print("Exiting the program...")
            exit()
         else:
            print("Invalid input. Please comply.")
   else:
      print("Invalid input. Please enter 'Yes' or 'No'.")

if __name__ == "__main__":
  main()