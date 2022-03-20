from TeamStatGoogleApi.celery import app
from get_data import get_stats_and_update_db


@app.task
def get_stats_from_sheet_2():
    """
    This task get data from spreadsheet and update values in database of users
    """
    data = get_stats_and_update_db('1EUnDwGqfIa_j3RXWzqywe_rbmUJMyA6_QhN8iYv5ZPg', 'Stats')

    value_ranges = data.get('valueRanges')[0]
    data_list = value_ranges.get('values')[1]
    data_lists = value_ranges.get('values')

    user_list_index = [
        data_list.index('Имя'),
        data_list.index('Live conversion'),
        data_list.index('LTV'),
        data_list.index('Remaining')
    ]

    return [data_lists, user_list_index, 'Irina']


@app.task
def get_stats_from_sheet_1():
    """
    This task get data from spreadsheet and update values in database of users
    """
    data = get_stats_and_update_db('1z26JBWnqn45dauJMag8ictuxr4wH813VUmADP1QfDCE', 'TEAM')

    value_ranges = data.get('valueRanges')[0]
    data_list = value_ranges.get('values')[0]
    data_lists = value_ranges.get('values')

    user_list_index = [
        data_list.index('Teacher'),
        data_list.index('Live conversion'),
        data_list.index('LTV'),
        data_list.index('Remaining')
    ]

    return [data_lists, user_list_index, 'Nikolay']
