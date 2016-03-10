import xmlrpclib
import pickle
import time

if __name__ == '__main__':
    proxy = xmlrpclib.ServerProxy("http://localhost:65530")

    start.time = time.time()

    feeds = {}
    feeds = proxy.getTop10()
    data = pickle.loads(feeds)

    i = 0
    while i < 10:
        print data[i]
        i = i + 1
        
    elapsed_time = time.time() - start.time
    print elapsed_time
