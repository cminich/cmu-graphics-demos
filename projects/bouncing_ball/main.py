"""
CMU Graphics - Bouncing Ball Project
=====================================
A complete bouncing ball simulation with physics-based movement.
The ball bounces off the walls and floor with realistic gravity effects.

Features:
- Gravity simulation
- Bounce physics with energy loss
- Wall collision detection
- Click to reset ball position

Prerequisites:
- Python 3.6+
- cmu_graphics library installed

Run this demo:
    python main.py
"""

from cmu_graphics import *

# =============================================================================
# CONSTANTS
# =============================================================================
# Canvas dimensions (default CMU Graphics canvas is 400x400)
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

# Ball properties
BALL_RADIUS = 20
BALL_COLOR = 'steelBlue'
BALL_BORDER_COLOR = 'navy'

# Physics constants
GRAVITY = 0.5           # Acceleration due to gravity (pixels per step^2)
BOUNCE_FACTOR = 0.8     # Energy retained after bounce (0.0 to 1.0)
FRICTION = 0.99         # Horizontal friction factor
MIN_VELOCITY = 0.5      # Minimum velocity threshold (stops tiny bounces)

# =============================================================================
# INITIAL SETUP
# =============================================================================

# Create the ball shape
ball = Circle(CANVAS_WIDTH // 2, BALL_RADIUS + 10, BALL_RADIUS, 
              fill=BALL_COLOR, border=BALL_BORDER_COLOR, borderWidth=2)

# Initialize velocity components
app.velocityX = 3       # Initial horizontal velocity
app.velocityY = 0       # Initial vertical velocity (starts falling)

# Track if the ball is at rest
app.atRest = False

# =============================================================================
# USER INTERFACE ELEMENTS
# =============================================================================

# Title label
Label('Bouncing Ball Simulation', CANVAS_WIDTH // 2, 20, 
      size=18, bold=True, fill='darkSlateGray')

# Instructions label
Label('Click anywhere to reset the ball', CANVAS_WIDTH // 2, CANVAS_HEIGHT - 20, 
      size=12, fill='gray')

# Ground line (visual reference)
Line(0, CANVAS_HEIGHT - 5, CANVAS_WIDTH, CANVAS_HEIGHT - 5, 
     fill='darkGray', lineWidth=2)

# =============================================================================
# PHYSICS SIMULATION
# =============================================================================

def onStep():
    """
    Called automatically ~30 times per second.
    Updates ball position based on velocity and handles collisions.
    """
    # Skip physics if ball is at rest
    if app.atRest:
        return
    
    # -------------------------------------------------------------------------
    # Apply Gravity
    # -------------------------------------------------------------------------
    # Gravity increases downward velocity each step
    app.velocityY += GRAVITY
    
    # -------------------------------------------------------------------------
    # Apply Friction to Horizontal Movement
    # -------------------------------------------------------------------------
    app.velocityX *= FRICTION
    
    # -------------------------------------------------------------------------
    # Update Position
    # -------------------------------------------------------------------------
    ball.centerX += app.velocityX
    ball.centerY += app.velocityY
    
    # -------------------------------------------------------------------------
    # Floor Collision Detection
    # -------------------------------------------------------------------------
    floorY = CANVAS_HEIGHT - 5  # Account for ground line
    
    if ball.centerY + BALL_RADIUS >= floorY:
        # Place ball exactly at floor level
        ball.centerY = floorY - BALL_RADIUS
        
        # Reverse and reduce vertical velocity (bounce)
        app.velocityY = -app.velocityY * BOUNCE_FACTOR
        
        # Check if ball should stop bouncing
        if abs(app.velocityY) < MIN_VELOCITY:
            app.velocityY = 0
            # Check if horizontal movement should also stop
            if abs(app.velocityX) < MIN_VELOCITY:
                app.velocityX = 0
                app.atRest = True
    
    # -------------------------------------------------------------------------
    # Ceiling Collision Detection
    # -------------------------------------------------------------------------
    if ball.centerY - BALL_RADIUS <= 0:
        ball.centerY = BALL_RADIUS
        app.velocityY = -app.velocityY * BOUNCE_FACTOR
    
    # -------------------------------------------------------------------------
    # Left Wall Collision Detection
    # -------------------------------------------------------------------------
    if ball.centerX - BALL_RADIUS <= 0:
        ball.centerX = BALL_RADIUS
        app.velocityX = -app.velocityX * BOUNCE_FACTOR
    
    # -------------------------------------------------------------------------
    # Right Wall Collision Detection
    # -------------------------------------------------------------------------
    if ball.centerX + BALL_RADIUS >= CANVAS_WIDTH:
        ball.centerX = CANVAS_WIDTH - BALL_RADIUS
        app.velocityX = -app.velocityX * BOUNCE_FACTOR

# =============================================================================
# USER INTERACTION
# =============================================================================

def onMousePress(mouseX, mouseY):
    """
    Called when the user clicks on the canvas.
    Resets the ball to the clicked position with new velocity.
    """
    # Reset ball position to click location
    ball.centerX = mouseX
    ball.centerY = mouseY
    
    # Give the ball a new random-ish velocity
    # (Using a simple formula based on click position)
    app.velocityX = (mouseX - CANVAS_WIDTH // 2) / 30
    app.velocityY = 0  # Start falling from rest
    
    # Wake up the ball if it was at rest
    app.atRest = False

def onKeyPress(key):
    """
    Called when the user presses a key.
    Provides additional controls for the simulation.
    """
    if key == 'space':
        # Toggle pause by inverting atRest state
        app.atRest = not app.atRest
    elif key == 'r':
        # Reset to initial position
        ball.centerX = CANVAS_WIDTH // 2
        ball.centerY = BALL_RADIUS + 10
        app.velocityX = 3
        app.velocityY = 0
        app.atRest = False
    elif key == 'up':
        # Give the ball an upward boost
        app.velocityY -= 10
        app.atRest = False
    elif key == 'left':
        # Push the ball left
        app.velocityX -= 5
        app.atRest = False
    elif key == 'right':
        # Push the ball right
        app.velocityX += 5
        app.atRest = False

# =============================================================================
# ADDITIONAL VISUAL FEEDBACK
# =============================================================================

# Add a shadow under the ball for depth perception
shadow = Oval(ball.centerX, CANVAS_HEIGHT - 8, BALL_RADIUS * 1.5, 8, 
              fill='gray', opacity=30)

# Update shadow position in onStep
original_onStep = onStep

def onStep():
    """
    Extended onStep that also updates the shadow position.
    """
    original_onStep()
    
    # Update shadow position to match ball's X position
    shadow.centerX = ball.centerX
    
    # Scale shadow size based on ball height
    # Shadow is larger when ball is higher (simulates light from above)
    height_factor = ball.centerY / CANVAS_HEIGHT
    shadow.width = BALL_RADIUS * (1.5 + (1 - height_factor))
    shadow.opacity = 20 + int(30 * height_factor)

# Keyboard controls info (displayed at bottom)
controlsGroup = Group(
    Rect(5, CANVAS_HEIGHT - 85, 120, 60, fill='white', opacity=80, 
         border='lightGray', borderWidth=1),
    Label('Controls:', 65, CANVAS_HEIGHT - 75, size=10, bold=True, fill='darkGray'),
    Label('SPACE: Pause/Resume', 65, CANVAS_HEIGHT - 60, size=9, fill='gray'),
    Label('R: Reset Ball', 65, CANVAS_HEIGHT - 48, size=9, fill='gray'),
    Label('Arrows: Push Ball', 65, CANVAS_HEIGHT - 36, size=9, fill='gray')
)

# =============================================================================
# START THE APPLICATION
# =============================================================================
# This line must be at the end of the script to display the canvas.
cmu_graphics.run()
