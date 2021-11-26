import re

def check_words(words=None):
    """
    中文、英文字母、
    :param words:
    :return:
    """
    pattern = re.compile(r'[^\u4e00-\u9fa5\u0041-\u005A\u0061-\u007A]+')

    r = pattern.findall('+-asdbSBd雲中君123')
    print(r)


def check_emoji():
    pattern = re.compile(r'['u'\U0001F300-\U0001F64F'u'\U0001F680-\U0001F6FF'u'\u2600-\u2B55]')
    r = pattern.findall('😜😏😍🤭')
    print(r)

if __name__ == '__main__':
    # check_emoji()
    print(hex(ord('3')))
    # print('\U0001f92d')
    # for i in range(int('2600', 16), int('2B55', 16)):
    #     print(i, chr(i))