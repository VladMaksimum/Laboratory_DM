def count_contr_bits(block: str, cnt_inds: list[int]) -> None:
    for i in cnt_inds:
        cur_pos = i-1
        cnt = ''

        while cur_pos < len(block):
            cnt += block[cur_pos:cur_pos+1:]
            cur_pos += (i*2)
        
        block = block[:(i-1):] + str(cnt.count("1") % 2) + block[(i-1)::]

if __name__ == "__main__":
    block = '01010000011001010110111001110100'
    count_contr_bits(block, [1,2,4,8,16,32])
    print(block)

