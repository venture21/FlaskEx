# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# Tkinter 라이브러리 임포트
import tkinter as tk # Python3
#import Tkinter as tk # Python2

# 핀 번호 할당 방법은 커넥터 핀 번호로 설정
GPIO.setmode(GPIO.BOARD)

# 핀 번호 할당
SRV = 12

# 출력 핀으로 설정
GPIO.setup(SRV, GPIO.OUT)

# 주파수 설정
freq = 100.0
# 각도의 최솟값 설정
deg_min = 0.0
# 각도의 최댓값 설정
deg_max = 180.0
# PWM 신호 최소 듀티 설정
dc_min = 5.0
# PWM 신호 최대 듀티 설정
dc_max = 22.0

# PWM 객체 인스턴스 생성
# 출력 핀: SRV, 주파수: freq
p = GPIO.PWM(SRV, freq)

# PWM 신호 출력
p.start(0)

# Tk 객체 인스턴스 작성
root = tk.Tk()

# Variable 객체 인스턴스를 부동소수형으로 작성
deg = tk.DoubleVar()
# 0을 설정
deg.set(0)

# 각도를 듀티 비로 환산해서 서보 모터를 회전시킴
def change_dc(dum):
    # 듀티 비를 변경
    dc = (deg.get() - deg_min) * (dc_max - dc_min) / (deg_max - deg_min) + dc_min
    p.ChangeDutyCycle( dc )

# 각도를 조절하는 슬라이드 바 작성
# 라벨 Angle, 수평, 숫자 범위는 0~180
s = tk.Scale(root, label = 'Angle', orient = 'h',\
from_ = 0, to = 180, variable = deg, command = change_dc)
# 슬라이드 바 배치
s.pack()

# root 표시
root.mainloop()

# PWM 정지
p.stop()

# GPIO 개방
GPIO.cleanup()
