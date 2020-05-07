class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        sk = [-1]
        res = 0
        
        '''
        根据木桶原理，经典利用stack构建升序
        遍历heights， 如果当前高度大于stack top 就插入
        如果小于stack top就弹出并且计算。
        把当前height看做一个挡板，弹出之后还是要插入stack里
        只是每次计算弹出来的height所构成的面积。
        面积需要知道h x w, h即弹出来当前木版的高度
        w就是前一个到挡板i的距离，为了计算所有的height 要在初始放入-1
        到stack中。这样每次弹出就计算面积和最终答案比较。
        
        一开始在heights末尾加入0也是为了把stack里的木版都弹出来。
        '''
        
        for i in range(len(heights)):
            while heights[i] < heights[sk[-1]]:
                h = heights[sk.pop()]
                w = i - sk[-1] - 1
                res = max(res, h * w)
            sk.append(i)
            
        return res

            