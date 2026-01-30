def count_contr_bits(block: str, cnt_inds: list[int]) -> str:
    for i in cnt_inds:
        cur_pos = i-1
        cnt = ''

        while cur_pos < len(block):
            cnt += block[cur_pos : cur_pos + i:]
            cur_pos += (i*2)
        
        block = block[:(i-1):] + str(cnt.count("1") % 2) + block[(i)::]
    return block

def decode(block: str, cnt_inds: list[int]) -> str:
    indexs = cnt_inds[::-1]
    for i in indexs:
        block = block[:(i-1):] + block[(i)::]
    
    res = ''
    for j in range(0, len(block), 8):
        res += chr(int(block[j:(j+8):], 2))
    
    return res

if __name__ == "__main__":
    print(decode('11010011000001100010101101110011110100', [1,2,4,8,16,32]))

