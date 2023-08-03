from pynput.mouse import Button, Controller
from time import sleep

mouse = Controller()

print('The current pointer position is {0}'.format(mouse.position))
# mouse.move(- left, - up)
# mouse.move(+ right, + down)

def generatePoints(r):
    center = (980, 531)
    #center = (3860, 1071)
    domain = (center[0] - r, center[0] + r)
    points = []
    
    for i in range(domain[0], domain[1] + 1):
        x = i
        y = (r**2 - ((x - center[0])**2))**(0.5) + center[1]
        points.append((x,y.real))
        
    for i in range(domain[0], domain[1] + 1):
        x = domain[0] + domain[1] - i
        y = (-1 * ((r**2 - ((x - center[0])**2))**(0.5))) + center[1]
        points.append((x,y.real))
    
    return points

# Generate all the points of the circle to move the mouse to.
circlePositions = generatePoints(450)

# Set mouse to the inital position.
sleep(2)
initX, initY = circlePositions[0]
mouse.position = (initX, initY)

# Start the circle drawing
sleep(2)
mouse.press(Button.left)

for x,y in circlePositions:
    mouse.position = (x, y)
    sleep(0.0001) # Need a sleep condition because it moves too fast for the website without it.

mouse.release(Button.left)
# Circle drawing completed.
