import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def get_service():
    """
    This function send request to google sheets api
    """
    creds_json = "./Users/token.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


def get_stats_and_update_db(sheet_id, list_name):
    """
    This function parce spreadsheet and return data of sheet
    """
    SERVICE = get_service()
    SHEET = SERVICE.spreadsheets()
    SHEET_ID = sheet_id
    data = SHEET.values().batchGet(spreadsheetId=SHEET_ID, ranges=[list_name]).execute()
    return data

