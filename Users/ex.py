import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

CRED_API_KEY = 'a0826dae9898b000f71865369e16bc0512888997'
names = []
convers = []
ltv = []


def get_service_simple():
    return build('sheets', 'v4', developerKey=CRED_API_KEY)


def get_service_sacc():
    creds_json = "token.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


def data():
    global names
    global convers
    global ltv
    service = get_service_sacc()
    sheet = service.spreadsheets()
    sheet_id = "1z26JBWnqn45dauJMag8ictuxr4wH813VUmADP1QfDCE"

    resp = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=['TEAM']).execute()

    for i in resp.get('valueRanges'):
        for x in i.get('values'):
            names.append(x[1])
            convers.append(x[14])
            ltv.append(x[15])

