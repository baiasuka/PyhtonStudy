import random
from datetime import datetime, timedelta


def birthday_check(birthday):
    """
    性别为女+生日/星座/年龄为注册当天出现的系统默认值（23年前），上报预警
    :param birthday:
    :return:
    """
    cur_time = datetime.now()
    default_year = cur_time.year - 23
    default_month = cur_time.month
    default_day = cur_time.day
    birthday_arry = birthday.split('-')
    if int(birthday_arry[0]) == default_year and int(birthday_arry[1]) == default_month \
            and int(birthday_arry[2]) == default_day:
        return True
    else:
        return False

if __name__ == '__main__':
    print(birthday_check('1998-09-01'))