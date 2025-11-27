# CMU Graphics Demos

Classroom-ready CMU Graphics demos for Python CS1 courses. This repository contains well-commented examples demonstrating shapes, animation, interactivity, and small projects suitable for introductory programming students.

## 📋 Table of Contents

- [About CMU Graphics](#about-cmu-graphics)
- [Installation](#installation)
- [Repository Structure](#repository-structure)
- [Running the Demos](#running-the-demos)
- [Demo Descriptions](#demo-descriptions)
- [License](#license)

## About CMU Graphics

[CMU Graphics](https://academy.cs.cmu.edu/desktop) is a beginner-friendly Python graphics library developed by Carnegie Mellon University. It provides an easy-to-use API for creating shapes, animations, and interactive applications—perfect for teaching introductory computer science concepts.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Installing CMU Graphics

Install the CMU Graphics library using pip:

```bash
pip install cmu-graphics
```

Or, if you're using Python 3 specifically:

```bash
pip3 install cmu-graphics
```

### Verifying Installation

To verify the installation was successful, run Python and try importing the library:

```python
from cmu_graphics import *
print("CMU Graphics installed successfully!")
```

## Repository Structure

```
cmu-graphics-demos/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── basics/                      # Fundamental concepts
│   ├── shapes.py               # Basic shape drawing
│   └── simple_animation.py     # Introduction to animation
└── projects/                    # Complete mini-projects
    └── bouncing_ball/
        ├── main.py             # Bouncing ball simulation
        └── README.md           # Project documentation
```

## Running the Demos

Navigate to the demo file you want to run and execute it with Python:

```bash
# Run the shapes demo
python basics/shapes.py

# Run the animation demo
python basics/simple_animation.py

# Run the bouncing ball project
python projects/bouncing_ball/main.py
```

Each demo opens a graphics window. Close the window to exit the application.

## Demo Descriptions

### Basics

#### `basics/shapes.py`
An introduction to drawing shapes with CMU Graphics. Covers:
- Rectangles, circles, and ovals
- Lines and polygons
- Stars and regular polygons
- Labels (text)
- Shape properties (fill, border, rotation)

#### `basics/simple_animation.py`
Learn how to create animations using the `onStep()` function. Demonstrates:
- Moving shapes across the screen
- Bouncing/reversing direction
- Pulsating (growing/shrinking) shapes
- Rotating shapes
- Color-changing animations
- Orbital motion using trigonometry

### Projects

#### `projects/bouncing_ball/`
A complete physics simulation featuring:
- Gravity and acceleration
- Wall and floor collision detection
- Bounce physics with energy loss
- User interaction (click to reset, keyboard controls)
- Visual effects (shadow)

See the project's [README](projects/bouncing_ball/README.md) for detailed documentation.

## For Instructors

These demos are designed to be:

- **Self-contained** - Each file runs independently
- **Well-commented** - Clear explanations throughout the code
- **Progressive** - Start with shapes, then animation, then projects
- **Modifiable** - Students can easily experiment with parameters

### Suggested Lesson Plan

1. **Day 1**: Introduction to CMU Graphics with `shapes.py`
2. **Day 2**: Animation basics with `simple_animation.py`
3. **Day 3-4**: Work through the bouncing ball project
4. **Day 5+**: Students create their own projects

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests with:
- Bug fixes
- New demo ideas
- Documentation improvements
- Additional projects

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
