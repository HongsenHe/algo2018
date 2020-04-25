import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        char_map = collections.Counter(tasks)
        freq = sorted(char_map.values())
        max_val = freq[-1] - 1
        idle_slots = max_val * n
        
        '''
        先统计每个字母的个数并且排序，找到最多个数的字母作为基准，来填充。
        比如[A, A, A, B, B, B] n = 2
        char_map = {A:3, B:3} freq = [3, 3], max_val = 2
        因为不考虑最后一个字母比如A _ _ A _ _ AXXX， 不必再填充
        那这样idle_slots 就是2个A X idle n = 4, 即要填充4个idle
        
        for loop从倒数第二多的字母开始，最多的A已经作为了基准。
        如何填充idle? 如果有其他字母就用他来代替idle, 如果没有就用'idle'
        也就是答案 即 最后idle_slots的个数 加上tasks本身的长度。
        
        idle_slots -= min(max_val, freq[i])是什么？
        比如这个例子3个A和3个B, 用A做框架，但不能把3个B全都填充到A中间，
        因为A _ _ A _ _ A 只有两个空挡可以填充，多余的B只能放到最后一个A 后面
        也就是max_val = 2, freq[i] = 3 选择2
        如果freq[i] = 1, 那就只能满足放入第一个A的后面，但也算替换了一个idle.
        最后看剩下idle的数量
        '''
        
        for i in range(len(freq)-2, -1, -1):
            idle_slots -= min(max_val, freq[i])
            
        if idle_slots > 0:
            return idle_slots + len(tasks)
        else:
            return len(tasks)
        