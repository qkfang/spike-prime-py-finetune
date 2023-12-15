
from run import Run

model = "lego-v1"
systemPrompt = "You are a lego robot. You can controls your movements and actions by executing python commands. In the answer, you only need to output python code. You can only use this python functions: moveForward(10), moveBackward(10), turnLeft(10), turnRight(10),rotateArmTop(50), await rotateArmFront(50), await stop(), await pause(1000), await detecteObstacle(), await detecteColor()."

caseList = [
    "move forward 19cm and then go back 0.25 meter. ",
    "turn left 45 degrees 3 times, and turn right for half cycle.",
    "spin the top motor for 360 degrees, first clock-wise then anti-clockwise. after that, move front arm for one round.",

    "move around a square, each side of square is 15cm",
    "move forward following a zigzag pattern for 30cm. ",
    "move following a full cycle,  the diameter of the cycle is 15 cm.",

    "do a dance move, only do 20 actions",
    "keep check if there is an obstacle in front of you every 1 second in a loop. if nothing, you can move for 30cm. if there is, make a beep.",
    "check if there is an obstacle in front of you, if nothing, you can move for 30cm. if there is, make a beep."]

# move forward for 100cm. while moving, keep check color every 10ms. if color is red, stop moving.
caseId = ""
while caseId != "exit":
    caseId = input("[Which exercise?]: ")
    print('')

    userPromp = caseList[int(caseId)]
    print(f"Case-{caseId}: {userPromp}")
    input()

    roboConnected = False
    Run(model, systemPrompt, userPromp, roboConnected)

