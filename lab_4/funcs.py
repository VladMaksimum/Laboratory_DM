from typing import Self

class Node:
    def __init__(self, parent, left, right, symbols):
        self.parent= parent
        self.left = left
        self.right = right
        self.smbs = symbols

def count_huffman_codes(counter: dict[str, int]) -> dict[str, str]:
    res: dict[str, str] = {}
    frq = [(item, cnt) for item, cnt in counter.items()]
    for symbol in counter.keys():
        res[symbol] = ''
    

    while len(frq) > 1:
        for smb in frq[0][0]:
            res[smb] = '1' + res[smb]
        for smb in frq[1][0]:
            res[smb] = '0' + res[smb]
        
        rm1 = frq.pop(0)
        rm2 = frq.pop(0)
        frq.append((rm1[0] + rm2[0], rm1[1] + rm2[1]))

        frq.sort(key=lambda item: item[1])
    return res

def encode_huffman(file_path: str, codes: dict[str, str], res_file: str) -> None:
    with open(file_path) as file:
        with open(res_file, "a+") as result:
            line = file.readline()

            while line:
                for symbol in line:
                    if symbol in codes.keys():
                        result.write(codes[symbol])
                    else:
                        result.write(symbol)
                
                line = file.readline()

def encode_lzw_codes(file_path: str, symbols: list[str], bits: int, q_smbs: int, res_file: str) -> int:
    with open(res_file, "w") as res:
        res.write('')
    
    len_code = 0


    with open(file_path) as file:
        line = file.readline()
        preffix = ''

        while line:
            if q_smbs > 2**bits:
                bits += 1

            for symbol in line:
                if symbol != '\n':
                    if (preffix + symbol) in symbols:
                        preffix += symbol
                    else:
                        symbols.append(preffix + symbol)
                        q_smbs += 1
                        output = bin(symbols.index(preffix))[2:]

                        if len(output) < bits:
                            output = "0" * (bits - len(output)) + output
                        
                        len_code += len(output)
                        preffix = symbol
                        
                        with open(res_file, "a") as res:
                            res.write(output)
                else:
                    with open(res_file, "a") as res:
                            res.write(symbol)
            line = file.readline()
    
    return len_code

    