import time
import keyboard
import pyperclip

def paste_plain_text():
    time.sleep(0.05)
    text = pyperclip.paste()
    keyboard.write(text)  # 使用keyboard模拟键盘输入实现粘贴
    print("已粘贴纯文本:", text)

def main():
    print("程序已启动。")
    print("每次按下 Ctrl+V 将进行纯文本粘贴。")
    print("按 ESC 键退出程序。")
    keyboard.add_hotkey('ctrl+v', paste_plain_text, suppress=True)
    keyboard.wait('esc')
    print("程序已退出。")

if __name__ == '__main__':
    main()