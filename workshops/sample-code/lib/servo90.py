"""
servo90.py - class Servo90
"""
import machine

class Servo90:

    def __init__(self):
        self.pwm = machine.PWM(0, frequency=50)
        self.pwm_c = self.pwm.channel(0, pin='P9', duty_cycle=0.075)

    def rotate(self, status):
        self.status = status
        self.duty_cycleDictionarie = {36: 0.01, 72: 0.05, 108:0.075, 154:0.1, 180:0.15}
        for rotation in self.duty_cycleDictionarie:
            if(self.status == rotation):
                self.pwm_c.duty_cycle(self.duty_cycleDictionarie[rotation])
                return


# test deze module als je in Atom/Pymakr op knop 'run' klikt
if __name__ == '__main__':
    servo = Servo90()
    print('rotate servo 36...')
    servo.rotate(36)
