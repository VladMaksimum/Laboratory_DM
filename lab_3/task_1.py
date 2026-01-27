
word = "Pentium "
bits = ''

for symbol in word:
    bits_tmp = bin(ord(symbol))[2:]
    if len(bits_tmp) < 8:
        bits_tmp = '0' * (8 - len(bits_tmp)) + bits_tmp
    
    bits += bits_tmp

blocks = [bits[:32:], bits[32::]]
print(blocks)
contr_bits_indexs = [1,2,4,8,16,32]

for i in contr_bits_indexs:
    blocks[0] = blocks[0][:(i-1):] + "0" + blocks[0][(i-1)::]
    blocks[1] = blocks[1][:(i-1):] + "0" + blocks[1][(i-1)::]

