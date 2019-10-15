class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 来记录board里每一个字母是否有可能成为答案，不是则略过
        visited = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 对于board里每一个字母进行搜索，如果找到就返回
                if self.helper(i, j, board, 0, word, visited):
                    return True
        return False
    
    def helper(self, i, j, board, idx, word, visited):
        # 退出条件：如果达到了目标word的长度则找到
        if idx == len(word):
            return True
        
        # 边界条件：如果超过边界 或者这个字母之前标记过是错的，或者当前字母board[i][j]不是要找的word[idx]字母 则返回错，剪枝
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[idx] != board[i][j] or visited.get((i, j)):
            return False
        
        # 回溯开始，先假设这个是正确的字母，进行上下左右的搜索
        visited[(i, j)] = True
        
        # 上下左右的搜索，同时idx要+1 来搜索下一个字母
        res = self.helper(i+1, j, board, idx+1, word, visited) or \
            self.helper(i-1, j, board, idx+1, word, visited) or \
            self.helper(i, j+1, board, idx+1, word, visited) or \
            self.helper(i, j-1, board, idx+1, word, visited)
        
        # 已当前字母搜索上下左右完毕，如果没找到 则复原为false, 今后则略过
        visited[(i, j)] = False
        
        return res
            