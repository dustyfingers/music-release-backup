import os.path
from zipfile import ZipFile

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]

# need to use absolute filepath for this to work when called from the cmd
BACKUP_FILEPATH = r'C:\Release Backups'
TOKEN_FILEPATH = r'.\token.json'

def main():
  """Insert new file.
  Returns : Id's of the file uploaded

  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  creds, _ = google.auth.default()

    # for each zip file in release backups, upload it to my google drive
  for file_name in os.listdir(BACKUP_FILEPATH):
        try:
            with ZipFile(file_name, 'r') as zip:
                zip.extractall()
                zip.close()
        except ZipFile.BadZipError:
            print('bad zip file!')

  try:
    # create drive api client
    service = build("drive", "v3", credentials=creds)

    file_metadata = {"name": "download.jpeg"}
    media = MediaFileUpload("download.jpeg", mimetype="image/jpeg")
    # pylint: disable=maybe-no-member
    file = (
        service.files()
        .create(body=file_metadata, media_body=media, fields="id")
        .execute()
    )
    print(f'File ID: {file.get("id")}')

  except HttpError as error:
    print(f"An error occurred: {error}")
    file = None

  return file.get("id")




if __name__ == "__main__":
  main()