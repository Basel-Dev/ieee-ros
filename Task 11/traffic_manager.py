from dataclasses import dataclass
import math

@dataclass
class RobotState:
    x: float | None
    y: float | None
    theta: float | None
    priority: int | None

@dataclass
class Decision:
    status: str
    robot_id: int


SAFE_DISTANCE = 5

def getDistance(x1, x2, y1, y2):
    return math.sqrt( ((x2 - x1)**2) + ((y2 - y1)**2) )

def checkIfNoneState(state: RobotState):
    return ( state.x is None or state.y is None or state.theta is None or state.priority is None)

def evaluate_traffic(self_state: RobotState, fleet_view: dict):
    ## Yielding Protocol

    decisionsList = []
    for robot_id, robot_state in fleet_view.items():
            if checkIfNoneState(robot_state):
                fleet_view_none = True
                continue ## Potential warn after a few tries so that a robot wouldn't be ignored

            distance = getDistance(self_state.x, robot_state.x, self_state.y, robot_state.y)
            self_priority = self_state.priority
            robot_priority = robot_state.priority

            if distance < SAFE_DISTANCE:
                if robot_priority > self_priority:
                    decisionsList.append(Decision("YIELD", robot_id))
                elif robot_priority == self_priority:
                    ## Multiple ways to resolve this conflict just logging in general
                    decisionsList.append(Decision("DANGER_EQUAL", robot_id))
                elif robot_priority < self_priority:
                    decisionsList.append(Decision("PROCEED_LOWER", robot_id))
            
    return decisionsList
