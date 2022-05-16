import tkinter as tk
import time

# 設定root視窗參數
rootWindows = tk.Tk()
rootWindows.geometry("600x300")
labelDemo = tk.Label

for i in range(1, 10):
    ans = 1 * i
    answer = ("1" + "x" + str(i) + "=" + str(ans))
    print(type(answer), answer)


name: str = "bob"

clock = time.strftime("%Y-%m-%d %H:%M:%S")

print(type(clock))

print("今天我要和" + name + "去吃飯, 我們約晚上" + clock + "點")

# Label放置
labelDemo = tk.Label(rootWindows, text=answer)
labelDemo.pack()


rootWindows.mainloop()
