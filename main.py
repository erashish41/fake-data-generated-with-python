from fake_generation_utils import (
    generate_fake_student_data,
    generate_fake_company_data,
    generate_fake_employee_data,
    generate_fake_product_data,
)
from export import (
    generate_csv_file_from_the_fake_data,
    generate_json_file_from_the_fake_data,
    generate_xls_file_from_the_fake_data,
)

# Calling function to generate fake data Student data for all formats
generate_csv_file_from_the_fake_data(generate_fake_student_data(), "student_data")
generate_json_file_from_the_fake_data(generate_fake_student_data(), "student_data")
generate_xls_file_from_the_fake_data(generate_fake_student_data(), "student_data")

# Calling function to generate fake data Company data for all formats
generate_csv_file_from_the_fake_data(generate_fake_company_data(), "company_data")
generate_json_file_from_the_fake_data(generate_fake_company_data(), "company_data")
generate_xls_file_from_the_fake_data(generate_fake_company_data(), "company_data")

# Calling function to generate fake data Employee data for all formats
generate_csv_file_from_the_fake_data(generate_fake_employee_data(), "employee_data")
generate_json_file_from_the_fake_data(generate_fake_employee_data(), "employee_data")
generate_xls_file_from_the_fake_data(generate_fake_employee_data(), "employee_data")

# Calling function to generate fake data Products data for all formats
generate_csv_file_from_the_fake_data(generate_fake_product_data(), "product_data")
generate_json_file_from_the_fake_data(generate_fake_product_data(), "product_data")
generate_xls_file_from_the_fake_data(generate_fake_product_data(), "product_data")
