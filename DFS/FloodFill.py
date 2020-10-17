from typing import List
image= [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 1
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        starting_pixel = image[sr][sc]
        if newColor ==starting_pixel:
            return image

        self.dfs( image, sr, sc, newColor, starting_pixel)
        return image


    def dfs(self, image, sr, sc, newColor, starting_pixel):
        if sr >= 0 and sr < len(image) and sc >= 0 and sc < len(image[0]):
            if image[sr][sc] == starting_pixel:
                image[sr][sc]= newColor

                self.dfs(image, sr + 1, sc, newColor, starting_pixel)
                self.dfs(image, sr - 1, sc, newColor, starting_pixel)
                self.dfs(image, sr, sc + 1, newColor, starting_pixel)
                self.dfs(image, sr, sc - 1, newColor, starting_pixel)
            elif image[sr][sc] != starting_pixel:
                return
        else:
            return


obj=Solution()
print(obj.floodFill(image, sr, sc, newColor))
