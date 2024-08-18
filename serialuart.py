from machine import UART


class SerialConnection:
    def __init__(self, rate:int = 9600, txd:int = 33, rxd:int = 32,
                        bits = 8, parity = None, stop = 1) -> None:
        self.connection =  UART(1, baudrate= rate, tx= txd, rx= rxd, 
                                bits= bits, parity= parity, stop= stop)

    def send(self, command:any):
        command = str(command)
        self.connection.write(command)
        
    def get(self, spacereading:int = 11) -> str:    
        buffer = self.connection.read(spacereading)
        result = buffer.decode("utf-8")
        return result