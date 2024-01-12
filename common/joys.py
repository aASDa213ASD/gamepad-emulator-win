class Joystick:
    def __init__(self):
        self.x:         int = 0
        self.y:         int = 0
        self.min_limit: int = -32768
        self.max_limit: int = 32767


class LeftJoystick(Joystick):
    def __init__(self):
        super().__init__()
        self.half_mode: bool = False

    def set(self, axis: str, positive: bool):
        value: int = 0
        
        if positive:
            value = self.max_limit if not self.half_mode else int((self.max_limit / 2))
        else:
            value = self.min_limit if not self.half_mode else int((self.min_limit / 2))
        
        if (axis == 'x'):
            self.x = value
        else:
            self.y = value

    def unset(self, axis: str):
        if axis == 'x':
            self.x = 0
        else:
            self.y = 0


class RightJoystick(Joystick):
    def __init__(self):
        super().__init__()
        self.sensitivity: int = 100
        self.origin_x:    int = 0
        self.origin_y:    int = 0
    
    def _get_rel(self, x, y) -> tuple:
        rel_x = (x - self.origin_x) * self.sensitivity
        rel_y = (y - self.origin_y) * self.sensitivity
        rel_y *= -1

        rel_x = max(self.min_limit, min(self.max_limit, rel_x))
        rel_y = max(self.min_limit, min(self.max_limit, rel_y))

        return (rel_x, rel_y)

    def set(self, x: int, y: int):
        coordinates = self._get_rel(x, y)
        self.x = coordinates[0]
        self.y = coordinates[1]

    def calibrate(self, x, y):
        self.origin_x = x
        self.origin_y = y
        self.x = 0
        self.y = 0
