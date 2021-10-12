import sys

def run():
    version = sys.version
    ver_num = version.split(' ')
    print(str(ver_num[0]))
    return (str(ver_num[0]))

    
if __name__ == '__main__':
    run()