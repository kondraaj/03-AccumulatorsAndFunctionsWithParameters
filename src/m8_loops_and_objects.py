"""
This module demonstrates simple LOOPS of the form:
   for k in range(blah):
      ... k ...

and also USING OBJECTS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Aaron Kondrat.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    run_test_print_sequence1()
    run_test_draw_circles1()
    run_test_print_sequence2()
    run_test_draw_circles2()
    run_test_print_sequences3()
    run_test_draw_circles3()
    run_test_print_cosines()


def print_sequence1():
    """
    Prints:
       0
       10
       20
       30
       40
       ...
       200
    """
    for k in range(21):
        print(10 * k)

    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------


def run_test_print_sequence1():
    print()
    print('--------------------------------------------------')
    print('Running print_sequence1:')
    print('--------------------------------------------------')
    print_sequence1()


def draw_circles1():
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws 21 rg.Circle objects such that:
         -- Each is centered at (200, 200)
         -- They have radii:  0  10  20  30  40 ... 200, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(400, 400)
    center_point = rg.Point(200, 200)

    for k in range(21):
        circle = rg.Circle(center_point, 10 * k)
        circle.attach_to(window)

    window.render()
    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # HINT: You might find a prior module useful when 'writing' this code.
    # ------------------------------------------------------------------


def run_test_draw_circles1():
    print()
    print('--------------------------------------------------')
    print('Running draw_circles1:  See graphics window')
    print('--------------------------------------------------')
    draw_circles1()


def print_sequence2():
    """
    Prints:
      50
      70
      90
      110
      130
      ...
      390.
    """
    for k in range(18):
        total = (k + 3) * 2
        print((total - 1) * 10)

    # ------------------------------------------------------------------
    # DONE: 4. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------


def run_test_print_sequence2():
    print()
    print('--------------------------------------------------')
    print('Running print_sequence2:')
    print('--------------------------------------------------')
    print_sequence2()


def draw_circles2():
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- Each has fill_color 'blue'.
         -- They are centered at, respectively:
               (50, 100)   (70, 100)   (90, 100)  (110, 100) ... (390, 100)
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(400, 400)

    for k in range(18):
        x_center = (((k + 3) * 2) - 1) * 10
        center = rg.Point(x_center, 100)
        circle = rg.Circle(center, 10)
        circle.fill_color = 'blue'
        circle.attach_to(window)

    window.render()
    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 5. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------


def run_test_draw_circles2():
    print()
    print('--------------------------------------------------')
    print('Running draw_circles2:  See graphics window')
    print('--------------------------------------------------')
    draw_circles2()


def print_sequence3():
    """
    Prints:
      1
      2
      3 
      4
      ...
      100.
    """
    value = 1
    for k in range(100):
        print(value)
        value = value + 1

    # ------------------------------------------------------------------
    # DONE: 6. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------


def run_test_print_sequences3():
    print()
    print('--------------------------------------------------')
    print('Running print_sequence3:')
    print('--------------------------------------------------')
    print_sequence3()


def draw_circles3():
    """
    -- Constructs an rg.RoseWindow whose width and height are both 300.
    -- Constructs and draws 100 rg.Circle objects such that:
         -- Each is centered at (200, 150)
         -- They have radii:  1  2  3  4  ... 100, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(300, 300)
    radius = 1
    for k in range(100):
        center = rg.Point(200, 150)
        circle = rg.Circle(center, radius)
        circle.attach_to(window)
        radius = radius + 1

    window.render()
    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 7. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------


def run_test_draw_circles3():
    print()
    print('--------------------------------------------------')
    print('Running draw_circles3:  See graphics window')
    print('--------------------------------------------------')
    draw_circles3()


def print_cosines():
    """
    For each of the integers 0  1  2  ... 100,
    prints 80 times the cosine of that integer.
    Thus, the numbers printed should be about:
       80.0
       43.224184469451174
       -33.29174692377139
       -79.19939972803563
       -52.29148966908895
       22.6929748370581
       76.81362293202928
       60.31218034746437
         ...
       -65.54305962331674
       3.185670431451112
       68.9855097830147
    """
    for k in range(101):
        print(80 * math.cos(k))
    # ------------------------------------------------------------------
    # DONE: 8. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    #
    # HINT: You need to   import math   at the top of this file
    #       to use math functions like the ones for cosine and sine.
    #       Once you have that import in place, typing
    #            math.
    #       (note the DOT) and pausing will display options that make
    #       it plain what the notation for the cosine function is.
    # ------------------------------------------------------------------


def run_test_print_cosines():
    print()
    print('--------------------------------------------------')
    print('Running print_cosines:')
    print('--------------------------------------------------')
    print_cosines()


def draw_cosines_and_sines():
    """
    -- Constructs a window whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- They are centered at, respectively:
               ( 200 + (80 * cos(0)), 200 + (80 * sin(0) )
               ( 200 + (80 * cos(1)), 200 + (80 * sin(1) )
               ( 200 + (80 * cos(2)), 200 + (80 * sin(2) )
               ( 200 + (80 * cos(3)), 200 + (80 * sin(3) )
                   ...
               ( 200 + (80 * cos(100)), 200 + (80 * sin(100) )
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(400, 400)

    for k in range(101)
        center = rg.Point( 200 + (80 * cos(k)), 200 + (80 * sin(k) ))
        circle = rg.Circle(center, 10)
        circle.attach_to(window)
        
    # ------------------------------------------------------------------
    # TODO: 9. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_cosines_and_sines:  See graphics window')
    print('--------------------------------------------------')


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
