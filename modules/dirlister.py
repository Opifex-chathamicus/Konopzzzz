import os

def run(**args):
    print("[*]In dirlister module.")
    files=os.listdir(".") #lists all files in current directory
    print(files)
    return str(files)

if __name__ == '__main__':
    run()
