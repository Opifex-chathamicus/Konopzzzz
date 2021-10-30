import os 

def run(**args):
    print("[*] In environment module.")
    print(str(os.environ))
    #retrieves any environment variables that are set on the remote machine.
    return str(os.environ) 
if __name__ == '__main__':
    run()
