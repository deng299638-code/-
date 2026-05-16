import re
from datetime import datetime


def reg_search(text: str, regex_list: list) -> list:
    result = []
    for regex_dict in regex_list:
        match_result = {}
        for field_name, pattern in regex_dict.items():
            matches = re.findall(pattern, text, re.DOTALL | re.MULTILINE)
            if not matches:
                continue
            cleaned_matches = [m.strip() for m in matches if m.strip()]
            match_result[field_name] = cleaned_matches[0]
        result.append(match_result)
    return result

if __name__ == "__main__":
    # 待匹配文本
    text = """
    标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份
    有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债
    券。
    换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束
    之日满 12 个月后的第一个交易日起至可交换债券到期日止，即 2023 年 6 月 2
    日至 2027 年 6 月 1 日止。
    """

    # 正则配置：自定义正则表达式
    regex_list = [{
        # 匹配股票代码：6位数字.SH/SZ
        '标的证券': r'股票代码：([\d]+\.[A-Z]+)',
        # 匹配年月日：YYYY 年 m 月 d 日
        '换股期限': r'(\d{4} 年 \d{1,2} 月 \d{1,2} 日)'
    }]

    # 调用函数
    result = reg_search(text, regex_list)

    # 打印结果
    print( result)
