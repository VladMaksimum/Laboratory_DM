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
        
        for j in range(0, len(line) - 1, 2):
            if line[j+1] != '\n':
                if not line[j] + line[j+1] in counter_pairs.keys():
                    counter_pairs[line[j] + line[j+1]] = 1
                else:
                    counter_pairs[line[j] + line[j+1]] += 1
    

        line = file.readline()

smb_cnt = 0
counter_smb = dict(sorted(counter_smb.items(), key=lambda item: item[1]))
counter_pairs = dict(sorted(counter_pairs.items(), key=lambda item: item[1]))
codes = count_huffman_codes(counter_smb, 1)
codes_pairs = count_huffman_codes(counter_pairs, 2)
encode_huffman(text_path, codes, huff_file_path)

with open(stats_path, "w") as sfile:
    for symbol, cnt in counter_smb.items():
        smb_cnt += cnt
        sfile.write(f'<{symbol}> = {cnt}    {' ' * (4 - len(str(cnt)))} huffman_code = {codes[symbol]}\n')
    for symbol1, cnt1 in counter_pairs.items():
        sfile.write(f'<{symbol1}> = {cnt1}    {' ' * (4 - len(str(cnt1)))} huffman_code = {codes_pairs[symbol1]}\n')

print("Quantity of symbols:", smb_cnt)

len_huff_coded_text = 0
for item, code in codes.items():
    len_huff_coded_text += (counter_smb[item] * len(code))

len_pairs_coded_text = 0
cnt_p = 0
for item1, code1 in codes_pairs.items():
    cnt_p += counter_pairs[item1]
    len_pairs_coded_text += (counter_pairs[item1] * len(code1))
print(cnt_p)

print("Unicode lenght:", smb_cnt * 6)
print("Huffman codes lenght:", len_huff_coded_text)
print("Huffman codes for pairs lenght:", len_pairs_coded_text)

q_information = 0.0
for frq in counter_smb.values():
    q_information -= (frq / smb_cnt * log2(frq / smb_cnt))

q_huff_codes = len_huff_coded_text / smb_cnt
q_pairs_info = len_pairs_coded_text / smb_cnt

print("Comresion:", q_huff_codes / 6)
print("Information Shannon:", q_information)
print("Information Huffman:", q_huff_codes)
print("Information Huffman for pairs:", q_pairs_info)
print("Difference HS/HP:", q_huff_codes / q_pairs_info)
print("Difference H/Sh:", q_huff_codes / q_information)

len_lzw_code = encode_lzw_codes(text_path, list(counter_smb.keys()), 6, len(counter_smb.keys()), lzw_file_path)

print("LZW codes lenght:", len_lzw_code)
q_lzw_info = len_lzw_code / smb_cnt
print("Information LZW codes:", q_lzw_info)
print("Difference LZW/Sh:", q_lzw_info / q_information)
print("Difference LZW/H:", q_lzw_info / q_huff_codes)
