import random

from django.core.exceptions import ObjectDoesNotExist
from Users.models import User, Curator


def create_or_update_user(data):
    user_data = data[0]
    user_indexes = data[1]
    user_curator = data[2]

    for user in user_data[2:]:
        if len(user) > 25:
            try:
                conversion = int(user[user_indexes[1]])
            except ValueError:
                conversion = 0

            try:
                ltv = int(user[user_indexes[2]])
                if ltv < 0:
                    ltv = 0
            except ValueError:
                ltv = 0

            try:
                remaining = int(user[user_indexes[3]])
                if remaining < 0:
                    remaining = 0
            except ValueError:
                remaining = 0

            try:
                user_object = User.objects.get(name=user[user_indexes[0]])
                user_object.conversion = conversion
                user_object.ltv = ltv
                user_object.remaining = remaining
                user_object.curator = Curator.objects.get(username=user_curator)
                user_object.save()
            except ObjectDoesNotExist:
                name = user[user_indexes[0]]
                user = User.objects.create(
                    name=name,
                    conversion=conversion,
                    ltv=ltv,
                    remaining=remaining,
                    password=random.randint(1000, 9999),
                    curator=Curator.objects.get(username=user_curator)
                )
                user.save()

            except IndexError:
                print('Error')
