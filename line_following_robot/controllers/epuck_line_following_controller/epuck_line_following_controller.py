# Import Motor class
from controller import Robot, DistanceSensor, Motor

TIME_STEP = 64
MAX_SPEED = 1.00

# create the Robot instance.
robot = Robot()

# initialize devices
gs = []
gsNames = ['gs0', 'gs1', 'gs2']

for i in range(3):
    gs.append(robot.getDevice(gsNames[i]))
    gs[i].enable(TIME_STEP)

# initializing the motors
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

while robot.step(TIME_STEP) != -1:
    # read sensors outputs
    gsValues = []
    for i in range(3):
        gsValues.append(gs[i].getValue())
    
    print(gsValues)  # Indentation corrected

    leftSensorVal = gsValues[0]
    middleSensorVal = gsValues[1]
    rightSensorVal = gsValues[2]
    
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
