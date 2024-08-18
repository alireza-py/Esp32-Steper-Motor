import utime
from machine import Pin


class BaseConfigMotors:
    # the stepper pins
    main_stepper = [
        Pin(12, Pin.OUT),
        Pin(13, Pin.OUT),
        Pin(14, Pin.OUT),
        Pin(15, Pin.OUT),
    ]
    # the sequence of steps for the motor
    main_step_sequence = [
        [1, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
    ]
    # the stepper pins
    wheel_stepper = [
        Pin(12, Pin.OUT),
        Pin(13, Pin.OUT),
        Pin(14, Pin.OUT),
        Pin(15, Pin.OUT),
    ]
    # the sequence of steps for the motor
    wheel_step_sequence = [
        [1, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
    ]


class Robot:
    def __init__(self) -> None:
        self.moving_step_index = 0
        self.wheel_step_index = 0

    def moving_step(self, direction, steps, delay):
        for _ in range(steps):
            self.moving_step_index = (self.moving_step_index + direction) % len(
                BaseConfigMotors.main_step_sequence
            )
            for pin_index in range(len(BaseConfigMotors.main_stepper)):
                pin_value = BaseConfigMotors.main_step_sequence[self.moving_step_index][
                    pin_index
                ]
                BaseConfigMotors.main_stepper[pin_index].value(pin_value)
            utime.sleep(delay)

    def wheel_step(self, direction, steps, delay):
        for _ in range(steps):
            self.wheel_step_index = (self.wheel_step_index + direction) % len(
                BaseConfigMotors.wheel_step_sequence
            )
            for pin_index in range(len(BaseConfigMotors.wheel_stepper)):
                pin_value = BaseConfigMotors.wheel_step_sequence[self.wheel_step_index][
                    pin_index
                ]
                BaseConfigMotors.wheel_stepper[pin_index].value(pin_value)
            utime.sleep(delay)

    def sharp(self, id:int):
        return