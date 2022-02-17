import Users
from TeamStatGoogleApi.celery import app
from Users.models import User
from get_data import get_stats_and_update_db


@app.task
def get_stats_from_sheets():
    """
    This task get data from spreadsheet and update values in database of users
    """
    data = get_stats_and_update_db()
    result_list = []
    for i in data.get('valueRanges'):
        for sheet_line in i.get('values'):
            if len(sheet_line) > 24:
                user_data = [sheet_line[1], sheet_line[24], sheet_line[15], sheet_line[25]]
                result_list.append(user_data)

    for user_data in result_list:
        try:
            user = User.objects.get(name=user_data[0])
            user.conversion = user_data[1]
            user.ltv = user_data[2]
            user.remaining = int(user_data[3]) if int(user_data[3]) > 0 else 0
            user.save()
        except Users.models.User.DoesNotExist:
            print('User not exist')

