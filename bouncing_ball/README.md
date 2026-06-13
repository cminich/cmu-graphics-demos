# Bouncing Ball Project

A physics-based bouncing ball simulation using the CMU Graphics library.

## Overview

This project demonstrates fundamental game physics concepts including:

- **Gravity simulation** - The ball accelerates downward over time
- **Collision detection** - The ball bounces off walls and floor
- **Energy loss** - Each bounce reduces the ball's velocity (bounce factor)
- **Friction** - Horizontal movement gradually slows down
- **User interaction** - Click to reposition, keyboard controls for manipulation

## Files

- `main.py` - The complete bouncing ball simulation

## Running the Project

Make sure you have the CMU Graphics library installed:

```bash
pip install cmu-graphics
```

Then run the project:

```bash
python main.py
```

## Controls

| Key/Action | Description |
|------------|-------------|
| **Click** | Reset ball to clicked position |
| **SPACE** | Pause/Resume simulation |
| **R** | Reset ball to starting position |
| **↑ (Up Arrow)** | Give ball an upward boost |
| **← (Left Arrow)** | Push ball to the left |
| **→ (Right Arrow)** | Push ball to the right |

## Physics Explained

### Gravity
Each frame, the vertical velocity increases by the gravity constant:
```python
velocityY += GRAVITY
```

### Bounce Physics
When the ball hits a surface, its velocity is reversed and reduced:
```python
velocityY = -velocityY * BOUNCE_FACTOR
```

The `BOUNCE_FACTOR` (0.8 by default) determines how much energy is retained. A value of 1.0 would mean a perfect bounce (no energy loss), while 0.5 would lose half the energy on each bounce.

### Friction
Horizontal velocity is gradually reduced by the friction factor:
```python
velocityX *= FRICTION
```

## Customization Ideas

Try modifying these constants in `main.py` to change the simulation behavior:

| Constant | Default | Description |
|----------|---------|-------------|
| `GRAVITY` | 0.5 | Acceleration due to gravity |
| `BOUNCE_FACTOR` | 0.8 | Energy retained after bounce (0.0-1.0) |
| `FRICTION` | 0.99 | Horizontal friction factor |
| `BALL_RADIUS` | 20 | Size of the ball |
| `BALL_COLOR` | 'steelBlue' | Color of the ball |

## Learning Objectives

After studying this project, students should understand:

1. How to implement basic physics in an animation
2. How to detect and respond to boundary collisions
3. How to handle user input for interactive applications
4. How to organize code with constants and functions
5. How animation loops work with `onStep()`

## Extensions

Here are some ideas to extend this project:

- [ ] Add multiple balls that interact with each other
- [ ] Implement ball-to-ball collision detection
- [ ] Add obstacles on the canvas
- [ ] Create a "breakout" style game
- [ ] Add sound effects using additional libraries
- [ ] Track and display the ball's statistics (max height, bounce count, etc.)
