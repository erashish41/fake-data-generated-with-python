import random

# import Faker from the faker module
from faker import Faker

# initialize the faker instance
fake = Faker()


def generate_fake_student_data(data_set_len=1000):
    """
    This function generate the fake data for the 1000 students, its optional param,
    If you wanna generate more or less data just add you value as int as an argument by default its 1000
    """
    # Here we created the empty list to store fake student data in the dict format
    fake_student_data = []
    # Here I used the range to iterate data for the 1000 times
    for i in range(data_set_len):
        # Here i used the fake module for getting all the data
        # Bellow used attributes are supported by the fake class instance
        # If you wanted to see these you can simple print(dir(fake))
        # or you can follow the document https://faker.readthedocs.io/en/master/
        fake_student_data.append(
            {
                "name": fake.name(),
                "email": fake.email(),
                "date_of_birth": fake.date_of_birth(
                    minimum_age=18, maximum_age=22
                ).isoformat(),
                "address": fake.address(),
                "phone_number": fake.phone_number(),
                "grade": fake.random_element(elements=("A", "B", "C", "D", "F")),
                "student_id": fake.uuid4(),
                "major": fake.random_element(
                    elements=(
                        "Computer Science",
                        "Engineering",
                        "Mathematics",
                        "Physics",
                        "Biology",
                        "History",
                        "Chemistry",
                    )
                ),
                "minor": fake.random_element(
                    elements=(
                        "Economics",
                        "Psychology",
                        "Philosophy",
                        "Art History",
                        "Sociology",
                        "Music",
                    )
                ),
                "enrollment_year": fake.year(),
                "graduation_year": fake.year(),
                "gender": fake.random_element(
                    elements=("Male", "Female", "Non-binary")
                ),
                "gpa": round(
                    fake.random_number(digits=2) / 10 + 2.0, 2
                ),  # Random GPA between 2.0 and 4.0
                "ethnicity": fake.random_element(
                    elements=(
                        "Caucasian",
                        "Hispanic",
                        "Asian",
                        "African American",
                        "Mixed",
                        "Other",
                    )
                ),
                "marital_status": fake.random_element(
                    elements=("Single", "Married", "Divorced")
                ),
                "courses": [
                    fake.bs() for _ in range(3)
                ],  # Fake courses like "Intro to Algorithms", "Data Structures"
                "student_type": fake.random_element(
                    elements=("Full-time", "Part-time")
                ),
                "scholarship": fake.random_element(elements=("Yes", "No")),
                "sports_teams": fake.random_element(
                    elements=("Basketball", "Football", "Soccer", "None")
                ),
                "internship_status": fake.random_element(
                    elements=("None", "Currently Internship", "Completed Internship")
                ),
                "social_security_number": fake.ssn(),
                "birth_place": fake.city(),
                "nationality": fake.random_element(
                    elements=("American", "Canadian", "British", "German", "Australian")
                ),
                "parents": {
                    "father_name": fake.name(),
                    "mother_name": fake.name(),
                    "contact_number": fake.phone_number(),
                },
                "emergency_contact": {
                    "name": fake.name(),
                    "relationship": fake.random_element(
                        elements=("Parent", "Sibling", "Friend", "Other")
                    ),
                    "phone_number": fake.phone_number(),
                },
                "language_proficiency": fake.random_element(
                    elements=(
                        "English",
                        "Spanish",
                        "Mandarin",
                        "French",
                        "German",
                        "Other",
                    )
                ),
                "previous_schools": [
                    fake.company() for _ in range(2)
                ],  # Fake names for previous schools
                "has_student_loan": fake.random_element(elements=("Yes", "No")),
            }
        )

    return fake_student_data


def generate_fake_employee_data(data_set_len=1000):
    """Generates fake employee data."""
    fake = Faker()
    fake_employee_data = []

    for _ in range(data_set_len):
        fake_employee_data.append(
            {
                "name": fake.name(),
                "email": fake.email(),
                "phone_number": fake.phone_number(),
                "employee_id": fake.uuid4(),
                "position": fake.job(),
                "department": fake.random_element(
                    elements=["HR", "Engineering", "Sales", "Marketing", "Finance"]
                ),
                "salary": round(random.uniform(40000, 120000), 2),
                "hire_date": fake.date_between(
                    start_date="-10y", end_date="today"
                ).isoformat(),
                "employment_type": fake.random_element(
                    elements=["Full-time", "Part-time", "Contract"]
                ),
                "address": fake.address(),
                "manager": fake.name(),
                "performance_rating": round(random.uniform(1.0, 5.0), 1),
                "skills": [fake.word() for _ in range(5)],
                "office_location": fake.city(),
                "has_parking_pass": fake.random_element(elements=["Yes", "No"]),
            }
        )

    return fake_employee_data


def generate_fake_company_data(data_set_len=100):
    """Generates fake company data."""
    fake = Faker()
    fake_company_data = []

    for _ in range(data_set_len):
        fake_company_data.append(
            {
                "company_name": fake.company(),
                "industry": fake.random_element(
                    elements=["Tech", "Finance", "Healthcare", "Retail", "Education"]
                ),
                "founded_year": fake.year(),
                "ceo": fake.name(),
                "headquarters": fake.city(),
                "num_employees": random.randint(50, 10000),
                "revenue": round(random.uniform(1_000_000, 10_000_000_000), 2),
                "website": fake.url(),
                "stock_symbol": fake.random_element(
                    elements=["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
                ),
                "customer_satisfaction": round(random.uniform(1.0, 5.0), 1),
                "publicly_traded": fake.random_element(elements=["Yes", "No"]),
            }
        )

    return fake_company_data


def generate_fake_product_data(data_set_len=500):
    """Generates fake product data."""
    fake = Faker()
    fake_product_data = []

    for _ in range(data_set_len):
        fake_product_data.append(
            {
                "product_name": fake.word().capitalize()
                + " "
                + fake.word().capitalize(),
                "category": fake.random_element(
                    elements=[
                        "Electronics",
                        "Clothing",
                        "Home & Kitchen",
                        "Beauty",
                        "Sports",
                    ]
                ),
                "price": round(random.uniform(10, 1000), 2),
                "sku": fake.uuid4(),
                "stock_quantity": random.randint(0, 5000),
                "release_date": fake.date_between(
                    start_date="-5y", end_date="today"
                ).isoformat(),
                "manufacturer": fake.company(),
                "warranty_period": fake.random_element(
                    elements=["6 months", "1 year", "2 years", "3 years"]
                ),
                "rating": round(random.uniform(1.0, 5.0), 1),
                "is_available": fake.random_element(elements=["Yes", "No"]),
            }
        )

    return fake_product_data
