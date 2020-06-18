import requests
import sys
from concurrent.futures import ThreadPoolExecutor
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from datetime import datetime
import threading

startTime = datetime.now()
if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("""


 ######           ######                                                    
 #     # # #####  #     # #  ####   ####   ####  #    # ###### #####  #   # 
 #     # # #    # #     # # #      #    # #    # #    # #      #    #  # #  
 #     # # #    # #     # #  ####  #      #    # #    # #####  #    #   #   
 #     # # #####  #     # #      # #      #    # #    # #      #####    #   
 #     # # #   #  #     # # #    # #    # #    #  #  #  #      #   #    #   
 ######  # #    # ######  #  ####   ####   ####    ##   ###### #    #   #
    
 
 HTTPS directory searcher                               Coded by TORSh4rk

""")
    print("""[+] Exemple for usage: python3 DirDiscovery.py https://www.nasa.gov/ wordlist.txt\n
                                        OR\n
[+] Exemple for usage: python3 DirDiscovery.py https://www.nasa.gov/ wordlist.txt .php (Any file extension)
    """)
    sys.exit()

else:
    pass

def brute(url, wordlist):
    with open(wordlist) as list:
       while True:
            directory = list.readline().strip("\n")
            path = url + directory
            req = requests.get(path, verify=False)
            print(path, req.status_code)
            if req.status_code == 200:
                 print("Directory Found: {} ===> Code Respose: {}".format(path, req.status_code))
            elif req.status_code == 301:
                 print("Directory Found: {} ===> Code Respose: {}".format(path, req.status_code))
            elif req.status_code == 302:
                 print("Directory Found: {} ===> Code Respose: {}".format(path, req.status_code))
            elif req.status_code == 400:
                 print("Interesting: {} ===> Code Respose: {}".format(path, req.status_code))
            elif req.status_code == 401:
                 print("Unauthorized Directory: {} ===> Code Respose: {}".format(path, req.status_code))
            else:
               pass 
            if not directory:
                break

def extbrute(url, dicionary, ext):
    with open(dicionary) as list:
       while True:
            directory = list.readline().strip("\n")
            extpath = url + directory + ext
            req = requests.get(extpath, verify=False)
            print(extpath, req.status_code)
            if req.status_code == 200:
                 print("File Found: {} ===> Code Respose: {}".format(extpath, req.status_code))
            elif req.status_code == 301:
                 print("File Found: {} ===> Code Respose: {}".format(extpath, req.status_code))
            elif req.status_code == 302:
                 print("File Found: {} ===> Code Respose: {}".format(extpath, req.status_code))
            elif req.status_code == 400:
                 print("Interesting File: {} ===> Code Respose: {}".format(extpath, req.status_code))
            elif req.status_code == 401:
                 print("Unauthorized File: {} ===> Code Respose: {}".format(extpath, req.status_code))
            else:
               pass 
            if not directory:
                break

threads = []

for i in range(len(sys.argv[2])):
    threading.Thread(target=brute)
    threads.append(i)

def main():

    if len(sys.argv) == 3:
        with ThreadPoolExecutor() as executor:
            executor.map(brute(sys.argv[1], sys.argv[2]),timeout=10)
    if len(sys.argv) == 4:
        with ThreadPoolExecutor() as executor:
            executor.map(extbrute(sys.argv[1], sys.argv[2], sys.argv[3]),timeout=10)
    else:
        pass

    endTime = datetime.now()
    totalTime = endTime - startTime
    print("Completed in ", totalTime)

if __name__ == '__main__':
    main()