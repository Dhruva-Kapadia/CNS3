key = "11101110110110101111001110011011"
sk1 = int(key[0:4],2)
sk2 = int(key[4:8],2)
sk3 = int(key[8:12],2)
sk4 = int(key[12:16],2)
sk5 = int(key[16:20],2)
sk6 = int(key[20:24],2)

plaintext = "0100000101101101"
x1 = int(plaintext[0:4],2)
x2 = int(plaintext[4:8],2)
x3 = int(plaintext[8:12],2)
x4 = int(plaintext[12:16],2)

s1 = (x1 * sk1)%17
s2 = (x2 + sk2)%16
s3 = (x3 + sk3)%16
s4 = (x4 * sk4)%17
s5 = (s1 ^ s3)
s6 = (s2 ^ s4)
s7 = (s5 * sk5)%17
s8 = (s6 + s7)%16
s9 = (s8 * sk6)%17
s10 = (s7 + s9)%16
s11 = (s1 ^ s9)
s12 = (s3 ^ s9)
s13 = (s2 ^ s10)
s14 = (s4 ^ s10)

ciphertext = bin(s11)[2:].zfill(4) + bin(s12)[2:].zfill(4) + bin(s13)[2:].zfill(4) + bin(s14)[2:].zfill(4)
print(ciphertext)
