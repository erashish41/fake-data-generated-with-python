import os
from zipfile import ZipFile

total_files = os.listdir()

def get_by_file_name(file_name, extension_type):
    result_file_name = []

    for file in file_name:
        # print(file)
        # print(file_name)
        complete_name, extension = file.split('.')
        # print(">>>>>.1>>>>>>>", complete_file)
        # print(">>>>>2>>>>>>>", extension)
        if extension == extension_type:
            result_file_name.append(file)
    return result_file_name

final_result = get_by_file_name(total_files, 'json')
# print(final_result)

# to zip
def zip_file(file_name):
    with ZipFile("all_json_zip_files.zip", "w") as zip_object:
        for file in file_name:
            zip_object.write(file)
zip_file(final_result)

# to unzip
def unzip_zipped_file(file_name):
    if file_name not in os.listdir():
        raise ValueError("File not found, please check your code")

    with ZipFile(file_name, "r") as unzip_object:
        unzip_object.extractall("unzipped_files")
unzip_zipped_file("all_json_zip_files.zip")