from funcs import count_contr_bits
from funcs import decode


word = "Pentium "
bits = ''

for symbol in word:
    bits_tmp = bin(ord(symbol))[2:]
    if len(bits_tmp) < 8:
        bits_tmp = '0' * (8 - len(bits_tmp)) + bits_tmp
    
    bits += bits_tmp

print("Transform to bits:", bits)
blocks = [bits[:32:], bits[32::]]
print("Separate into 2 blocks:", blocks)
contr_bits_indexs = [1,2,4,8,16,32]

for i in contr_bits_indexs:
    blocks[0] = blocks[0][:(i-1):] + "0" + blocks[0][(i-1)::]
    blocks[1] = blocks[1][:(i-1):] + "0" + blocks[1][(i-1)::]
print("Add control bits:", blocks)

for j in range(len(blocks)):
    blocks[j] = count_contr_bits(blocks[j], contr_bits_indexs)


i1, i2 = 5, 21
print("Count control bits",  blocks)


if blocks[0][i1-1] == "1":
    blocks[0] = blocks[0][:(i1-1):] + "0" + blocks[0][(i1)::]
else:
    blocks[0] = blocks[0][:(i1-1):] + "1" + blocks[0][(i1)::]

if blocks[1][i2-1] == "1":
    blocks[1] = blocks[1][:(i2-1):] + "0" + blocks[1][(i2)::]
else:
    blocks[1] = blocks[1][:(i2-1):] + "1" + blocks[1][(i2)::]

message = blocks.copy()
print("After breaking:",  blocks)

for i in contr_bits_indexs:
    blocks[0] = blocks[0][:(i-1):] + "0" + blocks[0][(i)::]
    blocks[1] = blocks[1][:(i-1):] + "0" + blocks[1][(i)::]

for j in range(len(blocks)):
    blocks[j] = count_contr_bits(blocks[j], contr_bits_indexs)


print("Recount bits:", blocks)

broken_message = ''
for block in blocks:
    broken_message += decode(block, contr_bits_indexs)

print("Broken message:", "<" + broken_message + ">")

brk_ind = [0, 0]
for k in range(len(message)):
    for l in range(len(message[k])):
        if message[k][l] != blocks[k][l]:
            brk_ind[k] += (l + 1)

print("Broken bits:", brk_ind)

i3, i4 = brk_ind[0], brk_ind[1]

if blocks[1][i4-1] == "1":
    blocks[1] = blocks[1][:(i4-1):] + "0" + blocks[1][(i4)::]
else:
    blocks[1] = blocks[1][:(i4-1):] + "1" + blocks[1][(i4)::]

if blocks[0][i3-1] == "1":
    blocks[0] = blocks[0][:(i3-1):] + "0" + blocks[0][(i3)::]
else:
    blocks[0] = blocks[0][:(i3-1):] + "1" + blocks[0][(i3)::]

print("Fix bits:", blocks)

for i in contr_bits_indexs:
    blocks[0] = blocks[0][:(i-1):] + "0" + blocks[0][(i)::]
    blocks[1] = blocks[1][:(i-1):] + "0" + blocks[1][(i)::]

for j in range(len(blocks)):
    blocks[j] = count_contr_bits(blocks[j], contr_bits_indexs)

print("Recount bits:", blocks)

print("Decoded meassge:", "<" + decode(blocks[0], contr_bits_indexs) + decode(blocks[1], contr_bits_indexs) + ">")
 

