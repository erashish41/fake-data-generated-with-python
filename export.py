import json
import csv
import openpyxl


def generate_json_file_from_the_fake_data(fake_data, file_name):
    # Write the fake generated data into the Json format
    with open(f"{file_name}.json", "w") as json_file:
        json.dump(fake_data, json_file, indent=4)
    print(">>>>>> Fake data stored in the json format >>>>>>>")
    return True


def generate_csv_file_from_the_fake_data(fake_data, file_name):
    # For header values
    fieldnames = fake_data[0].keys()

    # Write data to CSV file
    with open(f"{file_name}.csv", "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(fake_data)
    print(">>>>>> Fake data stored in the csv format >>>>>>>")
    return True


def generate_xls_file_from_the_fake_data(fake_data, file_name):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Fake Student Data"

    # Write the headers (keys of the dictionary)
    headers = list(fake_data[0].keys())
    sheet.append(headers)

    # Write the values (values of the dictionary)
    for data in fake_data:
        row = []
        for value in data.values():
            # If the value is a list, convert it to a string
            if isinstance(value, list):
                value = ", ".join(value)  # Convert list to a comma-separated string

            # If the value is a dictionary, convert it to a string
            if isinstance(value, dict):
                # Convert dictionary to a string by joining its key-value pairs
                value = ", ".join(f"{k}: {v}" for k, v in value.items())

            row.append(value)
        sheet.append(row)
    # Save the workbook to a file
    workbook.save(f"{file_name}.xlsx")
    print(">>>>>> Fake data stored in the Xlsx format >>>>>>>")
    return True
