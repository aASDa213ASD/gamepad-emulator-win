from pynput import mouse, keyboard
from threading import Thread
from time import sleep
import vgamepad as vg
from common.macroses import bomb_impact
from common.joys import (
    LeftJoystick,
    RightJoystick
)


class Gamepad:
    def __init__(self):
        print(f"[Gamepad] Arming conditions ...")

        self.pause:   bool  = True
        self.left_joystick  = LeftJoystick()
        self.right_joystick = RightJoystick()

        self.create()
        self.hook()
    
    def _send(self, gamepad_button, is_pressed):
        if is_pressed:
            self.device.press_button(button=gamepad_button)
        else:
            self.device.release_button(button=gamepad_button)
    
    def _on_mouse_move(self, x, y):
        if self.pause: return
        
        self.right_joystick.set(x, y)
        self.device.right_joystick(
            self.right_joystick.x,
            self.right_joystick.y
        )
        self.device.update()
    
    def _on_mouse_click(self, x, y, button, is_pressed):
        if self.pause: return

        try:
            button_name = button.char
        except AttributeError:
            button_name = button.name

        if (button_name == "left"):
            self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_X, is_pressed)
        elif (button_name == "right"):
            value = 255 if is_pressed else 0
            self.device.left_trigger(value)
        elif (button_name == "middle"):
            value = 255 if is_pressed else 0
            self.device.right_trigger(value)
            self.right_joystick.calibrate(x, y)
        elif (button_name == "x1"):
            self.right_joystick.calibrate(x, y)
            self.device.reset()
        
        self.device.update()

    def _on_key(self, key, is_pressed):
        try:
            key_name = str(key.char).lower()
        except AttributeError:
            key_name = str(key.name).lower()
        
        if (key_name == "caps_lock" and is_pressed):
            self.pause = not self.pause
        
        if self.pause: return

        match(key_name):
            case "w":
                self.left_joystick.set('y', True)  if is_pressed else self.left_joystick.unset('y')
            case "s":
                self.left_joystick.set('y', False) if is_pressed else self.left_joystick.unset('y')
            case "d":
                self.left_joystick.set('x', True)  if is_pressed else self.left_joystick.unset('x')
            case "a":
                self.left_joystick.set('x', False) if is_pressed else self.left_joystick.unset('x')
            case "e":
                self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_B, is_pressed)
            case "shift":
                self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_A, is_pressed)
            case "space":
                self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y, is_pressed)
            case "alt_l":
                self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_START, is_pressed)
            case "ctrl_l":
                self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB, is_pressed)
            case "ctrl_r":
                self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB, is_pressed)
            case "m":
                self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK, is_pressed)
            case "q":
                self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER, is_pressed)
            case "r":
                self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER, is_pressed)
            case "z":
                self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP, is_pressed)
            case "x":
                self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN, is_pressed)
            case "c":
                self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT, is_pressed)
            case "v":
                self._send(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT, is_pressed)
            case "shift_r":
                if is_pressed:
                    self.left_joystick.half_mode = not self.left_joystick.half_mode
            case "t":
                if is_pressed:
                    bomb_impact(self.device)
            case _:
                pass
        
        if (key_name in ['a', 'w', 's', 'd']):
            self.device.left_joystick(
                self.left_joystick.x,
                self.left_joystick.y
            )
        
        self.device.update()
    
    def create(self):
        print(f"[Gamepad] Creating an instance ...")
        self.device = vg.VX360Gamepad()
    
    def destroy(self):
        print(f"[Gamepad] Destroying existing instances ...")
        del self.device
    
    def hook(self):
        print(f"[Gamepad] Hooking pereferals ...")
        
        self.mouse = mouse.Listener(
            on_move  = self._on_mouse_move,
            on_click = self._on_mouse_click
        )

        self.keyboard = keyboard.Listener(
            on_press   = lambda key: self._on_key(key, True),
            on_release = lambda key: self._on_key(key, False)
        )

        Thread(target=self.mouse.start).start()
        Thread(target=self.keyboard.start).start()

    def run(self):
        print(f"[Gamepad] Up and running.")
        try:
            while True:
                sleep(60)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    gamepad = Gamepad()
    gamepad.run()
