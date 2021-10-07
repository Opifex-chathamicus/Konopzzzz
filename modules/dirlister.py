import os

def run(**args):
    print("[*]In dirlister modules.")
    files=os.listdir(".") #lists all files in current directory
    return str(files)

if __name__ == '__main__':
    run()
