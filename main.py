import robot
import matplotlib.pyplot as plt
r = robot.RobotController()
r.connect()

temperature_list = [r.take_temperature()]

r.forward(350)
r.left(130)

print(r.read_marker())

if r.read_marker() == 1:
    r.backward(50)
    r.left(650)
    r.forward(100)
    temperature_list.append(r.take_temperature())
    print(r.scan_for_people())

    if r.scan_for_people() is True:
        r.rescue_person()
        r.backward(100)
        r.right(800)
        r.backward(400)
        r.forward(450)
        r.left(150)

    else:
        r.backward(100)
        r.right(650)
        r.forward(50)

r.right(50)

r.forward(550)
r.left(50)

print(r.read_marker())

if r.read_marker() == 1:
    r.backward(50)
    r.left(600)
    r.forward(200)
    if r.scan_for_fire() is True:
        for i in range(30):
            r.extinguish_fire()
    temperature_list.append(r.take_temperature())
    r.backward(200)
    r.right(600)
    r.forward(50)


r.right(50)
r.forward(450)
r.rotate_counterclockwise(90)
r.forward(1630)


print(r.read_marker())

if r.read_marker() == 1:
    r.left(200)
    temperature_list.append(r.take_temperature())
    r.right(200)

r.right(50)
r.forward(550)
r.rotate_counterclockwise(90)
r.forward(900)
r.left(710)
r.forward(780)

print(r.read_marker())

if r.read_marker() == 1:
    r.right(10)
    r.forward(350)
    r.left(550)
    if r.scan_for_fire() is True:
        for i in range(3):
            r.extinguish_fire()
    temperature_list.append(r.take_temperature())
    r.right(550)
    r.backward(350)

r.left(1000)
r.forward(100)
r.left(500)


print(r.read_marker())


if r.read_marker() == 1:
    r.right(100)
    r.forward(350)
    r.left(420)
    temperature_list.append(r.take_temperature())
    if r.scan_for_people() is True:
        r.rescue_person()
        r.right(420)
        r.backward(350)
        r.right(500)
        r.backward(100)
        r.right(1000)
        r.backward(780)
        r.right(710)
        r.backward(900)
        r.left(2300)
        r.forward(2000)

    else:
        r.right(420)
        r.backward(350)


print(temperature_list)
plt.plot(temperature_list)
plt.xticks(list(range(len(temperature_list))))
plt.xlabel('Room Number (0 is hallway)')
plt.ylabel('Temperature (Degrees)')
plt.title('Temperature of Rooms in Simulator')
plt.show()
