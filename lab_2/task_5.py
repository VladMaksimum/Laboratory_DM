def count_ways(i: int, j: int) -> int:
    #print(i , j)
    if i > m - 1 or j > n - 1:
        return 0
    if i == m - 1 and j == n - 1:
        return 1


    return count_ways(i+1, j) + count_ways(i, j+1)

def count_ways_special(i: int, j: int, last_move: str) -> int:
    #print(i , j, last_move)
    if i > m - 1 or j > n - 1:
        return 0
    if i == m - 1 and j == n - 1:
        return 1
    
    if last_move == "u":
        return count_ways_special(i, j+1, "r")


    return count_ways_special(i+1, j, "u") + count_ways_special(i, j+1, "r")


n = 17
m = 16
#table: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]
print(count_ways(0, 0))
print(count_ways_special(0,0,"s"))
