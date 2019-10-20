from __future__ import print_function

import os.path
import pickle

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.pickle.

SCOPES = ['https://www.googleapis.com/auth/drive']


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    store = file.Storage('storage.json')
    creds = store.get()
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))
    FILES = DRIVE.files()
    GLOBAL_RESPONSE = []

    GLOBAL_RESPONSE += FILES.list(pageSize=1000, orderBy='folder, name', q="mimeType='application/pdf'", spaces='drive',
                                  fields='nextPageToken, files(name, mimeType, size)').execute().get('files', [])
    GLOBAL_RESPONSE += FILES.list(pageSize=1000, orderBy='folder, name', q="mimeType='application/vnd.ms-htmlhelp'", spaces='drive',
                                  fields='nextPageToken, files(name, mimeType, size)').execute().get('files', [])
    GLOBAL_RESPONSE += FILES.list(pageSize=1000, orderBy='folder, name', q="mimeType='application/epub+zip'", spaces='drive',
                                  fields='nextPageToken, files(name, mimeType, size)').execute().get('files', [])

    local_file = open('myBooks.csv', 'w+', encoding="utf-8")
    local_file.write("name, type, size\n")
    local_file.close()
    local_file = open('myBooks.csv', 'a', encoding="utf-8")

    for f in GLOBAL_RESPONSE:
        size = round(((int(f['size']) // 1024) / 1024), 2)
        formatted_name = f['name'].replace(',', '-')
        local_file.write("{}, {}, {} Mb\n".format(formatted_name, f['mimeType'], size))
    local_file.close()


if __name__ == '__main__':
    main()
