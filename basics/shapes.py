"""
CMU Graphics - Basic Shapes Demo
================================
This demo introduces the fundamental shapes available in the cmu_graphics library.
It covers creating rectangles, circles, ovals, lines, polygons, and labels.

Prerequisites:
- Python 3.6+
- cmu_graphics library installed

Run this demo:
    python shapes.py
"""

from cmu_graphics import *

# =============================================================================
# RECTANGLE
# =============================================================================
# Rect(centerX, centerY, width, height, ...)
# Creates a rectangle centered at (centerX, centerY) with the given dimensions.
Rect(50, 50, 80, 60, fill='steelBlue')

# =============================================================================
# CIRCLE
# =============================================================================
# Circle(centerX, centerY, radius, ...)
# Creates a circle centered at (centerX, centerY) with the given radius.
Circle(150, 50, 30, fill='crimson')

# =============================================================================
# OVAL
# =============================================================================
# Oval(centerX, centerY, width, height, ...)
# Creates an oval (ellipse) centered at (centerX, centerY) with given dimensions.
Oval(250, 50, 60, 40, fill='gold')

# =============================================================================
# LINE
# =============================================================================
# Line(x1, y1, x2, y2, ...)
# Creates a line from point (x1, y1) to point (x2, y2).
Line(320, 20, 380, 80, fill='forestGreen', lineWidth=4)

# =============================================================================
# POLYGON
# =============================================================================
# Polygon(x1, y1, x2, y2, x3, y3, ..., ...)
# Creates a polygon with vertices at the specified coordinates.
# This example creates a triangle.
Polygon(50, 150, 90, 100, 130, 150, fill='purple')

# =============================================================================
# STAR
# =============================================================================
# Star(centerX, centerY, radius, points, ...)
# Creates a star shape centered at (centerX, centerY).
Star(200, 130, 30, 5, fill='orange')

# =============================================================================
# REGULAR POLYGON
# =============================================================================
# RegularPolygon(centerX, centerY, radius, points, ...)
# Creates a regular polygon (e.g., pentagon, hexagon) centered at (centerX, centerY).
RegularPolygon(300, 130, 30, 6, fill='teal')

# =============================================================================
# LABELS (TEXT)
# =============================================================================
# Label(text, centerX, centerY, ...)
# Creates a text label centered at (centerX, centerY).
Label('Hello, CMU Graphics!', 200, 200, size=20, bold=True, fill='navy')

# =============================================================================
# SHAPES WITH BORDERS
# =============================================================================
# You can add borders to shapes using 'border' and 'borderWidth' parameters.
Rect(50, 280, 80, 60, fill='lightGray', border='black', borderWidth=3)
Circle(150, 280, 30, fill='lightPink', border='darkRed', borderWidth=2)

# =============================================================================
# TRANSPARENT / NO FILL SHAPES
# =============================================================================
# Use fill=None for transparent shapes (outline only).
Rect(250, 250, 80, 60, fill=None, border='darkGreen', borderWidth=3)

# =============================================================================
# ROTATED SHAPES
# =============================================================================
# Use the 'rotateAngle' parameter to rotate shapes.
Rect(350, 280, 60, 40, fill='salmon', rotateAngle=30)

# =============================================================================
# LABELS WITH DIFFERENT FONTS AND SIZES
# =============================================================================
Label('Small Text', 80, 350, size=12, fill='gray')
Label('Big Text', 200, 350, size=24, bold=True, fill='darkBlue')
Label('Italic Text', 320, 350, size=16, italic=True, fill='darkGreen')

# Start the graphics application
# This line must be at the end of the script to display the canvas.
cmu_graphics.run()
