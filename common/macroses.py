from time import sleep
from .joys import LeftJoystick, RightJoystick
from vgamepad import VX360Gamepad, XUSB_BUTTON


def bomb_impact(device: VX360Gamepad):
    # Jump
    device.press_button(XUSB_BUTTON.XUSB_GAMEPAD_Y)
    device.update()
    sleep(0.1)
    device.release_button(XUSB_BUTTON.XUSB_GAMEPAD_Y)
    device.update()
    
    # Spawn Round Bomb
    device.press_button(XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    device.update()
    sleep(0.1)
    device.release_button(XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    device.update()

    # Aim with Bow
    device.right_trigger(255)
    device.update()
    sleep(0.1)
    device.right_trigger(0)
    device.update()

    # Switch Square Bomb
    device.press_button(XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    device.update()
    sleep(0.1)

    device.press_button(XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    device.update()
    sleep(0.1)
    device.release_button(XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    device.update()
    sleep(0.1)

    device.release_button(XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    device.update()

    # Spawn Square Bomb
    sleep(0.1)
    device.press_button(XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    device.update()
    sleep(0.1)
    device.release_button(XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    device.update()

    # Switch back to Round Bomb
    device.press_button(XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    device.update()
    sleep(0.1)

    device.press_button(XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    device.update()
    sleep(0.1)

    device.release_button(XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    device.update()
    sleep(0.1)

    device.release_button(XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    device.update()
