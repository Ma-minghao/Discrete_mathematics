aInput = ''  # 输入的命题公式字符串
aHuajian = ''  # 化简后的sInput
va = []  # 保存公式中的变量
xiqu = []  # 主吸取范式最小项
hequ = []  # 主合取范式最大项
fo = ''  # 符号前面的部分
ba = ''  # 符号后的部分


def myinput():  # 输入所求命题式子
    global aInput
    print("请输入一个任意命题公式（'!'表示非，'&'表示合取,'|'表示析取，'>'表示条件,'<'表示双条件，'@'表示异或，可以有括号哦):")
    aInput = input()


def getva():  # 获取其中每一部分
    global aInput, va
    for c in aInput:
        if c >= 'A' and c <= 'Z' or c >= 'a' and c <= 'z':
            if c not in va:
                va.append(c)
            elif c != '!' and c != '&' and c != '|' and c != '(' and c != ')' and c != '>' and c != '<' and c != '@':
                print('输入错误!')
    va = sorted(va)


def getFB(c):
    global aInput, aHuajian, fo, ba
    alen = len(aHuajian)
    for i in range(0, alen):  # 遍历aHuajian中的所有字符
        if aHuajian[i] == c:
            if aHuajian[i - 1] != ')':  # 找到fo
                fo = aHuajian[i - 1]
            else:
                flag = 1
                j = i - 1
                while flag != 0:
                    if aHuajian[j] == '!':
                        j -= 1
                    if aHuajian[j] == '(':
                        flag -= 1
                    if aHuajian[j] == ')':
                        flag += 1
                    j -= 1
                fo = aHuajian[j + 1:i]
            if aHuajian[i + 1] != '(':  # 找到ba
                ba = aHuajian[i + 1]
            else:
                flag = 1
                j = i + 2
                while flag != 0:
                    if aHuajian[j] == '!':
                        j += 1
                    if aHuajian[j] == ')':
                        flag -= 1
                    if aHuajian[j] == '(':
                        flag += 1
                    j += 1
                ba = aHuajian[i + 1:j]
            if c == '>':
                aHuajian = aHuajian.replace(fo + '>' + ba, '(' + '!' + fo + '|' + ba + ')')
            elif c == '<':
                aHuajian = aHuajian.replace(fo + '<' + ba, '(' + fo + '&' + ba + ')|(!' + fo + '&!' + ba + ')')
            elif c == '@':
                aHuajian = aHuajian.replace(fo + '@' + ba,
                                            '!(' + '(' + fo + '&' + ba + ')|(!' + fo + '&!' + ba + ')' + ')')


def huajianinput():
    global aInput, aHuajian
    aHuajian = aInput
    getFB('>')
    getFB('<')
    getFB('@')


def cal():
    global aInput, aHuajian, va, xiqu, hequ, xiqujieguo, hequjieguo
    vlen = len(va)  # 变量个数
    n = 2 ** vlen  # 所有情况个数
    print('真值表如下图所示：')
    print(' '.join(va), aInput + '即', aHuajian)
    for n1 in range(0, n):  # 遍历所有的情况
        value = []  # 数值
        j = n1  # 真值表当前行
        for i in range(0, vlen):  # 遍历所有变量
            value.append(0)
        i = 0
        while j != 0:
            value[i] = j % 2
            j = j // 2
            i += 1
        value.reverse()  # 反转这个列表
        value = list(map(str, value))  # 将value中的数字变成字符形式，此时仍为一个列表
        a = aHuajian  # 将化简后的式子赋值给a
        for x in range(0, vlen):  # 遍历所有变量
            a = a.replace(va[x], value[x])  # 用数字字符代替变量,那样计算机就可以进行计算了。p&q&r这些无法计算但是0&1可以计算
        result = eval(a) & 1  # 将字符变为数字
        if result == 1:
            xiqu.append(n1)
        else:
            hequ.append(n1)
        print(' '.join(value), result)


def outprint():
    print('主析取范式：')
    print(' + '.join([''.join(va[i] if (n>>i)&1 else '!'+va[i] for i in range(len(va))) for n in xiqu]))
    print('主合取范式：')
    print(' * '.join([''.join(va[i] if (n>>i)&1 else '!'+va[i] for i in range(len(va))) for n in hequ]))


def main():
    myinput()
    getva()
    huajianinput()
    cal()
    outprint()


if __name__ == '__main__':
    main()
