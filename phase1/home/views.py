from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    context = {
        "variable": "lokesh is luffy"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
        return render(request, 'about.html')

def services(request):
         return render(request, 'services.html')

def contact(request):
    success = False
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        success = True
    return render(request, 'contact.html', {'success': success})

import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Upgraded Reptite Creature")
screen.setup(width=1000, height=800)
screen.tracer(0)

# Settings
NUM_SEGMENTS = 30
SEGMENT_LENGTH = 12
LEG_LENGTH = 18
WAVE_SPEED = 0.15
WAVE_AMPLITUDE = 8
TOE_LENGTH = 5

# Segment state
positions = [[0, 0] for _ in range(NUM_SEGMENTS)]
angles = [0 for _ in range(NUM_SEGMENTS)]
frame = 0

# Drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(2)
pen.speed(0)

# Color gradient from head to tail
def get_segment_color(i):
    shade = int(255 - (i / NUM_SEGMENTS) * 150)  # lighter head
    return (shade, shade, shade)

def set_pen_color(rgb):
    r, g, b = [c / 255 for c in rgb]
    turtle.colormode(1.0)
    pen.color((r, g, b))

def follow_mouse(x, y):
    dx = x - positions[0][0]
    dy = y - positions[0][1]
    angle = math.atan2(dy, dx)
    positions[0] = [x, y]
    angles[0] = angle

    for i in range(1, NUM_SEGMENTS):
        tx, ty = positions[i - 1]
        dx = tx - positions[i][0]
        dy = ty - positions[i][1]
        angle = math.atan2(dy, dx)

        wave = math.sin(frame * WAVE_SPEED + i * 0.5) * math.radians(WAVE_AMPLITUDE)
        angle += wave if i > NUM_SEGMENTS // 2 else 0  # tail wiggle only

        angles[i] = angle
        positions[i][0] = tx - math.cos(angle) * SEGMENT_LENGTH
        positions[i][1] = ty - math.sin(angle) * SEGMENT_LENGTH

def draw_creature():
    pen.clear()

    # Draw spine
    pen.penup()
    pen.goto(positions[0])
    pen.pendown()
    for i in range(1, NUM_SEGMENTS):
        set_pen_color(get_segment_color(i))
        pen.goto(positions[i])

    # Draw legs with toes
    for i in range(3, NUM_SEGMENTS, 4):
        x, y = positions[i]
        angle = angles[i]
        leg_angle = angle + math.pi / 2
        wiggle = math.sin(frame * 0.3 + i) * 6
        leg_angle += math.radians(wiggle)

        lx = math.cos(leg_angle) * LEG_LENGTH
        ly = math.sin(leg_angle) * LEG_LENGTH

        # Draw left leg
        leg_x1, leg_y1 = x + lx, y + ly
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.goto(leg_x1, leg_y1)

        # Toes for left leg
        toe_angle = math.pi / 6
        for offset in [-toe_angle, 0, toe_angle]:
            toe_dx = math.cos(leg_angle + offset) * TOE_LENGTH
            toe_dy = math.sin(leg_angle + offset) * TOE_LENGTH
            pen.penup()
            pen.goto(leg_x1, leg_y1)
            pen.pendown()
            pen.goto(leg_x1 + toe_dx, leg_y1 + toe_dy)

        # Draw right leg
        leg_x2, leg_y2 = x - lx, y - ly
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.goto(leg_x2, leg_y2)

        # Toes for right leg
        for offset in [-toe_angle, 0, toe_angle]:
            toe_dx = math.cos(leg_angle + math.pi + offset) * TOE_LENGTH
            toe_dy = math.sin(leg_angle + math.pi + offset) * TOE_LENGTH
            pen.penup()
            pen.goto(leg_x2, leg_y2)
            pen.pendown()
            pen.goto(leg_x2 + toe_dx, leg_y2 + toe_dy)

    screen.update()

def update():
    global frame
    frame += 1
    x = screen.cv.winfo_pointerx() - screen.cv.winfo_rootx() - screen.window_width() // 2
    y = screen.window_height() // 2 - (screen.cv.winfo_pointery() - screen.cv.winfo_rooty())

    follow_mouse(x, y)
    draw_creature()
    screen.ontimer(update, 30)

update()
screen.mainloop()