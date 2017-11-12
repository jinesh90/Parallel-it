import time
import threading
import requests
from requests.exceptions import ConnectionError, ConnectTimeout


weblinks = [
            "https://www.google.com",
            "https://www.cnn.com",
            "https://www.yahoo.com",
            "https://www.baidu.com",
            "https://www.espn.com",
            "https://www.walmart.com",
            "https://www.facebook.com",
            "https://www.stanford.edu",
            "https://www.mit.edu",
            "http://www.alibaba.com"
]


def get_page(url):
    try:
        response = requests.get(url,verify=False)
        assert (response.status_code, 200, "Can not get page for {}".format(url))
        print(response.reason)
    except ConnectTimeout, ConnectionError:
        print("Connection Error for url {}".format(url))



# Sequ. fetching from web links

t1 = time.time()

for links in weblinks:
    get_page(links)

t2 = time.time()


#Parellel fetching


t3 = time.time()
threads = []
for links in weblinks:
    t = threading.Thread(target=get_page, args=(links,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

t4 = time.time()

print("Time for Seq. Execution is {} Seconds".format(t2-t1))

print("Time for Parallel Execution is {} Seconds".format(t4-t3))

