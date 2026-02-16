class RuangUjian:
    def __init__(self,ruangan,Pengawas,PesertaUjian):
        self.ruangan = ruangan
        self.pengawas = Pengawas
        self.peserta = PesertaUjian
        
    def introduce_self(self):
        print("Ruangan : " +self.ruangan)
        print("Nama Pengawas : " +self.pengawas)
        print("Nama Peserta Ujian : " +self.peserta)


Ruangan1 = RuangUjian("1","Pak ASwan","udin ,muahmmad ,torik")
Ruangan2 = RuangUjian("2","Pak wanur","mahdi ,putra,rafiq,ari")

Ruangan1.introduce_self()
Ruangan2.introduce_self()
