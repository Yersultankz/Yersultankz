import re

def extract_phone_numbers(text):
    # 提取以 + 开头或以数字开头的常见国际号码格式
    pattern = r'\+?\d{10,15}'
    return re.findall(pattern, text)

if __name__ == "__main__":
    sample_text = """
    联系方式如下：
    - WhatsApp: +77011234567
    - 手机：87011234567
    - 备用：+998901234567
    """
    numbers = extract_phone_numbers(sample_text)
    print("提取到的号码：")
    for number in numbers:
        print(number)
