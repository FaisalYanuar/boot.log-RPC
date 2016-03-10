import xmlrpclib
import pickle

if __name__ == '__main__':
    proxy = xmlrpclib.ServerProxy("http://localhost:65530")

    feeds = {}
    feeds = proxy.getTop10()
    data = pickle.loads(feeds)

    i = 0
    while i < 10:
        print data[i]
        i = i + 1