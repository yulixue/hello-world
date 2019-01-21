# 如果一个n位数刚好包含了1至n中所有数字各一次则称它们是全数字的，例如四位数1324就是1至4全数字的。
# 从键盘上输入一组整数，输出其中的全数字，若找不到则输出“not found”。
# input: 1243,322,321,1212,2354
# output: 1243\n321

def pandigital(nums):
    plst = []
    for num in nums:
        flag = True
        for i in range(1, len(str(num))+1):
            if str(i) in str(num):
                continue
            else:
                flag = False
                break
        if flag == True:
            plst.append(num)
    return plst

if __name__ == "__main__":
    lst = pandigital(eval(input('Please enter a group of int:')))
    if len(lst) != 0:
        for i in range(len(lst)):
            print(lst[i])
    else:
        print("not found")
