class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        self.helper(sr, sc, color, image, newColor)
        return image
        
    def helper(self, row, col, color, image, newColor):
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] == newColor or image[row][col] != color:
            return
        
        image[row][col] = newColor
        self.helper(row+1, col, color, image, newColor)
        self.helper(row-1, col, color, image, newColor)
        self.helper(row, col+1, color, image, newColor)
        self.helper(row, col-1, color, image, newColor)
        