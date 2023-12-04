#Fungsi
# Membuat fungsi
def tampilkan(nama): # definisi fungsi
#"""fungsi ini untuk menampilkan nama yang dikirim melalui parameter"""
    print("Hello", nama, ". Selamat datang")

# Memanggil fungsi
tampilkan("Ari") # call function with string input 'Ari'
nama = "Ari Santoso"
tampilkan(nama) # call function with variable nama

#Fungsi dengan return value
# Membuat fungsi
def hitung(a, b): # definisi fungsi
    return a + b

# Memanggil fungsi
hitung(4, 5) # call function with int input 4 and 5
a = 10
b = 15
hitung(a, b) # call function with variable a and b

#Fungsi dengan argument default
# Membuat Fungsi
def tampilkan(nama, msg=". Apa kabar?"): # definisi fungsi
#"""fungsi ini untuk menampilkan nama yang dikirim melalui parameter"""
    print("Hello", nama, msg)

# Memanggil Fungsi
tampilkan("Ari") # call function with string input 'Ari'
nama = "Ari Santoso"
tampilkan(nama) # call function with variable nama
tampilkan(nama, ". Selamat datang") # call function with variable nama and string '. Selamat datang'

#Fungsi dengan Keyword Arguments
# Membuat Fungsi
def hitung(a, b): # definisi fungsi
    return a + b

# Memanggil Fungsi
hitung(4, 5) # call function with int input 4 and 5
hitung(a=10, b=15) # call function with keyword a and b
hitung(b=15, a=25) # call function with keyword b and a
hitung(10, b=25) # call function with input 10 and keyword b

#Fungsi dengan Arbitrary Arguments
# Membuat Fungsi
def tampilkan(*names): # definisi fungsi
    for nama in names:
        print("Hello", nama, ". Apa kabar?")

# Memanggil Fungsi
tampilkan("Ari") # call function with string input 'Ari'
tampilkan("Ari","Dina","Ratna") # call function with list of name

# Lambda function
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# filter out only the even items from a list
new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)

# double each item in a list using map()
new_list = list(map(lambda x: x * 2 , my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)