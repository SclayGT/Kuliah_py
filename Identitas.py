angka1= 100
angka2= 100

print(angka1 is angka2)
print("Alokasi memori", id(angka1))
print("Alokasi memori", id(angka1)) 

list1 = [1,2,3]
list2 = [1,2,3]

print(list1 is list2) # Apakah variabel angka1 dan angka2 identik apa tidak?
print(list1 == list2)
print("Alokasi memori", id(list1))
print("Alokasi memori", id(list2))