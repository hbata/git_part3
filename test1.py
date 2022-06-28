import os

def get_filename(filename):
    return "Hello from: {}".format(filename)

filename = os.path.basename(__file__)
print(get_filename(filename))
