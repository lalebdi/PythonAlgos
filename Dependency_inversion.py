from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class LightBulb(Switchable):  # LightBulb implements the interface of Switchable
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned of...")


class Fan(Switchable): # Fan implements the interface of Switchable
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")


class ElectricPowerSwitch:  # Dependency Inversion is happening here
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False

        else:
            self.client.turn_on()
            self.on = True



l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()

f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()

"""
Instead of have coupled classes, use Dependency Inversion instead to decouple them
"""