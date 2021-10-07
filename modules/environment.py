import os 

def run(**args):
    print("[*] In environment module.")
    print(str(os.environ))
    return str(os.environ) #retrieves any environment variables that are set on the remote machine.
if __name__ == '__main__':
    run()
