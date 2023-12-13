# 1. 윈도우 만들기
import tkinter as tk
root = tk.Tk() #윈도우를 만든다
#root.mainloop() #윈도우를 표시한다
# 2. 윈도 위에 캔버스 만들기
# Canvas 메소드 : 도형이나 이미지를 그리는 구조
canvas =tk.Canvas(root, width =600, height
=400, bg="white")
# 3. 캔버스의 위치 결정 : 윈도 윈에 같은 크기의캔버스가 겹치도록 세팅
canvas.place(x = 0, y = 0)
#중심 [(300,200), 반경 20]의 원 그리기
canvas.create_oval(300 - 20, 200 - 20, 300 + 20, 200 + 20)

# 4. 원을 그리기 - [creat_oval]이라는 메서드를사용. 처음 2개는 위 좌표, 그 다음 2개는 오른쪽아래 좌표
#중심 [(300,200), 반경 20]의 원 그리기
canvas.create_oval(300 - 20, 200 - 20, 300 + 20, 200 + 20)
# 5. 원의 색깔을 바꾸기 - 옵션값 설정
# width : 선의 폭
# outline : 선의 색
# fill : 칠하는 색
#빨간원 만들기(선없음)
canvas.create_oval(300 - 20, 200 - 20, 300 + 20, 200 + 20,fill="red", width=0)

canvas.pack()
root.mainloop ()