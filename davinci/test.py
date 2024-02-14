#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://oai-north-22.openai.azure.com/"
openai.api_version = "2023-09-15-preview"
openai.api_key = "b8fef4ce72a84e0999a26295ec3412d7"

response = openai.Completion.create(
  engine="davinci-002-a",
  prompt="Learn from below robot commands in python and write a python program to move robot back and forth 10 cm.\n\n\n# python function signature to move robot forward. first parameter is distance in cm. second parameter is speed that could be Slow or Fast.\nmove(targetDistance, speed=Speed.Slow)\n# command block to move robot forward 10 cm.\nawait move(10, Speed.Slow)\n# command block to move robot backward 10 cm.\nawait move(-10, Speed.Slow)\n# python function signature to turn robot to its left. first parameter is degrees to turn, positive value turns right, negative value turns left. second parameter is speed that could be Slow or Fast.\nturn(targetTurnDegree, speed=Speed.Slow)\n# command block to turn robot to left 10 degrees.\nawait turn(-10, Speed.Slow)\n# command block to turn robot to right 10 degrees.\nawait turn(10, Speed.Slow)\n# python function signature to rotote robot's top motor. first parameter is degrees to rotate, positive value rotates clockwise, negative value rotates anti-clockwise.\nawait rotateTop(targetDegree)\n# command block to rotate robot's motor on the top clockwise 100 degrees.\nawait rotateTop(100)\n# command block to rotate robot's motor on the top anti-clockwise 100 degrees.\nawait rotateTop(-100)\n# python function signature to rotote robot's front motor. first parameter is degrees to rotate, positive value rotates clockwise, negative value rotates anti-clockwise.\nawait rotateFront(targetDegree)\n# command block to rotate robot's motor in the front clockwise 100 degrees.\nawait rotateFront(100)\n# command block to rotate robot's motor in the front anti-clockwise 100 degrees.\nawait rotateFront(-100)\n# command block to stop robot's movement\nmotor_pair.stop(motor_pair.PAIR_1, stop = motor.BRAKE)\n# command block to delay timer for 1 second\ntime.sleep_ms(1000)\n# python program's main function to control the robot should be wrapped in main() function. then python commonds to control robot are inside main function.\nasync def main(): \n    #python commands here\n# python program to make robot move forward 19cm and then move backward 10cm.\nasync def main(): \n    await move(19)\n    await move(-1)\n	\n	\n	\npathon program here:\n\n	\n",
  temperature=0,
  max_tokens=250,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  best_of=4,
  stop=None)


print(response)
print(response['choices'][0]['text'])