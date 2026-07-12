import os
import random

def generate_random_script():
    templates = [
        # 模板 1：随机密码生成器
        """import random
import string

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print(f"随机生成密码: {generate_password()}")
""",
        # 模板 2：简易计算器
        """def calculator():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(['+', '-', '*', '/'])
    
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    else:
        result = num1 / num2 if num2 != 0 else 'N/A'
        
    print(f"{num1} {op} {num2} = {result}")

if __name__ == "__main__":
    calculator()
""",
        # 模板 3：简单的猜数字游戏
        """import random

def guess_number():
    secret = random.randint(1, 10)
    guess = random.randint(1, 10)
    print(f"随机猜数字：目标是 {secret}，猜测是 {guess}")
    if guess == secret:
        print("猜对了！")
    else:
        print("猜错了，再接再厉！")

if __name__ == "__main__":
    guess_number()
"""
    ]
    
    # 随机选择一个模板并保存
    code = random.choice(templates)
    filename = f"random_script_{random.randint(1000, 9999)}.py"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
        
    print(f"成功生成随机代码文件：{filename}")
    print("-" * 30)
    print("代码内容：")
    print(code)
    print("-" * 30)

if __name__ == "__main__":
    generate_random_script()
