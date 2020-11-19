import zerorpc

class HelloRPC(object):
    def belipulsa(self, nama, jumlah):
        c = zerorpc.Client()
        c.connect("tcp://127.0.0.1:4242")
        hasil = c.mutasi(nama, jumlah)
        if hasil :
            return "Transaksi berhasil"
        else :
            return "Transaksi gagal"

try :
    s = zerorpc.Server(HelloRPC())
    s.bind("tcp://0.0.0.0:4241")
    s.run()
except KeyboardInterrupt:
    print("Keluar")