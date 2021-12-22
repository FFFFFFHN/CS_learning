# 6. 求一个集合中有多少个整数可以表达为该集合中另外两个整数的和。
# 相关说明
# 输入条件 参数 s 是一个整数集合。
# 输出要求 可以表达为该集合中另外两个整数的和的整数个数。
# 其它要求 将代码写入函数 func6。

def fun6(s): # 啥都不想管，直接三个for循环遍历，简洁明了。
    s = set(s)
    s = list(s)
    count = 0
    for i in range(len(s)-2):
        for j in range(i+1,len(s)-1):
            for k in range(j+1,len(s)):
                if s[i] == s[j]+s[k] or s[j] ==s[i]+s[k] or s[k]==s[i]+s[j]:
                    count += 1
    return count

# 7. 给定一个字符串，将字符串正中间的 4 个字符改成“****”。如字符串长度为奇数，
# 则扣除（不是删除）字符串尾部的 1 个字符后确定字符串正中间的位置。
# 相关说明
# 输入条件 参数 s 是一个字符串。
# 输出要求 返回正中间的 4 个字符被改成“****”的字符串。如字符串长度小于 6
# 或大于 10，则返回“****”。
# 其它要求 将代码写入函数 func7。
def fun7(s):
    if len(s)<6 or len(s)>10:
        return '****'
    else:
        return s[:len(s)//2-2]+'****'+s[len(s)//2+2:]
# 8. 已知一个等差数列缺失了一个值，求出这个缺失值。
# 输入条件 参数 lst 是一个未排序整数列表。缺失值一定不在数列的两端。
# 输出要求 返回一个缺失的值，可使得 lst 构成等差数列。如 lst 长度小于 4，则返回 None。
def fun8(lst):
    lst.sort()
    delta = (lst[-1]-lst[0])/(len(lst))
    if len(lst)<4:
        return None
    else:
        for i in range(len(lst)):
            if lst[i] != lst[0] + delta*i:
                return int(lst[0] + delta*i)