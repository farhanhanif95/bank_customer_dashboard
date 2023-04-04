import random
import string
import datetime

# Generate random names using string library
def generate_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(7))

# Generate random email
def generate_email():
    email_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    return generate_name() + "@" + random.choice(email_domains)

# Generate random gender
def generate_gender():
    return random.choice(["Male", "Female"])

# Generate random age between 18 and 65
def generate_age():
    return random.randint(18, 65)

# Generate random number of months as a customer
def generate_months_as_customer(join_date, leave_date=None):
    if leave_date is None:
        return (datetime.date.today() - join_date).days // 30
    else:
        return (leave_date - join_date).days // 30

# Generate random join date between 2015 and 2022
def generate_join_date():
    start_date = datetime.date(2015, 1, 1)
    end_date = datetime.date(2022, 1, 1)
    days_between = (end_date - start_date).days
    random_number_of_days = random.randrange(days_between)
    return start_date + datetime.timedelta(days=random_number_of_days)

# Generate random leave date between join date and current date
def generate_leave_date(join_date):
    if random.random() <= 0.3:
        return None
    else:
        current_date = datetime.date.today()
        days_between = (current_date - join_date).days
        random_number_of_days = random.randrange(days_between)
        return join_date + datetime.timedelta(days=random_number_of_days)

# Generate 10000 random entries
data = []
for i in range(1, 10001):
    entry = {}
    entry['id'] = i
    entry['first_name'] = generate_name().capitalize()
    entry['last_name'] = generate_name().capitalize()
    entry['email'] = generate_email()
    entry['gender'] = generate_gender()
    entry['age'] = generate_age()
    entry['join_date'] = generate_join_date()
    entry['leave_date'] = generate_leave_date(entry['join_date'])
    entry['months_as_a_customer'] = generate_months_as_customer(entry['join_date'], entry['leave_date'])
    data.append(entry)

# Save data to CSV file
import csv
with open('user_data.csv', mode='w', newline='') as file:
    fieldnames = ['id', 'first_name', 'last_name', 'email', 'gender', 'age', 'months_as_a_customer', 'join_date', 'leave_date']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for entry in data:
        writer.writerow(entry)