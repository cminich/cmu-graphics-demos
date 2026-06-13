# CMU Graphics Demos

Classroom-ready CMU Graphics demos for Python CS1 courses. This repository contains well-commented examples suitable for introductory programming students.

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
├── bouncing-ball/               # Bouncing ball simulation
│   ├── main.py
│   └── README.md
└── wyo-lax/                     # Wyoming lacrosse demo
    └── main.py
```

## Running the Demos

Navigate to the demo file you want to run and execute it with Python:

```bash
# Run the bouncing ball project
python bouncing-ball/main.py

# Run the wyo-lax demo
python wyo-lax/main.py
```

Each demo opens a graphics window. Close the window to exit the application.

## Demo Descriptions

### `bouncing-ball/`

A complete physics simulation featuring:
- Gravity and acceleration
- Wall and floor collision detection
- Bounce physics with energy loss
- User interaction (click to reset, keyboard controls)
- Visual effects (shadow)

See the project's [README](bouncing-ball/README.md) for detailed documentation.

### `wyo-lax/`

A lacrosse-themed CMU Graphics demo.

## For Instructors

These demos are designed to be:

- **Self-contained** - Each file runs independently
- **Well-commented** - Clear explanations throughout the code
- **Modifiable** - Students can easily experiment with parameters

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests with:
- Bug fixes
- New demo ideas
- Documentation improvements
- Additional projects

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
