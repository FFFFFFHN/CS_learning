# 现有列表[35,46,57,13,24,35,99,68,13,79,88,46]，请编写程序将其中重复的元素去除，并
# 按从小到大的顺序排列后输出。
lst = [35, 46, 57, 13, 24, 35, 99, 68, 13, 79, 88, 46]
lst2 = []
for i in lst:
    if i not in lst2:
        lst2.append(i)
lst2.sort()
print(lst2)