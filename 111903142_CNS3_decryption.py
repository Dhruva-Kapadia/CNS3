def addin(temp):
    i = (16-temp)%16
    return i

def multin(temp):
    for i in range(0, 17):
        if ((temp%17)*(i*17))%17 == 1:
            return i
    return -1

key = "11101110110110101111001110011011"
sk1 = int(key[0:4],2)
sk2 = int(key[4:8],2)
sk3 = int(key[8:12],2)
sk4 = int(key[12:16],2)
sk5 = int(key[16:20],2)
sk6 = int(key[20:24],2)
  
ciphertext = "1111100100000100"
x1 = int(ciphertext[0:4],2)
x2 = int(ciphertext[4:8],2)
x3 = int(ciphertext[8:12],2)
x4 = int(ciphertext[12:16],2)

s1 = (x1 * multin(sk1))%17
s2 = (x2 + addin(sk2))%16
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

plaintext2 = bin(s11)[2:].zfill(4) + bin(s12)[2:].zfill(4) + bin(s13)[2:].zfill(4) + bin(s14)[2:].zfill(4)
print(plaintext2)
