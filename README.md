# Webots-line-following-robot-simulation
Webots line following simulation using epuck robot and it's 3 infrared distance sensors mounted on ground plate of the robot.
Used python robot controller for this.

Any one can add new tracks if needed by changing "RectangleArena->flooarAppearance-PBRAppearance->BaseColorMap-ImageTexture->url" picture.

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
https://github.com/kpgs123/Webots-line-following-robot-simulation/assets/56798215/4c27b21b-d0e8-4863-8cb3-21c82e55b3f5
Track 2 - 
https://github.com/kpgs123/Webots-line-following-robot-simulation/assets/56798215/ffd5fee7-1a15-4987-aee4-025c39a3b5b1
Track 3 -
https://github.com/kpgs123/Webots-line-following-robot-simulation/assets/56798215/74f5ed67-ec3a-4ff4-a4ed-923f8cc5fec7
