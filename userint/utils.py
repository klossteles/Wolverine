

def save_file(request_file):
    file_name = 'signal-file.txt'
    with open(file_name, 'wb') as file:
        for chunk in request_file.chunks():
            file.write(chunk)

    return file_name
