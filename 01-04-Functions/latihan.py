'''
1. prime = [2,3,5,7]

buat program untuk menentukan nilai max/min dari list tersebut

2. budimukidi

buat list untuk menghitung jumlah huruf yang ada, Contoh hasil: b:1, u:1, d:1

3. tambahkan sebuah key & value pada sebuah dictionary
contoh: {{0:"Ali"}, {1:"Syamsul"}}
'''

# 1. prime
# cara 1
prime = [2,3,5,7]
nilaimax = max(prime)
print(nilaimax)

nilaimin = min(prime)
print(nilaimin)

# cara 2
# mengurutkan huruf terkecil hingga huruf terbesar
prime = [2,3,5,7]
nilaimax = nilaimin = nilaiakhir = 0
for angka in prime:
    if angka > nilaiakhir:
        nilaimax = angka
        nilaiakhir = angka
    print(nilaimax) 

# 2. menghitung jumlah huruf
def hitung_huruf(teks):
    
    # Membuat dictionary untuk menyimpan frekuensi huruf
    frekuensi_huruf = {}
    
    # Menghitung setiap huruf dalam teks
    for huruf in teks:
        if huruf.isalpha():  # Memastikan hanya menghitung huruf alfabet
            huruf = huruf.lower()  # Mengubah huruf menjadi huruf kecil
            if huruf in frekuensi_huruf:
                frekuensi_huruf[huruf] += 1
            else:
                frekuensi_huruf[huruf] = 1
    
    return frekuensi_huruf

# Contoh penggunaan
teks = "budi mulkidi"
hasil = hitung_huruf(teks)
print(hasil)

# 3. key & value dictionary
dict = {"murid":"dahayu", "sekolah":"praxis"}
print(dict)

# add
dict["alamat"] = input ("masukkan alamat ")
print(dict)