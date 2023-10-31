import pgzrun
box1 = Rect((250,250),(50,50))

def draw():
    screen.fill('white') 
    screen.draw.filled_rect(box1, "red")

def update():
    if keyboard.left:
        box1.x -=5
    if keyboard.right:
         box1.x +=5
    if keyboard.up:
         box1.y -=5
    if keyboard.down:
         box1.y +=5
pgzrun.go()         
        #