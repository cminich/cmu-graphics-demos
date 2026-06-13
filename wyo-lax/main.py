from cmu_graphics import *
import math

# --------------------------------------------------
# Team colors
# --------------------------------------------------
WYO_BLUE = rgb(27, 31, 138)      # sampled from the Wyomissing logo
TV_GREEN = rgb(30, 105, 60)      # Twin Valley forest green
NAVY = rgb(15, 20, 95)
STEEL_BLUE = rgb(60, 90, 170)
LIGHT_BLUE = rgb(170, 195, 235)
PALE_BLUE = rgb(220, 232, 248)

# --------------------------------------------------
# Square canvas
# --------------------------------------------------
app.width = 400
app.height = 400
app.stepsPerSecond = 30
app.background = rgb(98, 136, 200)

# --------------------------------------------------
# Layered abstract background (blue & white theme)
# --------------------------------------------------
# Soft mid-ground washes
Circle(260, 115, 110, fill=LIGHT_BLUE, opacity=40)
Circle(120, 95, 80, fill=PALE_BLUE, opacity=30)
Circle(390, 170, 95, fill='white', opacity=20)
Circle(100, 330, 85, fill=LIGHT_BLUE, opacity=35)

# Soft geometric overlays
Polygon(150, 103, 260, 66, 340, 131, 230, 180,
        fill=PALE_BLUE, opacity=25)
Polygon(250, 151, 390, 140, 400, 306, 260, 291,
        fill=STEEL_BLUE, opacity=30)

# Thin vertical stripes along the left edge
Rect(18, 55, 7, 143, fill=NAVY, opacity=45)
Rect(30, 75, 6, 131, fill='white', opacity=45)
Rect(42, 92, 5, 103, fill=NAVY, opacity=30)

# --------------------------------------------------
# Wyomissing "W/A" monogram logo, built from shapes.
# (cx, cy) is the logo center; size is its approximate
# width in pixels. Drawn on a white badge disk.
# --------------------------------------------------
def drawWyoLogo(cx, cy, size):
    s = size / 100

    # White badge behind the monogram
    Circle(cx, cy, 62 * s, fill='white')

    # Outer strokes of the W, drawn as quads so the top
    # edges slant outward (outer corner higher than inner)
    Polygon(cx - 42 * s, cy - 36 * s,   # top outer corner
            cx - 30 * s, cy - 28 * s,   # top inner corner
            cx - 14 * s, cy + 39 * s,   # bottom inner corner
            cx - 24 * s, cy + 41 * s,   # bottom outer corner
            fill=WYO_BLUE)
    Polygon(cx + 42 * s, cy - 36 * s,
            cx + 30 * s, cy - 28 * s,
            cx + 14 * s, cy + 39 * s,
            cx + 24 * s, cy + 41 * s,
            fill=WYO_BLUE)

    # Middle of the W forms the 'A': two legs plus a crossbar
    Line(cx - 19 * s, cy + 40 * s, cx, cy - 26 * s,
         fill=WYO_BLUE, lineWidth=max(2, 9 * s))
    Line(cx + 19 * s, cy + 40 * s, cx, cy - 26 * s,
         fill=WYO_BLUE, lineWidth=max(2, 9 * s))
    Line(cx - 10 * s, cy + 12 * s, cx + 10 * s, cy + 12 * s,
         fill=WYO_BLUE, lineWidth=max(2, 7 * s))

# Bold foreground circles
drawWyoLogo(345, 45, 70)                                 # top-right Wyo logo
Circle(45, 220, 60, fill=LIGHT_BLUE)                     # left light blue
Circle(365, 205, 65, fill=STEEL_BLUE, opacity=90)        # right steel blue
Circle(75, 343, 55, fill=LIGHT_BLUE, opacity=60)         # bottom-left
Circle(180, 311, 48, fill=NAVY, opacity=95)              # bottom-center navy
Circle(370, 363, 60, fill='white')                       # bottom-right white
Circle(35, 389, 65, fill=LIGHT_BLUE)                     # bottom-left light blue

# Small decorative dots
for x, y, r in [
    (118, 41, 2), (300, 86, 4), (330, 246, 5),
    (210, 323, 6), (155, 243, 2),
    (170, 300, 2), (255, 49, 3)
]:
    Circle(x, y, r, fill='white', opacity=45)

# --------------------------------------------------
# Big bright "GOOD LUCK" in the upper left
# --------------------------------------------------
Label('GOOD LUCK', 123, 33, size=26, bold=True,
      fill='hotPink', opacity=90, font='monospace',
      rotateAngle=-6)
Label('GOOD LUCK', 121, 31, size=26, bold=True,
      fill='yellow', font='monospace',
      rotateAngle=-6)

# Left-aligned white underline
Line(60, 50, 180, 50, fill='white', lineWidth=4, opacity=95)

# --------------------------------------------------
# Main title: "Wyomissing" in logo blue, rest in white
# --------------------------------------------------
# White halo behind the blue word for pop
Label('Wyomissing', 202, 102, size=28, bold=True,
      fill='white', opacity=85)
Label('Wyomissing', 200, 100, size=28, bold=True, fill=WYO_BLUE)

# "Girls" / "Lacrosse" in white with navy shadow
Label('Girls', 202, 130, size=28, bold=True,
      fill=NAVY, opacity=60)
Label('Lacrosse', 202, 158, size=28, bold=True,
      fill=NAVY, opacity=60)
Label('Girls', 200, 128, size=28, bold=True, fill='white')
Label('Lacrosse', 200, 156, size=28, bold=True, fill='white')

# --------------------------------------------------
# Opponent
# --------------------------------------------------
# "vs" in white, "Twin Valley" in Twin Valley green
Label('vs', 107, 245, size=22, bold=True, fill=NAVY, opacity=50)
Label('vs', 105, 243, size=22, bold=True, fill='white')
Label('Twin Valley', 222, 245, size=22, bold=True,
      fill='white', opacity=85)
Label('Twin Valley', 220, 243, size=22, bold=True, fill=TV_GREEN)

# --------------------------------------------------
# Lacrosse stick icon function (returns a Group so the
# whole stick can be shown/hidden)
# --------------------------------------------------
def drawMiniStick(x, y, direction):
    d = direction
    ang = math.radians(-38 * d)
    ca, sa = math.cos(ang), math.sin(ang)
    hx, hy = x - 14 * d, y - 22      # head center

    def pt(px, py):
        # Rotate a head-local point (mirrored for direction)
        # and place it on the canvas
        px *= d
        return (hx + px * ca - py * sa, hy + px * sa + py * ca)

    g = Group()

    # Long shaft angled down toward center, with a butt cap
    g.add(Line(x, y, x + 48 * d, y + 64, fill='white', lineWidth=5))
    g.add(Circle(x + 48 * d, y + 64, 4, fill='white'))

    # Throat connecting the shaft to the head
    tx, ty = pt(0, 21)
    g.add(Line(tx, ty, x, y, fill='white', lineWidth=6))

    # Tilted oval head shell
    g.add(Oval(hx, hy, 30, 46, fill=None, border='white',
               borderWidth=4, rotateAngle=-38 * d))

    # Crosshatch mesh inside the head (two diagonal families)
    mesh = [
        ((-11, -14), (11, 2)), ((-12, -4), (12, 12)), ((-10, 6), (9, 16)),
        ((11, -14), (-11, 2)), ((12, -4), (-12, 12)), ((10, 6), (-9, 16)),
    ]
    for (p1, p2) in mesh:
        x1, y1 = pt(*p1)
        x2, y2 = pt(*p2)
        g.add(Line(x1, y1, x2, y2, fill='white', lineWidth=1.5, opacity=85))

    # Stud dots around the top rim of the head
    for t in (-80, -40, 0, 40):
        r = math.radians(t)
        rx, ry = pt(15 * math.sin(r), -23 * math.cos(r))
        g.add(Circle(rx, ry, 2, fill='white'))

    # Ball resting beside the stick
    g.add(Circle(x + 26 * d, y + 14, 6, fill='white', opacity=85))

    return g

# --------------------------------------------------
# Side view of a lacrosse goal cage (hidden until the
# mouse is held down). Open mouth faces left, toward
# the incoming ball.
# --------------------------------------------------
def drawGoalCage(gx, gy, height=80, depth=56):
    g = Group(
        # Front post, ground bar, and slanted top bar
        Line(gx, gy - height, gx, gy, fill='white', lineWidth=5),
        Line(gx, gy, gx + depth, gy, fill='white', lineWidth=5),
        Line(gx, gy - height, gx + depth, gy, fill='white', lineWidth=4)
    )

    # Netting inside the triangle
    for k in (14, 28, 42):
        top = gy - height * (1 - k / depth)
        g.add(Line(gx + k, top, gx + k, gy,
                   fill='white', lineWidth=1, opacity=70))
    for m in (20, 40, 60):
        back = gx + depth * (1 - m / height)
        g.add(Line(gx, gy - m, back, gy - m,
                   fill='white', lineWidth=1, opacity=70))
    return g

leftStick = drawMiniStick(62, 265, 1)
rightStick = drawMiniStick(340, 265, -1)

# Positioned so the ball's landing point (354, 243) sits
# at the center of the cage triangle
goalCage = drawGoalCage(335, 270)
goalCage.visible = False
# --------------------------------------------------
# Bottom date banner: white card, navy shadow, blue text
# --------------------------------------------------
Rect(58, 342, 276, 48, fill=NAVY, opacity=85)
Rect(70, 334, 276, 48, fill='white')
Label('State Championship', 210, 351, size=17, bold=True,
      fill=WYO_BLUE, opacity=30)
Label('State Championship', 208, 349, size=17, bold=True,
      fill=WYO_BLUE)
Label('Saturday, June 13', 210, 371, size=15,
      fill=WYO_BLUE, opacity=30)
Label('Saturday, June 13', 208, 369, size=15,
      fill=WYO_BLUE)

# --------------------------------------------------
# GO SPARTANS! hype text, on screen from the start and
# pulsing throughout the animation
# --------------------------------------------------
goShadow = Label('GO SPARTANS!', 203, 311, size=24,
                 bold=True, fill=NAVY, opacity=60, font='montserrat')
goText = Label('GO SPARTANS!', 200, 308, size=24,
               bold=True, fill='white', opacity=95, font='montserrat')

# --------------------------------------------------
# Animated floating circles
# --------------------------------------------------
floaters = Group()

def makeFloater(x, y, r, color, dx, dy, opacity):
    c = Circle(x, y, r, fill=color, opacity=opacity)
    c.dx = dx
    c.dy = dy
    floaters.add(c)

makeFloater(250, 46, 34, PALE_BLUE, .25, .15, 25)
makeFloater(280, 51, 28, 'white', -.2, .12, 20)
makeFloater(175, 186, 22, 'white', .15, -.12, 35)
makeFloater(260, 289, 20, LIGHT_BLUE, -.12, .12, 32)
makeFloater(85, 120, 36, PALE_BLUE, .18, .1, 20)

# --------------------------------------------------
# Lacrosse ball tossed in an arc between the two sticks
# --------------------------------------------------
# Stick head centers (from the drawMiniStick calls above)
TOSS_X1, TOSS_X2 = 48, 354
TOSS_Y = 243
TOSS_HEIGHT = 60           # peak of the arc above the stick heads

ball = Circle(TOSS_X1, TOSS_Y, 7, fill=rgb(195, 200, 208),
              border=rgb(140, 146, 158), borderWidth=1)
ball.t = 0                 # flight progress, 0 to 1
ball.direction = 1         # 1 = left-to-right, -1 = right-to-left

# --------------------------------------------------
# Scoreboard between the title and "vs Twin Valley".
# Hidden until the first goal is scored while the
# mouse is held down; resets on mouse release.
# --------------------------------------------------
app.score = 0
app.scoreFinal = False     # set when the mouse is released; freezes the score
app.netDone = False        # after the first release, the net never returns
scoreLabel = Label('0 - 0', 200, 201, size=20, bold=True,
                   fill='white', font='montserrat')
scoreboard = Group(
    Rect(150, 184, 100, 34, fill=NAVY, opacity=90,
         border='white', borderWidth=2),
    scoreLabel
)
scoreboard.visible = False

# --------------------------------------------------
# Subtle sparkle group
# --------------------------------------------------
sparkles = Group()
for x, y in [(118, 41), (300, 86), (330, 246),
             (210, 323), (155, 243)]:
    sparkles.add(Circle(x, y, 3, fill='white', opacity=45))

app.counter = 0

# --------------------------------------------------
# Animation
# --------------------------------------------------
def onStep():
    app.counter += 1

    # Floating translucent background circles
    for c in floaters:
        c.centerX += c.dx
        c.centerY += c.dy

        if c.centerX < -60 or c.centerX > 460:
            c.dx *= -1
        if c.centerY < -60 or c.centerY > 460:
            c.dy *= -1

    # Ball flies in a parabolic arc from one stick to the other,
    # then loops back the other way
    # Ball flies faster while shooting at the goal
    ball.t += 0.035 if goalCage.visible else 0.014
    if ball.t >= 1:
        ball.t = 0
        if goalCage.visible:
            # Landing in the net = a score (unless frozen)
            if ball.direction == 1 and not app.scoreFinal:
                app.score += 1
                scoreLabel.value = str(app.score) + ' - 0'
                scoreboard.visible = True
            # While the goal is out, always relaunch from the
            # left stick (no return toss)
            ball.direction = 1
        else:
            ball.direction *= -1

    t = ball.t if ball.direction == 1 else 1 - ball.t
    ball.centerX = TOSS_X1 + (TOSS_X2 - TOSS_X1) * t
    ball.centerY = TOSS_Y - TOSS_HEIGHT * 4 * t * (1 - t)

    # GO SPARTANS! pulses in size
    pulse = 24 + 3 * math.sin(app.counter / 8)
    goShadow.size = pulse
    goText.size = pulse

    # Sparkles twinkle
    if app.counter % 18 == 0:
        for s in sparkles:
            s.opacity = randrange(25, 70)

# --------------------------------------------------
# Click animation: little hype pulse
# --------------------------------------------------
def onMousePress(mouseX, mouseY):
    # Swap the right stick for the goal cage while held,
    # but only for the first press
    if not app.netDone:
        rightStick.visible = False
        goalCage.visible = True

def onMouseRelease(mouseX, mouseY):
    # Put the stick back; the net is done for good
    rightStick.visible = True
    goalCage.visible = False
    app.netDone = True

    # Letting go freezes the accumulated score
    if app.score > 0:
        app.scoreFinal = True

cmu_graphics.run()
