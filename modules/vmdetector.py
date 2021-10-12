import sys

#https://docs.python.org/3/library/sys.html

def run():
    print("[+] In vmdetector module.")

    if hasattr(sys, 'real_prefix'):
        return "Virtual Machine: True"
    else:
        return "Virtual Machine: False"

if __name__ == '__main__':
    run()