# membuat stack
def buat_stack():
    stack = [36, 38]
    return stack

# memeriksa apakah stack kosong
def check_empty(stack):
    return len(stack) ==0

# menambahkan item pada posisi teratas
def push(stack, item):
    stack.append(item)
    print("Ukuran sepatu yang masuk : ", +item)

# menghapus item pada posisi teratas
def pop(stack):
    if (check_empty(stack)):
        return print("Sepatu pada rak kosong")
    print("Ukuran sepatu yang terjual : ", stack.pop())

# menghitung elemen stack
def size(stack):
    print("Jumlah sepatu yang ada pada rak : ", len(stack))

# menentukan elemen paling atas
def top(stack):
    top = len(stack)-1
    if top <0:
        print("Tidak terdefinisikan")
    else:
        print("Ukuran sepatu teratas : ", stack[top])

# memanggil hasil stack
def tampilkan(stack):
    print(stack)

A = buat_stack()

print("============================================")
print("||             TOKO ADIDAS SHOES          ||")
print("||----------Tumpukan sepatu pada Rak------||")
print("============================================")

# data awal pada stack
print("Ukuran sepatu yang ada pada rak saat ini : ", A)
top(A)
size(A)
print()

# Sepatu terjual
pop(A)
pop(A)
print("Ukuran sepatu yang ada pada rak saat ini : ", A)
top(A)
size(A)
print()
# Sepatu masuk
push(A, 39)
push(A, 41)
print("Ukuran sepatu yang ada pada rak saat ini : ", A)
top(A)
size(A)
print()