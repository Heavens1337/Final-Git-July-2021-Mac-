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

r.forward(450)
r.rotate_counterclockwise(90)
r.forward(1630)

r.read_marker()

marker_check = r.read_marker()
print(marker_check)

if marker_check == 1:
    r.left(200)
    #temp scan here
    r.right(200)

r.right(50)

r.forward(550)
r.rotate_counterclockwise(90)
r.forward(900)
r.left(710)
r.forward(780)

r.read_marker()

marker_check = r.read_marker()
print(marker_check)

if marker_check == 1:
    r.right(10)
    r.forward(350)
    r.left(550)
    #temp scan here
    r.right(550)
    r.backward(350)

r.left(1000)
r.forward(100)
r.left(500)


r.read_marker()

marker_check = r.read_marker()
print(marker_check)

if marker_check == 1:
    r.right(100)
    r.forward(350)
    r.left(450)
    #scan here
    r.right(450)
    r.backward(350)
