import os
import time

from wolverine import settings


def save_file(user_name, request_file):
    file_name = os.path.join(userpath(user_name), 'signal_input_{}.txt'.format(time.time()))

    with open(file_name, 'wb') as file:
        for chunk in request_file.chunks():
            file.write(chunk)

    return file_name


def userpath(user_name):
    user_path = os.path.join(settings.USERFILES_PATH, user_name)

    if not os.path.exists(user_path):
        os.makedirs(user_path)

    return user_path
