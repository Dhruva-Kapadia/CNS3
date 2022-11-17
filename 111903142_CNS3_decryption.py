def addin(temp):
    i = (16-temp)%16
    return i

def multin(temp):
    inv = [-1, 1, 9, 6, 13, 7, 3, 5, 15, 2, 12, 14, 10, 4, 11, 8]
    #print(temp)
    #print(inv[temp])
    return inv[temp]

key = "111111011100011110100011"
sk1 = int(key[0:4],2)
sk2 = int(key[4:8],2)
sk3 = int(key[8:12],2)
sk4 = int(key[12:16],2)
sk5 = int(key[16:20],2)
sk6 = int(key[20:24],2)
  
ciphertext = "1011101101001011"
x1 = int(ciphertext[0:4],2)
x2 = int(ciphertext[4:8],2)
x3 = int(ciphertext[8:12],2)
x4 = int(ciphertext[12:16],2)

s1 = (x1 ^ multin(sk1))%17
s2 = (x2 + addin(sk2))%16
print(bin(s2))
s3 = (x3 + addin(sk3))%16
s4 = (x4 * multin(sk4))%17
s5 = (s1 ^ s3)
s6 = (s2 ^ s4)
s7 = (s5 * multin(sk5))%17
s8 = (s6 + s7)%16
s9 = (s8 * multin(sk6))%17
s10 = (s7 + s9)%16
s11 = (s1 ^ s9)
s12 = (s3 ^ s9)
s13 = (s2 ^ s10)
s14 = (s4 ^ s10)

plaintext2 = bin(s11)[2:].zfill(4) + bin(s13)[2:].zfill(4) + bin(s12)[2:].zfill(4) + bin(s14)[2:].zfill(4)
print(plaintext2)
