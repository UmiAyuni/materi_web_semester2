stack = [1, 2, 3, 4, 5]
print('data sekarang: ', stack)

# memasukkan data baru
stack.append(6)
print('Data masuk: ', 6)
print('Data sekarang: ', stack)
stack.append(7)
print('Data masuk: ', 7)
print('Data sekarang: ', stack)

out = stack.pop()
print('data keluar: ', out)
print('data sekarang: ',stack)