# DrawCircle

This was a fun little script I made to use on the website https://neal.fun/perfect-circle/.
The purpose of the website it to try to draw a circle as perfect as possible and it will rate your drawing.

I made this script to generate the positions that the mouse should follow to create a circle. With this script, I'm able to achieve 99.9% of a circle. This appears to be the highest score since the score tagline is "Perfect circle".

## How it works

To generate the points, I need a center position and radius to use. The center position I measure by placing my mouse on the center of the website and having pynput return to me the mouse position. This value depends on your monitor resolution, so this will need to be determined for each setup.

Once I have that info, I generate the domain of the circle. This is the value I will use my loop to run through as my x value when using the formula of a circle.
I took the the formula of a circle, solved the equation for y so that we can calculate the y position to be used. The center position coordinates and the radius get inserted into the equation and now it's ready to be used. When solving for y, at one point you need to take the square root of a squared variable. This means we will have two functions that we need to run the domain through. A positive and negative function, each responsible for drawing half of the circle. 
I loop through the domain and this provides me the first half of points. I loop through the domain rather than just a counting the difference between the domain as this allows me to set my x directly to the loop variable. Although this does give a bit extra calculation in the 2nd loop.
For the second half, I now need to count down in my x values. I do this by adding the domain ends value's together and then subtracting my looping variable. If I don't count down, the first position of this half will be on the opposite side of the last position of the first half(Next to first position of the first half). This causes a jump in points, which is something the website will not accept. The website is looking for a continuous drawing of a circle.

Once both loops are done, all points are generated and can now be used with pynput to move the mouse across those positions.
I setup the mouse into the inital position of the list, to prevent any jumps from where the user may set the mouse. Register a mouse press and hold, move the mouse to each position in a loop, and release the mouse press.
This completes the drawing of a circle.
