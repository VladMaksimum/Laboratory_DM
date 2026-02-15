import numpy as np
import itertools

def divison(p1: str, p2: str):

    r = p1
    c_i = 0

    while len(r) >= len(p2):
        n_q = ''
        for i in range(0, len(p2)):
            if r[i] != p2[i]:
                n_q += '1'
            elif len(n_q) != 0:
                n_q += '0'
        
        r = n_q + p1[c_i + len(p2)::]
        c_i += (len(p2) - len(n_q))
        #print(r, p1[c_i::])
    
    return r

def to_string(array):
    res = ''

    for element in array:
        res += str(element)
    
    return res

def add_remain(m: int, array, remain: str):
    for i in range(len(remain)):
        array[i + m] = int(remain[i])
    

def create_gener_matrix(n: int, m: int, px: str):
    res  = np.eye(m, n, dtype=int)

    for i in range(len(res)):
        n_row = divison(to_string(res[i]), px)
        if len(n_row) < len(px) - 1:
            n_row = ("0" * (len(px) - len(n_row) - 1) + n_row)

        add_remain(m, res[i], n_row)

    return res

def count_ones(code, matrix, i, m):
    cnt = 0

    for j in range(m):
        if code[j] == '1' and matrix[j][i + m] == 1:
            cnt += 1
    
    return cnt

def generate_codes(m: int, n: int,  info_codes, matrix, file_path: str):
    res = []

    with open(file_path, 'w') as file:
        for code in info_codes:
            for i in range(n - m):
                code += str(count_ones(code, matrix, i, m) % 2)

            res.append(code)
            file.write(code + '\n')
        
    
    return res

def distance(c1: str, c2: str) -> int:
    cnt = 0

    for i in range(len(c1)):
        if c1[i] != c2[i]:
            cnt += 1
    
    return cnt  

def count_distance(n, codes):
    dis = np.zeros((n, n)).astype(int)
    min_dis = n + 1

    for i in range(n-1):
        for j in range(i + 1, n):
            d = distance(codes[i], codes[j])
            dis[i][j] = d
            dis[j][i] = dis[i][j]

            min_dis = min(min_dis, d)

    return (dis, min_dis)

def is_wrong(code: str, px: str) -> bool:
    sindrom = divison(code, px)

    if len(sindrom) == 0 or len(sindrom) == sindrom.count("0"):
        return False
    return True

def generate_errors(n, px, file_path: str):
    errs = itertools.product(['0', '1'], repeat=n//2)
    res = {}

    with open(file_path, 'w') as file:
        for error in errs:
            str_err = to_string(error) + (n - len(error)) * '0'
            #print(str_err)
            sindrom = divison(str_err, px)
            file.write(f"{str_err}  {sindrom}\n")

            res[sindrom] = str_err
    
    return res

if __name__ == "__main__":
    ...