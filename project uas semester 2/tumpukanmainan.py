# creating a stack (buat stack)
def create_stack():
    stack = [12, 13]
    return stack

# creating an empty stack (memeriksa apa stack kosong)
def check_empty(stack):
    return len(stack) == 0

# adding items into the stack (tambahkanitem pada stack)
def push(stack, item):
    stack.append(item)
    print("Kode buku yang dikembalikan : ", +item)

# menghapus item pada posisi teratas
def pop(stack):
    if (check_empty(stack)):
        return print("Mainan pada rak kosong")
    print("Mainan yang dibeli : ", stack.pop)

# menghitung elemen stack
def size(stack):
    print("Jumlah mainan yang ada di rak : ", len(stack))

# menentukan posisi elemen paling atas
def top(stack):
    top = len(stack)-1
    if top <0:
        print("Tidak terdefinisikan")
    else:
        print("Mainan teratas : ",stack[top])

# menampilkan hasil stack
def tampilkan(stack):
    print(stack)

s = create_stack()
print("============================================")
print("||              TOKO MAINAN BUNA          ||")
print("||----------Tumpukan Mainan pada Rak------||")
print("============================================")

# Data awal pada stack
print("Mainan yang ada pada rak saat ini : ",s)
top(s)
size(s)
print()

# Mainan terbeli
pop(s)
# Mainan masuk

