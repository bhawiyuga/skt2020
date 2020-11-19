import zerorpc

user = {
    "Andi" : 100000,
    "Budi" : 50000,
    "Candra" : 200000
}

class HelloRPC(object):
    def mutasi(self, nama, jumlah):
        global user
        saldo = user[nama]
        if jumlah < saldo :
            user[nama] = saldo - jumlah
            return True
        else :
            return False

try :
    s = zerorpc.Server(HelloRPC())
    s.bind("tcp://0.0.0.0:4242")
    s.run()
except KeyboardInterrupt:
    print("Keluar")