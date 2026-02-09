from funcs import count_huffman_codes
from math import log2
from funcs import encode_huffman
from funcs import encode_lzw_codes

text_path = "lab_4/text.txt"
huff_file_path = "lab_4/huffman_coded_text.txt"
stats_path = "lab_4/stats.txt"
lzw_file_path = "lab_4/lzw_coded_text.txt"
counter_smb: dict[str, int] = {}
counter_pairs: dict[str, int] = {}

with open(text_path) as file:
    s = ''

    line = file.readline()
    while line:
        for i in range(len(line) - 1):
            if not line[i] in counter_smb.keys():
                counter_smb[line[i]] = 1
            else:
                counter_smb[line[i]] += 1
            
            if line[i+1] != '\n':
                if not line[i] + line[i+1] in counter_pairs.keys():
                    counter_pairs[line[i] + line[i+1]] = 1
                else:
                    counter_pairs[line[i] + line[i+1]] += 1
    

        line = file.readline()

smb_cnt = 0
counter_smb = dict(sorted(counter_smb.items(), key=lambda item: item[1]))
codes = count_huffman_codes(counter_smb)
encode_huffman(text_path, codes, huff_file_path)

with open(stats_path, "w") as sfile:
    for symbol, cnt in counter_smb.items():
        smb_cnt += cnt
        sfile.write(f'<{symbol}> = {cnt}    {' ' * (4 - len(str(cnt)))} huffman_code = {codes[symbol]}\n')
    for symbol1, cnt1 in counter_pairs.items():
        sfile.write(f'<{symbol1}> = {cnt1}\n')

print("Quantity of symbols:", smb_cnt)

len_huff_coded_text = 0
cnt1 = 0
for item, code in codes.items():
    cnt1 += counter_smb[item]
    len_huff_coded_text += (counter_smb[item] * len(code))

print("Unicode lenght:", smb_cnt * 6)
print("Huffman codes lenght:", len_huff_coded_text)

q_information = 0.0
for frq in counter_smb.values():
    q_information -= (frq / smb_cnt * log2(frq / smb_cnt))

q_huff_codes = len_huff_coded_text / smb_cnt


print("Comresion:", q_huff_codes / 6)
print("Information Shannon:", q_information)
print("Information Huffman:", q_huff_codes)
print("Difference H/Sh:", q_huff_codes / q_information)

len_lzw_code = encode_lzw_codes(text_path, list(counter_smb.keys()), 6, len(counter_smb.keys()), lzw_file_path)

print("LZW codes lenght:", len_lzw_code)
q_lzw_info = len_lzw_code / smb_cnt
print("Information LZW codes:", q_lzw_info)
print("Difference LZW/Sh:", q_lzw_info / q_information)
print("Difference LZW/H:", q_lzw_info / q_huff_codes)
