class Solution:
    def convert(self, s: str, numRows: int) -> str:
        curr_row = 0
        going_down = False
        zigzag = [[] for _ in range(numRows)]
        for i in range(len(s)):
            zigzag[curr_row].append(s[i])
            if curr_row == 0 or curr_row == numRows-1:
                going_down = not going_down
            if going_down:
                curr_row += 1
            else:
                curr_row -= 1
        output = "".join("".join(row) for row in zigzag)
        return output

