from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive']

def authenticate_google_docs_and_drive():
    """Shows basic usage of the Docs and Drive API."""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def copy_and_share_google_doc(source_doc_id, target_email):
    creds = authenticate_google_docs_and_drive()
    drive_service = build('drive', 'v3', credentials=creds)

    # Copy the Google Doc
    copied_doc = drive_service.files().copy(fileId=source_doc_id, body={'name': 'Copy of document'}).execute()
    new_doc_id = copied_doc.get('id')

    # Share the copied doc with the target email
    drive_service.permissions().create(
        fileId=new_doc_id,
        body={
            'type': 'user',
            'role': 'writer',
            'emailAddress': target_email
        },
        fields='id'
    ).execute()

    print(f"Document copied and shared with {target_email}. New document ID: {new_doc_id}")

# Example usage
source_doc_id = 'YOUR_SOURCE_DOCUMENT_ID_HERE'  # Replace with your source document ID
target_email = 'EMAIL' # Replace with your email
copy_and_share_google_doc(source_doc_id, target_email)
