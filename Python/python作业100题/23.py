# 已知一个整数列表，判断列表内容是否为回文，即无论正序还是倒序，列表的内容是否
# 相同
lst = [1,2,3,4,5,4,3,2,1]
if lst == lst[::-1]:
    print('是回文')
else:
    print('不是回文')