import tkinter as tk
# 원의 좌표와 반경
x = 400
y = 300
# 이동양
dx = 1
dy = 1
def move():
 global x, y, dx, dy
 # 지금 원을 지운다
 canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="white",
width=0)
 # X좌표를 움직인다
 x = x + dx
 # Y좌표를 움직인다
 y = y + dy
 # 다음 위치에 원을 그린다
 canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="red", width=0)
 # 끝을 넘으면 반대방향으로 한다
 if x >= canvas.winfo_width():
    dx = -1
 if x <= 0:
    dx = +1
 # Y좌표에 대해서도 마찬가지
 if y >= canvas.winfo_height():
    dy = -1
 if y <= 0:
    dy = +1
 # 다시 타이머
 root.after(10, move)
# 윈도우를 그린다
root = tk.Tk()
root.geometry("600x400")
# 캔버스를 놓는다
canvas =tk.Canvas(root, width =600, height
=400, bg="white")
canvas.place(x = 0, y = 0)
# 타이머를 설정한다
root.after(10, move)
root.mainloop()