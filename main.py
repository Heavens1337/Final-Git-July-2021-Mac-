import robot
r = robot.RobotController()
r.connect()

r.forward(350)
r.left(130)

r.read_marker()

marker_check = r.read_marker()
print(marker_check)

if marker_check == 1:
    r.backward(50)
    r.left(650)
    r.forward(100)
    #do scans and stuff here
    r.backward(100)
    r.right(650)
    r.forward(50)
    r.right(50)

else:
    r.right(50)

r.forward(550)
r.left(50)

r.read_marker()

marker_check = r.read_marker()
print(marker_check)

if marker_check == 1:
    r.backward(50)
    r.left(600)
    r.forward(200)
    # do scans and stuff here
    r.backward(200)
    r.right(600)
    r.forward(50)
    r.right(50)

else:
    r.right(50)