import string
import random

letters = string.ascii_letters + string.digits
long_short = {}
short_long = {}

class Codec:
    '''
    如何设计短URL? 如何设计一个hash function? 可以用26个字母大小写52个加上数字10个一共62个字符，
    在从中随机选取6个字符 作为网站的后缀，棒棒哒。
    
    '''


    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        # 随机选取六个字符作为后缀
        def hashURL():
            code = ''
            tmp = ''
            for i in range(6):
                tmp = letters[random.randint(0, 10000) % 62]
                code = code + tmp
            return code
        
        prefix = "http://tinyurl.com/"
        # 如果已经存在了，直接返回
        if longUrl in long_short:
            return prefix + long_short[longUrl]
        else:
            suffix = hashURL()
            long_short[longUrl] = suffix
            short_long[suffix] = longUrl
            return prefix + suffix
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        # 把短变长，在字典里找到相应的 后缀，返回长网址
        shortUrl = shortUrl.split('/')[-1]
        if shortUrl in short_long:
            return short_long[shortUrl]
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))