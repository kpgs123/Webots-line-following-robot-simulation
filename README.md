# Webots-line-following-robot-simulation
Webots line following simulation using epuck robot and it's 3 infrared distance sensors mounted on ground plate of the robot.
Used python robot controller for this.

Any one can add new tracks if needed by changing "RectangleArena->floorAppearance-PBRAppearance->BaseColorMap-ImageTexture->url" picture.

![Screenshot from 2024-01-04 14-35-44](https://github.com/kpgs123/Webots-line-following-robot-simulation/assets/56798215/5419e40c-ebee-471d-a9b6-ccba2946b3ff)

Controller logic - 

```python
    if leftSensorVal > 400 and middleSensorVal > 400 and rightSensorVal > 400:
        leftMotor.setVelocity(-MAX_SPEED)
        rightMotor.setVelocity(-MAX_SPEED)
    elif leftSensorVal > 400:
        if middleSensorVal > 400:
            leftMotor.setVelocity(MAX_SPEED)
            rightMotor.setVelocity(0.50 * MAX_SPEED)
        else:
            leftMotor.setVelocity(0.75 * MAX_SPEED)
            rightMotor.setVelocity(0.50 * MAX_SPEED)
    elif rightSensorVal > 400:
        if middleSensorVal > 400:
            leftMotor.setVelocity(0.50 * MAX_SPEED)
            rightMotor.setVelocity(MAX_SPEED)
        else:
            leftMotor.setVelocity(0.50 * MAX_SPEED)
            rightMotor.setVelocity(0.75 * MAX_SPEED)
    else:
        leftMotor.setVelocity(0.50 * MAX_SPEED)
        rightMotor.setVelocity(0.50 * MAX_SPEED)
```
<br>

Track 1 -
<br>


https://github.com/kpgs123/Webots-line-following-robot-simulation/assets/56798215/acec9936-f78e-4fe2-b31a-3119cacae345


<br><br>
Track 2 - 
<br>

https://github.com/kpgs123/Webots-line-following-robot-simulation/assets/56798215/6b6a5121-b080-4704-af90-4917587ea516



<br><br>
Track 3 - 
<br>


https://github.com/kpgs123/Webots-line-following-robot-simulation/assets/56798215/4b5d685c-1296-4010-98f8-a62348ea577c


<br><br>
