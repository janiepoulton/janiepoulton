'''
Janie Poulton
CSCI 203 Section 2
Final Program
December 6th, 2019
Sources consulted: class notes, chapter slides, tutor Blake Adams

By submitting this work, I attest that it is my original work and that I did not violate
the University of Mississippi academic policies set forth in the M book.

My program has a background of transparent flowers that are changing color by row at random.
There are two mouse-tracking flowers that are inversly related to one another in size and position.
When you move your mouse up and down the y-axis the flowers get larger and smaller.
When you move your mouse across the x-axis they switch position.
*Move your mouse in a circular motion and they display a 3D effect traveling around one another.* 
When you clap your hands or make sound the petals on the flower rotate.
When you press your mouse the background darkens or lightens.
'''


add_library('sound')

#global variable
pressed = False

r = []
g = []
b = []

angle = 0

def setup():
    size(1000,500)
    background(252,239,120)
    global r, g, b
    
    global mic, vol
    mic = AudioIn(this,0)
    vol = Amplitude(this)
    
    mic.start()
    
    vol.input(mic)
    
    for i in range(100):
        r.append(random(255))
        g.append(random(255))
        b.append(random(255))
    
def mousePressed():
    global pressed
    pressed = not pressed
    
        
def draw():
    global r,g,b, angle
    strokeWeight(1)
    stroke(255)
    
    soundLevel = map(vol.analyze(), 0, 1, 1, 100)
    
    if pressed:
        background(255,198,8)
    else:
        background(252,239,120)
    
    #grid detail
    stroke(255,198,8)
    for i in range(20, 990, 50):
        index = 0
        for j in range(20, 490, 50):
            fill(r[index], g[index], b[index], 10)
            star(i, j, 0)
            index += 1
    
    #shape movement
    x = mouseX
    y = mouseY
    w = width - mouseX #inverse X
    h = height - mouseY #inverse Y
    
    pushMatrix()
    translate(x, height/2)
    fill(252,20,168,50)
    n = map(mouseY,0,500,.5,10)
    scale(n)
    star(0,0, angle)
    fill(20,204,252,50)
    popMatrix()
    
    pushMatrix()
    translate(w, height/2)
    n = map(mouseY,0,500,10,.5)
    scale(n)
    star(0,0, angle)
    popMatrix()
    
    angle += soundLevel
    print(angle)
    
    for i in range(100):
        r[i] = random(255)
        g[i] = random(255)
        b[i] = random(255)
    
    
#user defined function 
def star(x,y,angle):
    stroke(255)
    strokeWeight(.5)
    pushMatrix()
    translate(x,y)
    rotate(radians(angle))
    ellipse(0,0,10,50)
    ellipse(0,0,50,10)
    rotate(radians(angle+45))
    ellipse(0,0,10,50)
    ellipse(0,0,50,10)
    popMatrix()
