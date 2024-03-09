import os
import requests
import zipfile

def compress_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(folder_path, '..')))

folder_to_compress = "to-be-uploaded"
compressed_zip = "compressed.zip"

# Compress the folder
compress_folder(folder_to_compress, compressed_zip)

url = "https://plantimage.p.rapidapi.com/"

# Read the zip file as binary data
with open(compressed_zip, 'rb') as file:
    zip_data = file.read()

payload = {
    "uploaded": "true",
    "key2": "value"
}

headers = {
    "X-RapidAPI-Key": "b7ad4d30e0msh5d309142ea426d5p194cd7jsn126b4dbb65ab",
    "X-RapidAPI-Host": "plantimage.p.rapidapi.com",
    # Use appropriate content type for binary data
    "Content-Type": "application/zip"
}

try:
    response = requests.post(url, data=zip_data, headers=headers, params=payload)

    # Check if the request was successful (status code 2xx)
    if response.status_code == requests.codes.ok:
        print("Upload successful.")
    else:
        # If request was not successful, print error message
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    # Handle network or request-related errors
    print("Error:", e)
