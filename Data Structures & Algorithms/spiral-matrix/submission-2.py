class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        output = []
        # while it is a valid rectangle
        while top < bottom and left < right:
            for j in range(left, right):
                output.append(matrix[top][j])
            top += 1
            for k in range(top, bottom):
                output.append(matrix[k][right - 1])
            right -= 1
            if top < bottom: 
                for m in range(right - 1, left - 1, -1):
                    output.append(matrix[bottom - 1][m])
                bottom -= 1
            if left < right:
                for n in range(bottom - 1, top - 1, -1):
                    output.append(matrix[n][left])
                left += 1
        return output
