class BUKU:
    def __init__(self,Judul,Penulis):
        self.judul  = Judul
        self.Penulis = Penulis

    def introduce_self(self):
        print("Judul Buku : "+ self.judul)
        print("Penulis : "+ self.Penulis)

# Daftar untuk menyimpan buku-buku
daftar_buku = []

buku1 = BUKU("Cara Belajar koding dengan mudah", "Rafiq")
buku2 = BUKU("Python untuk Pemula", "Andi")

# Menambah buku ke daftar
daftar_buku.append(buku1)
daftar_buku.append(buku2)

# Menampilkan semua buku
print("=== Daftar Buku ===")
for buku in daftar_buku:
    buku.introduce_self()
    print()

# Menghapus buku dari daftar
daftar_buku.remove(buku2)
print("Buku2 telah dihapus dari daftar")

# Menampilkan buku yang tersisa
print("\n=== Buku yang Tersisa ===")
for buku in daftar_buku:
    buku.introduce_self()