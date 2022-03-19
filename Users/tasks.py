import random

import Users
from TeamStatGoogleApi.celery import app
from Users.models import User
from get_data import get_stats_and_update_db


@app.task
def get_stats_from_sheet_2():
    """
    This task get data from spreadsheet and update values in database of users
    """
    data = get_stats_and_update_db('1EUnDwGqfIa_j3RXWzqywe_rbmUJMyA6_QhN8iYv5ZPg', 'Stats')

    result_list = []

    name_index = 0
    conversion_index = 0
    ltv_index = 0
    remaining_index = 0

    for i in data.get('valueRanges'):
        first = i.get('values')[1]
        name_index = first.index('Имя')
        conversion_index = first.index('Live conversion')
        ltv_index = first.index('LTV')
        remaining_index = first.index('Remaining')

        for x in data.get('valueRanges'):
            print(x)
            for sheet_line in x.get('values')[1:]:
                print(sheet_line)
                if len(sheet_line) > 20:
                    user_data = [
                        sheet_line[name_index],
                        sheet_line[conversion_index],
                        sheet_line[ltv_index],
                        sheet_line[remaining_index]
                    ]
                    result_list.append(user_data)


        for user_data in result_list:
            print(123)
            try:
                user_data[3] = int(user_data[3])
            except ValueError:
                user_data[3] = 0

            try:
                user = User.objects.get(name=user_data[0])
                user.conversion = user_data[1]
                user.ltv = user_data[2]
                user.remaining = user_data[3] if user_data[3] > 0 else 0
                user.save()
            except Users.models.User.DoesNotExist:
                user = User.objects.create(
                    name=user_data[0],
                    conversion=user_data[1],
                    ltv=user_data[2],
                    password=random.randint(1000, 9999)
                )
                user.save()
            except IndexError:
                print('Error index')


@app.task
def get_stats_from_sheet_1():
    """
    This task get data from spreadsheet and update values in database of users
    """
    data = get_stats_and_update_db('1z26JBWnqn45dauJMag8ictuxr4wH813VUmADP1QfDCE', 'TEAM')

    result_list = []

    name_index = 0
    conversion_index = 0
    ltv_index = 0
    remaining_index = 0

    for i in data.get('valueRanges'):
        first = i.get('values')[0]
        name_index = first.index('Teacher')
        conversion_index = first.index('Live conversion')
        ltv_index = first.index('LTV')
        remaining_index = first.index('Remaining')

        for x in data.get('valueRanges'):
            for sheet_line in x.get('values')[1:]:
                if len(sheet_line) > 20:
                    user_data = [
                        sheet_line[name_index],
                        sheet_line[conversion_index],
                        sheet_line[ltv_index],
                        sheet_line[remaining_index]
                    ]
                    result_list.append(user_data)

        for user_data in result_list:
            try:
                user_data[3] = int(user_data[3])
            except ValueError:
                user_data[3] = 0

            try:
                user = User.objects.get(name=user_data[0])
                user.conversion = user_data[1]
                user.ltv = user_data[2]
                user.remaining = user_data[3] if user_data[3] > 0 else 0
                user.save()
            except Users.models.User.DoesNotExist:
                user = User.objects.create(
                    name=user_data[0],
                    conversion=user_data[1],
                    ltv=user_data[2],
                    password=random.randint(1000, 9999)
                )
                user.save()
            except IndexError:
                print('Error index')
