import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4241")
#print(c.hello("RPC"))
hasil = c.belipulsa("Andi",100000)
print(hasil)