import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN)
# Motor pins
motor_in1 = 23
motor_in2 = 24
motor_en = 25
GPIO.setup(motor_in1, GPIO.OUT)
GPIO.setup(motor_in2, GPIO.OUT)
GPIO.setup(motor_en, GPIO.OUT)
# Setup PWM pin for motor speed control
motor_pwm = GPIO.PWM(motor_en, 100)
motor_pwm.start(0)
# Main program loop
while True:
    value = int(GPIO.input(18))
    print(value)
    # Set motor direction and speed
    if value == 1:
        GPIO.output(motor_in1, GPIO.HIGH)
        GPIO.output(motor_in2, GPIO.LOW)
        motor_pwm.ChangeDutyCycle(50)
    else:
        GPIO.output(motor_in1, GPIO.LOW)
        GPIO.output(motor_in2, GPIO.LOW)
        motor_pwm.stop()
        motor_pwm.start(0)
    time.sleep(1)
GPIO.cleanup()
