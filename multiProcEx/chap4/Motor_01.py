# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# time 라이브러리 임포트
import time

# 핀 번호 할당 방법은 커넥터 핀 번호로 설정
GPIO.setmode(GPIO.BOARD)

# 사용할 핀 번호 할당
AIN1 = 13
AIN2 = 15
PWMA = 12

# 듀티 비를 변화시킬 스텝 정의
c_step = 10

# 각 핀을 출력 핀으로 설정
GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(PWMA, GPIO.OUT, initial=GPIO.LOW)

# PWM 객체 인스턴스 작성
# 출력 핀: 12번, 주파수 100Hz
p = GPIO.PWM(PWMA, 100)

# PWM 신호 출력
p.start(0)

# 예외 처리
try:
    # 무한 반복
    while 1:
        # AIN1에 하이 레벨 출력
        GPIO.output(AIN1, GPIO.HIGH)
        # 듀티 비를 0부터 100까지 c_step씩 증가
        for pw in range(0, 101, c_step):
            # 펄스 폭을 설정해서 PWM 신호 출력
            p.ChangeDutyCycle(pw)
            # 0.5초 대기
            time.sleep(0.5)
        # 듀티 비를 100부터 0까지 c_step씩 감소
        for pw in range(100, -1, c_step * -1):
            # 펄스 폭을 설정해서 PWM 신호 출력
            p.ChangeDutyCycle(pw)
            # 0.5초 대기
            time.sleep(0.5)
        # AIN1에 로우 레벨 출력
        GPIO.output(AIN1, GPIO.LOW)
        # 0.5초 대기
        time.sleep(0.5)

        # AIN2에 하이 레벨 출력
        GPIO.output(AIN2, GPIO.HIGH)
        # 듀티 비를 0부터 100까지 c_step씩 증가
        for pw in range(0, 101, c_step):
            # 펄스 폭을 설정해서 PWM 신호 출력
            p.ChangeDutyCycle(pw)
            # 0.5초 대기
            time.sleep(0.5)
        # 듀티 비를 100부터 0까지 c_step씩 감소
        for pw in range(100, -1, c_step * -1):
            # 펄스 폭을 설정해서 PWM 신호 출력
            p.ChangeDutyCycle(pw)
            # 0.5초 대기
            time.sleep(0.5)
        # AIN2에 로우 레벨 출력
        GPIO.output(AIN2, GPIO.LOW)
        # 0.5초 대기
        time.sleep(0.5)

# 키보드 예외 검출
except KeyboardInterrupt:
    # 아무것도 하지 않음
    pass

# PWM 정지
p.stop()

# GPIO 개방
GPIO.cleanup()
