"""
CMU Graphics - Simple Animation Demo
=====================================
This demo introduces basic animation concepts using the cmu_graphics library.

# In the onStep function, the position of the ball (movingCircle) is updated to create animation:
# - Each time onStep is called, the x-coordinate of the ball increases or decreases,
#   depending on the value of app.circleDirection.
# - This makes the ball move right (when app.circleDirection is 1) or left (when it is -1).
# - The position update is done by adding a small amount to movingCircle.centerX.
# - If the ball reaches the edge of the canvas, app.circleDirection is reversed,
#   causing the ball to "bounce" and move the other direction.
It demonstrates how to use the onStep() function to create movement over time.

Prerequisites:
- Python 3.6+
- cmu_graphics library installed

Run this demo:
    python simple_animation.py
"""

from cmu_graphics import *

# =============================================================================
# SETUP - Create the shapes we want to animate
# =============================================================================

# A circle that will move across the screen
movingCircle = Circle(50, 100, 25, fill='steelBlue')

# A rectangle that will grow and shrink (pulsate)
pulsatingRect = Rect(200, 200, 50, 50, fill='crimson', align='center')

# A star that will rotate
rotatingStart = Star(350, 100, 30, 5, fill='gold')

# A label to display instructions
Label('Watch the shapes animate!', 200, 30, size=18, bold=True, fill='navy')
Label('The circle moves, the rectangle pulsates, and the star rotates.', 
      200, 50, size=12, fill='gray')

# =============================================================================
# ANIMATION VARIABLES
# =============================================================================
# We use app.* variables to store animation state across frames.

# Direction for the moving circle (1 = right, -1 = left)
app.circleDirection = 1

# Whether the rectangle is growing or shrinking
app.rectGrowing = True

# Current size factor for the rectangle
app.rectSize = 50

# =============================================================================
# onStep() - Called automatically ~30 times per second
# =============================================================================
def onStep():
    """
    This function is called automatically by the cmu_graphics library
    approximately 30 times per second. Use it to update shape properties
    for animation effects.
    """
    
    # -------------------------------------------------------------------------
    # ANIMATION 1: Moving Circle (Horizontal bounce)
    # -------------------------------------------------------------------------
    # Move the circle in the current direction
    movingCircle.centerX += 3 * app.circleDirection
    
    # If the circle reaches the edge of the canvas, reverse direction
    if movingCircle.centerX >= 375:  # Right edge (400 - radius)
        app.circleDirection = -1
    elif movingCircle.centerX <= 25:  # Left edge (radius)
        app.circleDirection = 1
    
    # -------------------------------------------------------------------------
    # ANIMATION 2: Pulsating Rectangle
    # -------------------------------------------------------------------------
    # Grow or shrink the rectangle
    if app.rectGrowing:
        app.rectSize += 1
        if app.rectSize >= 80:
            app.rectGrowing = False
    else:
        app.rectSize -= 1
        if app.rectSize <= 30:
            app.rectGrowing = True
    
    # Apply the new size to the rectangle
    pulsatingRect.width = app.rectSize
    pulsatingRect.height = app.rectSize
    
    # -------------------------------------------------------------------------
    # ANIMATION 3: Rotating Star
    # -------------------------------------------------------------------------
    # Rotate the star by 3 degrees each step
    rotatingStart.rotateAngle += 3

# =============================================================================
# ADDITIONAL ANIMATED ELEMENTS
# =============================================================================

# A color-changing circle
colorCircle = Circle(100, 300, 30, fill='red')

# Track the current color index
app.colorIndex = 0
app.colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
app.colorCounter = 0

# Extended onStep to include color changing
# Note: We need to redefine onStep to include all animations
def onStep():
    """
    Combined animation function for all shapes.
    """
    global colorCircle
    
    # Animation 1: Moving Circle
    movingCircle.centerX += 3 * app.circleDirection
    if movingCircle.centerX >= 375:
        app.circleDirection = -1
    elif movingCircle.centerX <= 25:
        app.circleDirection = 1
    
    # Animation 2: Pulsating Rectangle
    if app.rectGrowing:
        app.rectSize += 1
        if app.rectSize >= 80:
            app.rectGrowing = False
    else:
        app.rectSize -= 1
        if app.rectSize <= 30:
            app.rectGrowing = True
    pulsatingRect.width = app.rectSize
    pulsatingRect.height = app.rectSize
    
    # Animation 3: Rotating Star
    rotatingStart.rotateAngle += 3
    
    # Animation 4: Color-Changing Circle
    # Change color every 15 steps (about 0.5 seconds)
    app.colorCounter += 1
    if app.colorCounter >= 15:
        app.colorCounter = 0
        app.colorIndex = (app.colorIndex + 1) % len(app.colors)
        colorCircle.fill = app.colors[app.colorIndex]

# Display info about the color-changing circle
Label('Color-changing circle below:', 100, 260, size=12, fill='gray')

# =============================================================================
# EXTRA: An orbiting dot
# =============================================================================
import math

# Center point for the orbit
orbitCenterX = 300
orbitCenterY = 300
orbitRadius = 40

# The orbiting dot
orbitDot = Circle(orbitCenterX + orbitRadius, orbitCenterY, 10, fill='darkGreen')

# Orbit indicator circle (static)
Oval(orbitCenterX, orbitCenterY, orbitRadius * 2, orbitRadius * 2, 
     fill=None, border='lightGray', borderWidth=1)

# Track the angle for orbital motion
app.orbitAngle = 0

# Final combined onStep with orbital motion
def onStep():
    """
    Master animation function that handles all animations:
    1. Bouncing circle
    2. Pulsating rectangle
    3. Rotating star
    4. Color-changing circle
    5. Orbiting dot
    """
    # Animation 1: Moving Circle
    movingCircle.centerX += 3 * app.circleDirection
    if movingCircle.centerX >= 375:
        app.circleDirection = -1
    elif movingCircle.centerX <= 25:
        app.circleDirection = 1
    
    # Animation 2: Pulsating Rectangle
    if app.rectGrowing:
        app.rectSize += 1
        if app.rectSize >= 80:
            app.rectGrowing = False
    else:
        app.rectSize -= 1
        if app.rectSize <= 30:
            app.rectGrowing = True
    pulsatingRect.width = app.rectSize
    pulsatingRect.height = app.rectSize
    
    # Animation 3: Rotating Star
    rotatingStart.rotateAngle += 3
    
    # Animation 4: Color-Changing Circle
    app.colorCounter += 1
    if app.colorCounter >= 15:
        app.colorCounter = 0
        app.colorIndex = (app.colorIndex + 1) % len(app.colors)
        colorCircle.fill = app.colors[app.colorIndex]
    
    # Animation 5: Orbiting Dot
    app.orbitAngle += 0.05  # Radians per step
    orbitDot.centerX = orbitCenterX + orbitRadius * math.cos(app.orbitAngle)
    orbitDot.centerY = orbitCenterY + orbitRadius * math.sin(app.orbitAngle)

# Label for the orbiting dot
Label('Orbiting dot:', 300, 350, size=12, fill='gray')

# Start the graphics application
# This line must be at the end of the script to display the canvas.
cmu_graphics.run()
