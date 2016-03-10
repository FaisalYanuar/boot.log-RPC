from SimpleXMLRPCServer import SimpleXMLRPCServer
import pickle
import os

class RPCServer:
    '''
    classdocs
    '''

    def getTop10(self):
        sentence = {}
        for filename in os.listdir("filenya/."):
            print filename
            for line in open("filenya/"+filename).xreadlines():
                #print line

                #cek = line.split(": ")
                #cek = " ".join(cek[1:])
                #cek = cek.split("\n")[0]

                cek = line.split()
                cek = " ".join(cek[4:])
                #print line
                #print cek
                if (cek in sentence):
                    sentence[cek] = sentence[cek] + 1
                else:
                    sentence[cek] = 0


        #print sentence
        #print sentence.items()

        sort = sorted(sentence.items(), key=lambda x:x[1], reverse=True)
        sort = pickle.dumps(sort)
        return sort

    def __init__(self):
        '''
        Constructor
        '''
        self.server = SimpleXMLRPCServer(('192.168.236.53',65530))
        print "listening at 65530"
        self.server.register_function(self.getTop10, 'getTop10')
        #self.server.allow_none = True
        self.server.serve_forever()


if __name__ == "__main__":
    server = RPCServer()
