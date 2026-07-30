class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_order = []
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        while top < bottom and left < right:
            for i in range(left, right): # top row
                spiral_order.append(matrix[top][i])
            top += 1
            for j in range(top, bottom): # right
                spiral_order.append(matrix[j][right - 1])
            right -= 1
            if top < bottom:
                for k in range(right - 1, left - 1, -1):
                    spiral_order.append(matrix[bottom - 1][k])
                bottom -= 1
            if left < right:
                for j in range(bottom - 1, top - 1, -1):
                    spiral_order.append(matrix[j][left])
                left += 1
        return spiral_order