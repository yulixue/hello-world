# 定义函数countchar()按字母表顺序统计字符串中所有出现的字母的个数
# input: Hello, World!
# output: [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 3, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
import time
def countchar(string):
    string = string.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    a_list = []
    for i in range(len(alphabet)):
        if alphabet[i] in string:
            a_list.append(string.count(alphabet[i]))
        else:
            a_list.append(0)
    return a_list

if __name__ == "__main__":
    string = input('Enter some strings:')
    start = time.perf_counter()
    print(countchar(string), time.perf_counter()-start)
