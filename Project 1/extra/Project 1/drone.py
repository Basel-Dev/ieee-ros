from enum import Enum

class DroneStatus(Enum):
    IDLE = "IDLE"
    RETURNING = "RETURNING"
    DELIVERING = "DELIVERING"


class Drone:
    def __init__(self, drone_id, max_weight):
        self.id = drone_id
        self.max_weight = max_weight
        self.battery = 100
        self.position = (0, 0)
        self.status = DroneStatus.IDLE

    def set_status(self, status):
        if isinstance(status, DroneStatus):
            self.status = status

    def consume_battery(self, amount):
        self.battery = max(0, self.battery - amount)

    def __str__(self):
        return f"{self.id} | {self.status.value} | {self.battery}% | {self.position}"