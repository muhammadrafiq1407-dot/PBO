class BUKU:
    def __init__(self, Judul: str,Penulis: str,NoBuku: str):
        self.jd = Judul
        self.pn = Penulis
        self.nb = NoBuku
        self.sb = False
    
    def buku_diPinjam(self):
        "Buku Yang di pinjam"
        self.sb = True
    def buku_diKembalikan(self) :
        "Buku Yang di kembalikan"
        self.sb = False

    def Status_buku(self):
        status = "Dipinjam" if self.sb else "Tersedia"
        return f"{self.jd} - {self.pn}"
    
class PENGGUNA:
    def __init__(self,name,no_id):
        self.nama = name
        self.id_p = no_id
        self.Penyimpanan_Status_buku = [] 


    def __str__(self):
        return f"Pengguna : {self.nama} (Id Pengguna: {self.id_p})"  


class KARYAWAN:
    def __init__(self,name,id_karyawan):
        self.nama = name
        self.id_k = id_karyawan

    def __str__(self):
        return f"Karyawan : {self.nama} (NIP karyawan : {self.id_k})"
    

class Transaksi:
    
    Jumlah_Transaksi = 0

    def __init__(self,book,pengguna,karyawan):
        Transaksi.Jumlah_Transaksi += 1
        self.id_transaksi = f"TRX -{Transaksi.Jumlah_Transaksi : 03d}"

        self.book = book
        self.pengguna = pengguna
        self.karyawan = karyawan
        self.borrow_date = self._get_current_date()  # ATRIBUT YANG HILANG
        self.returned = False
    
    def _get_current_date(self):
        """Simulasi tanggal (karena tanpa import datetime)"""
        return "2026-02-21"
    
    def borrow_book(self, staff):
        """Proses peminjaman - PERBAIKAN: book sudah ada di self.book"""
        if not self.book.sb:
            self.book.buku_diPinjam()
            print(f"[OK] {self.pengguna.nama} pinjam '{self.book.jd}'")
            print(f"     Diproses oleh: {staff.nama}")
            print(f"     Tanggal: {self.borrow_date}")
        else:
            print(f"[GAGAL] '{self.book.jd}' sudah dipinjam")
    
    def return_book(self, staff):
        """Proses pengembalian - PERBAIKAN: book sudah ada di self.book"""
        if not self.returned:
            self.book.buku_diKembalikan()
            self.returned = True
            print(f"[OK] {self.pengguna.nama} kembalikan '{self.book.jd}'")
            print(f"     Diproses oleh: {staff.nama}")
    
    def __str__(self):
        status = "Dikembalikan" if self.returned else "Dipinjam"
        return f"[{self.id_transaksi}] {self.pengguna.nama} - {self.book.jd} ({status})"



def main():
    print("="*50)
    print("SISTEM PERPUSTAKAAN - SESUAI UML (DIPERBAIKI)")
    print("Tanpa Import - Pure Python")
    print("="*50)
    
    
    print("\n---BUKU ---")
    book1 = BUKU("Python Programming", "John Doe", "ISBN-001")
    book2 = BUKU("Data Structures", "Jane Smith", "ISBN-002")
    book3 = BUKU("Machine Learning", "Bob Johnson", "ISBN-003")
    print(f" {book1}")
    print(f" {book2}")
    print(f" {book3}")
    
    
    print("\n---KARYAWAN ---")
    staff1 = KARYAWAN("Ani", "STF-001")
    staff2 = KARYAWAN("Budi", "STF-002")
    print(f" {staff1}")
    print(f" {staff2}")
    
    
    print("\n---PENGGUNA ---")
    member1 = PENGGUNA("RAFIQ", "MBR-001")
    member2 = PENGGUNA("Siti", "MBR-002")
    print(f" {member1}")
    print(f" {member2}")
    
    
    print("\n" + "-"*50)
    print("TRANSAKSI PEMINJAMAN 1")
    print("-"*50)
    trans1 = Transaksi(book1, member1, staff1)
    trans1.borrow_book(staff1) 
    member1.Penyimpanan_Status_buku.append(trans1)
    
    
    print("\n" + "-"*50)
    print("TRANSAKSI PEMINJAMAN 2")
    print("-"*50)
    trans2 =Transaksi(book2, member2, staff2)
    trans2.borrow_book(staff2)
    member2.Penyimpanan_Status_buku.append(trans2)
    
    
    print("\n" + "-"*50)
    print("COBA PINJAM BUKU YANG SUDAH DIPINJAM")
    print("-"*50)
    trans3 = Transaksi(book1, member2, staff1)
    trans3.borrow_book(staff1)
    
    
    print("\n--- STATUS BUKU ---")
    print(f"[BUKU] {book1}")
    print(f"[BUKU] {book2}")
    print(f"[BUKU] {book3}")
    
    
    print("\n--- PINJAMAN RAFIQ ---")
    if member1.Penyimpanan_Status_buku:
        for trans in member1.Penyimpanan_Status_buku:
            print(f"  {trans}")  
    else:
        print("  Tidak ada pinjaman")
    
    print("\n--- PINJAMAN SITI ---")
    if member2.Penyimpanan_Status_buku:
        for trans in member2.Penyimpanan_Status_buku:
            print(f"  {trans}")  
    else:
        print("  Tidak ada pinjaman")
    
    # RAFIQ kembalikan buku
    print("\n" + "-"*50)
    print("TRANSAKSI PENGEMBALIAN")
    print("-"*50)
    trans1.return_book(staff1) 
    
    # hasil RAFIQ mengembalikan buku
    print("\n--- STATUS SETELAH PENGEMBALIAN ---")
    print(f"[BUKU] {book1}")
    
    print("\n--- PINJAMAN RAFIQ SEKARANG ---")
    active = [t for t in member1.Penyimpanan_Status_buku if not t.returned]
    if active:
        for trans in active:
            print(f"  {trans}")  
    else:
        print("  Tidak ada pinjaman aktif")
    
    # RAFIQ pinjam buku 3
    print("\n" + "-"*50)
    print("TRANSAKSI PEMINJAMAN BARU")
    print("-"*50)
    trans4 = Transaksi(book3, member1, staff2)
    trans4.borrow_book(staff2)
    member1.Penyimpanan_Status_buku.append(trans4)
    
    print("\n--- PINJAMAN RAFIQ SEKARANG ---")
    for trans in member1.Penyimpanan_Status_buku:
        print(f"  {trans}")  
    # riwayat peminjman RAFIQ
    print("\n" + "="*50)
    print("RINGKASAN TRANSAKSI")
    print("="*50)
    print(f"Total transaksi: {Transaksi.Jumlah_Transaksi}")
    print(f"Buku dipinjam: {sum(1 for b in [book1, book2, book3] if b.sb)}")
    print(f"Buku tersedia: {sum(1 for b in [book1, book2, book3] if not b.sb)}")
    
    print("\n" + "="*50)
    print("PROGRAM SELESAI")
    print("="*50)


if __name__ == "__main__":
    main()                
