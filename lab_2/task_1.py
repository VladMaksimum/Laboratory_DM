word = "KOMBINATORIKA"
letters: dict[str,int] = {}
cnt = 0

for letter in word:
    if letter in letters.keys():
        continue
    letters[letter] = word.count(letter)
    
def is_possible(s: str) -> bool:
    for letter, limit in letters.items():
        if s.count(letter) > limit:
            return False
        
    return True

for s1 in letters.keys():
    for s2 in letters.keys():
        if not is_possible(s1 + s2):
            continue

        for s3 in letters.keys():
            if not is_possible(s1 + s2 + s3):
                continue

            for s4 in letters.keys():
                if not is_possible(s1 + s2 + s3 + s4):
                    continue
                
                for s5 in letters.keys():
                    if not is_possible(s1 + s2 + s3 + s4 + s5):
                        continue
                    
                    for s6 in letters.keys():
                        if not is_possible(s1 + s2 + s3 + s4 + s5 + s6):
                            continue

                        s = s1 + s2 + s3 + s4 + s5 + s6
                        cnt += 1

print(cnt)

