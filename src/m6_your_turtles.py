"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and tae.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

"""
Demonstrates:
  -- LOOPS (doing something repeatedly) and
  -- using OBJECTS
via Turtle Graphics.

Concepts include:
 * Using OBJECTS:
   -- CONSTRUCT an INSTANCE of a CLASS (we call such instances OBJECTS).
   -- Make an object  ** DO **  something by using a METHOD.
   -- Reference an object's  ** DATA **  by using an INSTANCE VARIABLE.

 * LOOPS:
   -- Using a FOR expression like this:
         for k in range(41):
             blah
             blah
             blah

     The above repeats the body of the FOR expression 41 times.
     The name  k  is:
            0 the first time the body runs,
       then 1 the next time the body runs,
       then 2 the next time the body runs,
         etc
       then 40 the last time the body runs.

 * ASSIGNMENT and NAMES
  -- ASSIGNING a VALUE to a NAME (aka VARIABLE), as in these examples:
        jack = 45
        jill = 'ran down the hill'
        size = size - 12

 * The DOT trick: If you type expressions like the following,
     pausing after typing the DOT (period, full stop),
     then the window that pops up give lots of clues for what you can do!
        rg.
        rg.SimpleTurtle().
        rg.Pen().
        rg.PaintBucket().

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Amanda Stouder, Aaron Wilkin, and their colleagues.
"""
import rosegraphics as rg

###############################################################################
# One window, for two examples.
###############################################################################
window = rg.TurtleWindow()

###############################################################################
# Example 1.
###############################################################################
blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('midnight blue', 3)
blue_turtle.speed = 20  # Fast

# The first square will be 300 x 300 pixels:
size = 150

# Do the indented code 6 times.  Each time draws a square.
for k in range(8):

    # Put the pen down, then draw a square of the given size:
    blue_turtle.draw_square(size)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    blue_turtle.pen_up()
    blue_turtle.right(90)
    blue_turtle.forward(10)
    blue_turtle.left(45)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    blue_turtle.pen_down()
    #size = size - 12

###############################################################################
# Example 2.  It shows how to speed up the animation.
###############################################################################
window.tracer(100)  # Bigger numbers make the animation run faster

another_turtle = rg.SimpleTurtle('triangle')
another_turtle.pen = rg.Pen('red', 1)
another_turtle.backward(50)

# The name k takes on the values 0, 1, 2, ... 499 as the loop runs
for k in range(700):
    another_turtle.left(60)
    another_turtle.forward(k)

for k in range(700):
    another_turtle.right(91)
    another_turtle.backward(k)

window.close_on_mouse_click()