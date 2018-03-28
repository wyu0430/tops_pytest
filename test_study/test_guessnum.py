# coding=utf-8

def guess_num(num):

    min_num = 1
    max_num = 99
    guessnum = input('请输入{min_num}到{max_num}之间的数字：'.format(min_num=min_num, max_num=max_num ) )
    if guessnum < min_num or guessnum > max_num:
        return ("数字超过限制")
    else:
        while guessnum != num:
            if guessnum < num:
                min_num = guessnum
                guessnum = input('请输入{min_num}到{max_num}之间的数字：'.format(min_num=min_num, max_num=max_num ) )
            else:
                max_num = guessnum
                guessnum = input('请输入{min_num}到{max_num}之间的数字：'.format(min_num=min_num, max_num=max_num ) )
        return ("真聪明，猜对了!")


def get_BMI():
    height = input("请输入身高：")
    weight = input("请输入体重：")
    bmi = weight / ((height/100.0) ** 2.0)
    if bmi >= 18:

        return '你的BMI是：{}，你丫的太胖了！'.format(bmi)
    else:
        return '你的BMI是：{}，你丫的太瘦了！'.format(bmi)

print get_BMI()
