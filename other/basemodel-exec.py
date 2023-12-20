from gpt import chat

model = "gpt-35"
systemPromp = "You are a lego robot. You can controls your movements and actions by executing python commands. In the answer, you only need to output python code. You can only use this python functions: moveForward(10), moveBackward(10), turnLeft(10), turnRight(10), rotateArmTop(50), rotateArmFront(50), stop(), pause(1000), detecteObstacle(), detecteColor(), display(text), beep(), face(text)."

test1 = "you move forward 19cm and then move backward 10cm. "
test2 = "you turn left 90 degrees and stop."
test3 = "you turn right 180 degrees very fast and stop."
test5 = "you move around a triangle obstacle that each side is 10cm, then stop. "
test6 = "you move forward 20cm very fast."
test7 = "you move forward following a zigzag pattern for 100cm. "
test8 = "you move forward 20cm and pass a small obstacle in the way. "
test9 = "you move forward 50 cm, but there is a medium obstacle in front of you."
test10 = "you move forward 50 cm, but there is a large sink hole in front of you. the sink hole is about 20cm in size."

chat(model, systemPromp, test1)
# chat(model, systemPromp, test2)
# chat(model, systemPromp, test3)
# # chat(model, systemPromp, test4)
# chat(model, systemPromp, test5)
# chat(model, systemPromp, test6)
# chat(model, systemPromp, test7)
# chat(model, systemPromp, test8)
# chat(model, systemPromp, test10)
