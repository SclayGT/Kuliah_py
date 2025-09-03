# Nama: Rony Wijaya
# NIM: J0403251047
# Kelas: TPL B2

print(4*"=", " Soal No 3 ",4*"=")

# Menentukan sisa pembagian bilangan bulat dengan x

# Input bilangan dan nilai x
bilangan = int(input("Masukkan bilangan bulat: "))
x = int(input("Masukkan nilai x (x > 0): "))

# Pastikan x lebih dari 0
if x > 0:
    sisa = bilangan % x
    print(f"Hasil pembagian {bilangan} dibagi {x} adalah {bilangan//x}")
    print(f"Sisa dari {bilangan} dibagi {x} adalah {sisa}")
else:
    print("Nilai x harus lebih besar dari 0!")
