'''
假设某大学的成绩绩点计算规则为：90分(含)以上计4.5分，80分(含)-90分（不含）计3分，70分(含)-80分（不含）计1.5分，60分(含)-70分（不含）计1分,60分以下不计分。输入某位同学的各门课成绩，请编写一个函数，打印该同学的平均绩点（保留2位小数）。
函数接口定义：
函数接口描述：
GPA(参数...)
裁判测试程序样例：
lst=list(map(eval,input().split()))
GPA(*lst)
输入样例1：在这里给出一组输入。例如：
90 95 87
输出样例1：在这里给出相应的输出。例如：
4.00
输入样例2：在这里给出一组输入。例如：
60 73 88 59
输出样例2：在这里给出相应的输出。例如：
1.38
'''
def GPA(*lst):
    gpa = 0
    for i in range(len(lst)):
        m = lst[i] // 10
        if m >= 9:
            gpa += 4.5
        elif 9 > m >= 8:
            gpa += 3
        elif 8 > m >= 7:
            gpa += 1.5
        elif 7 > m >= 6:
            gpa += 1
        else:
            gpa += 0
    print("{:.2f}".format(gpa/len(lst)))