import requests
import sys 


sub = open ('subfile_new.txt').read()
subs =  sub.splitlines()
for s in subs :
    url = "https://{}.{}".format(s,sys.argv[1])
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("valid",url)
