class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        if not matrix or not matrix[0]:
            return False
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Pointers representing the start and end of the "flattened" matrix
        left = 0
        right = (rows * cols) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Convert the 1D mid index into 2D row and column coordinates
            mid_val = matrix[mid // cols][mid % cols]
            
            # Standard binary search logic
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False