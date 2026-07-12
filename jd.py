Python 随机数生成器。
下面给你一个完整、可运行的 Python 程序，支持生成整数、浮点数、随机字符串，并带有输入验证和错误处理。

Pythonimport random
import string

def generate_random_integer(min_val, max_val):
    """生成指定范围的随机整数"""
    if min_val > max_val:
        raise ValueError("最小值不能大于最大值")
    return random.randint(min_val, max_val)

def generate_random_float(min_val, max_val):
    """生成指定范围的随机浮点数"""
    if min_val > max_val:
        raise ValueError("最小值不能大于最大值")
    return random.uniform(min_val, max_val)

def generate_random_string(length):
    """生成指定长度的随机字符串（字母+数字）"""
    if length <= 0:
        raise ValueError("长度必须大于0")
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    try:
        print("=== Python 随机生成器 ===")
        print("1. 随机整数")
        print("2. 随机浮点数")
        print("3. 随机字符串")
        choice = input("请选择功能 (1/2/3): ").strip()

        if choice == "1":
            min_val = int(input("请输入最小整数: "))
            max_val = int(input("请输入最大整数: "))
            print("生成的随机整数:", generate_random_integer(min_val, max_val))

        elif choice == "2":
            min_val = float(input("请输入最小浮点数: "))
            max_val = float(input("请输入最大浮点数: "))
            print("生成的随机浮点数:", generate_random_float(min_val, max_val))

        elif choice == "3":
            length = int(input("请输入字符串长度: "))
            print("生成的随机字符串:", generate_random_string(length))

        else:
            print("无效选择，请输入 1/2/3")

    except ValueError as e:
        print("输入错误:", e)
    except Exception as e:
        print("发生未知错误:", e)


功能说明

随机整数：random.randint(a, b) 生成 [a, b] 范围内的整数
随机浮点数：random.uniform(a, b) 生成 [a, b] 范围内的浮点数
随机字符串：使用 string.ascii_letters + string.digits 生成字母+数字组合


✅ 这个程序可以直接运行，并且会根据你的选择生成不同类型的随机数据。
如果你需要，我还可以帮你升级成 支持权重概率的随机生成器，这样可以按概率生成不同结果。
要我帮你加上这个功能吗？
