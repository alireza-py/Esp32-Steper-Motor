import utime
import _thread
from utils import Robot
from serialuart import SerialConnection

class progress(_thread, Robot):
    def __init__(self) -> None:
        self.connection = SerialConnection(rate= 9600,
                                           txd= 33,
                                           rxd= 32,)
        self.speed = 0
        self.angle = 90
        self.dist = 5
        self.received = ['', False]
        self.start_sign_command = ['#', '*']
        utime.sleep(.1)
        self.connection.send('ready')

    def first(self): # without threading
        command = self.connection.get()
        result = self.command(command)
        self.speed = result[0]
        self.angle = result[1]
        self.dist = result[2]
        

    def secund(self): # threading the main-motor function
        pass

    def command(self, com:str = None):
        result = []
        if not com:
            return None
        if not isinstance(com, str):
            return None
        for out in com:
            if out in self.start_sign_command: 
                self.received[-1] = not self.received[-1]
                result = list(self.received[0])
            if self.received[-1]:
                self.received[0] = self.received[0] + out
        out = []
        if not len(result) % 3 == 0:
            return None
        number = len(result) // 3
        for _ in range(number):
            out.append(int(''.join(map(str, result[:3]))))
            result = result[3:]
        return out 