

bitlist_to_binary = lambda bitlist: "0b" + ''.join("1" if x else "0" for x in bitlist)

b = list(map(bool, map(int, "010101010101")))
c = list(map(bool, map(int, "000000111111")))

print(bitlist_to_binary(b))
print(bitlist_to_binary(c))

for i in range(len(b)):
    b[i] |= c[i]

print(bitlist_to_binary(b))



