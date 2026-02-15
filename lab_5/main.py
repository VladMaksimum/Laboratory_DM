import numpy as np
from funcs import create_gener_matrix, generate_codes, count_distance, is_wrong, divison, generate_errors
import itertools

n = 31
m = 16

px = '1000111110101111'
gener_matr_file = "lab_5/generMatrix.txt"
codes_file = 'lab_5/codes.txt'
distance_file = 'lab_5/distances.txt'
error_file = "lab_5/errors.txt"

v = create_gener_matrix(n, m, px)
codes_info = [''.join(i) for i in itertools.product(['1', '0'], repeat=m)]
codes = generate_codes(m, n, codes_info, v, codes_file)

dis, min_dis = count_distance(n ,codes)
print("Minimum distance:", min_dis)
if min_dis % 2 == 1:
    qu = (min_dis - 1) // 2
else:
    qu = min_dis / 2 - 1

print("Max fix errors:", qu)
print("Max find error:", min_dis - 1)

np.savetxt(distance_file, dis, fmt='%s')
np.savetxt(gener_matr_file, v, fmt='%s')

#Examples
print("==================")
print()
print("==================")
print("Examples")

errors = generate_errors(n, px, error_file)
s0 = '1111111111111111111111111111111'
s1 = '0000001111111111111111111111111'
s2 = '1111111111101101001010111111110'
print("Initial code", s0)

print(s1, "is broken code?", is_wrong(s1, px))
print(s2, "is broken code?", is_wrong(s2, px))

s3 = '0001111111111111111111111111111'

s3_sindrom = divison(s3, px)

print("Sindrom for", s3, ":", s3_sindrom)
print("Error vector:", errors[s3_sindrom], "can fix error")

s4 = "0000111111111111111111111111110"

s4_sindrom = divison(s4, px)

print("Sindrom for", s4, ":", s4_sindrom)
print("Error vector:", errors[s4_sindrom], "cant fix error")