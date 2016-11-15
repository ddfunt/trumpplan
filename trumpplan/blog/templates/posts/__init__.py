import os

basepath = os.path.dirname(os.path.realpath(__file__))

def get_post(id):
    id = id.replace(' ', '_')
    for file in os.listdir(os.path.dirname(os.path.realpath(__file__))):
        if file.endswith('.html') and id in file:
            print(basepath)
            with open(os.path.join(basepath,file), 'r') as f:
                text = f.read()
                return os.path.join(basepath,file)
        else:
            return None
