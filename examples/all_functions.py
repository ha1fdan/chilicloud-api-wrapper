from chilicloud import *

updateApiToken() # Gets a new X-Apigw-Session token for interacting with the API
file_uuid = uploadFile('test_file.txt') # Uploads out test_file.txt to the server
downloadFile(file_uuid, 'downloaded_file.txt') # Retrieves the uploaded file
deleteFile(file_uuid) # Deletes the uploaded file