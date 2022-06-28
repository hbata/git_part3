import os

def get_files(curr_dir):
    result = [f for f in os.listdir(curr_dir) if os.path.isfile(os.path.join(curr_dir,f))]
    return result

if __name__ == "__main__":
    curr_dir = os.getcwd()
    print(get_files(curr_dir))
