import sys
import os

# 将models目录添加到sys.path中
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

from helper import greet
from calculator import add

def main():
    # 调用utils目录下的helper模块
    greet("Alice")
    
    # 调用models目录下的calculator模块
    result = add(3, 5)
    print(f"3 + 5 = {result}")

if __name__ == "__main__":
    main()