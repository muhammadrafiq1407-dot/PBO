class HewanPeliharaan:
    def __init__(self,nama,hewan,umur):
        self.pemilik = nama
        self.nama = hewan
        self.umur = umur
        
    def introduce_self(self):
        print("Pemilik Hewna : " +self.pemilik)
        print("Jenis hewan : " +self.nama)
        print("Umur Hewan : " +self.umur)


Hewan1 = HewanPeliharaan("rafiq","Kucing"," 4 bulan")
Hewan2 = HewanPeliharaan("Rehan","Ikan arwana","2 bulan")

Hewan1.introduce_self()
Hewan2.introduce_self()