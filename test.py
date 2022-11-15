import pyglet
from pyglet import shapes

title = "Tic Tac Toe"

window = pyglet.window.Window(600, 600, title)

batch = pyglet.graphics.Batch()


def foo():
    pyglet.app.run()
def drawBoard(shape_list, batch=None):
    circle = shapes.Circle(300,150,10,color=(50,225,30),batch=batch)
    shape_list.append(circle)
    for i in range(100, 600, 100):
        linex = shapes.Line(i, 0, i, 600, width=2, color=(0, 230, 0), batch=batch)
        linex.opacity = 250
        shape_list.append(linex)
        liney = shapes.Line(0, i, 600, i, width=2, color=(0, 230, 0), batch=batch)
        liney.opacity = 250
        shape_list.append(liney)

shape_list = []
drawBoard(shape_list, batch=batch)

@window.event
def on_draw():
    window.clear()
    batch.draw()

foo()