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