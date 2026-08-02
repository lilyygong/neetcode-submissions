class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output = [[] for _ in range(numRows)]
        curr_row = 0
        going_down = False
        if numRows == 1:
            return s
        for c in s:
            output[curr_row].append(c)
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            if going_down:
                curr_row += 1
            else:
                curr_row -= 1
        output_string = ''.join([''.join(row) for row in output])
        return output_string