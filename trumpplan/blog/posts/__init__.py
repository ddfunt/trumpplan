import os


def get_post(id):
    for file in os.listdir(os.path.dirname(__file__)):
        if file.endswith('.html') and id in file:
            with open(file, 'r') as f:
                text = f.read()
                return text
        else:
            return None
