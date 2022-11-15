import pyglet
from pyglet import shapes

class Node:
    def __init__(self, vec):
        self.vec = vec
        self.left = None
        self.right = None
        self.top_right = [600,600]
        self.bot_left = [0,0]

class KDTree:
    def __init__(self, k):
        self.k = k
        self.root = None
    
    def insert(self, vec):
        if self.root == None:
            self.root = Node(vec);
            return

        new_node = Node(vec)
        tmp = self.root
        tmp2 = tmp
        height = 0
        while tmp is not None:
            tmp2 = tmp
            if tmp.vec[height % self.k] > new_node.vec[height % self.k]:
                tmp = tmp.left
            else:
                tmp = tmp.right
            height += 1

        height -= 1

        if tmp2.vec[height % self.k] > new_node.vec[height % self.k]:
            tmp2.left = new_node
            if self.k == 2:
                if height % self.k == 0:
                    new_node.top_right = [tmp2.vec[0], tmp2.top_right[1]]
                    new_node.bot_left = tmp2.bot_left
                else:
                    new_node.top_right = [tmp2.top_right[0], tmp2.vec[1]]
                    new_node.bot_left = tmp2.bot_left
        else:
            tmp2.right = new_node
            if self.k == 2:
                if height % self.k == 0:
                    new_node.top_right = tmp2.top_right
                    new_node.bot_left = [tmp2.vec[0], tmp2.bot_left[1]]
                else:
                    new_node.top_right = tmp2.top_right
                    new_node.bot_left = [tmp2.bot_left[0], tmp2.vec[1]]

    def search(self, vec):
        if self.root == None:
            return None

        tmp = self.root
        height = 0
        while tmp is not None:
            if tmp.vec[height % self.k] > vec[height % self.k]:
                tmp = tmp.left
            elif tmp.vec[height % self.k] < vec[height % self.k]:
                tmp = tmp.right
            else:
                return tmp
            height += 1

        return None


    def prin_in_order(self, node):
        if node is None:
            return
        self.prin_in_order(node.left)
        for i in range(self.k):
            print(node.vec[i], end=' ')
        print()
        self.prin_in_order(node.right)

    def print_in_order(self):
        self.prin_in_order(self.root)

kd = 2;
arbol = KDTree(kd)

def drawBoard(shape_list, batch=None):
    pre_order(arbol.root,0,shape_list,batch)

def pre_order(node, depth, shape_list, batch):
    if node is None:
        return
    point = shapes.Circle(node.vec[0],node.vec[1],10, batch=batch)
    
    if depth % 2 == 0:
        line = shapes.Line(node.vec[0],node.bot_left[1],node.vec[0],node.top_right[1],color=(255, 0, 0),batch=batch)
        shape_list.append(line)
    else:
        line = shapes.Line(node.bot_left[0],node.vec[1],node.top_right[0],node.vec[1],color=(0, 255, 0),batch=batch)
        shape_list.append(line)
    shape_list.append(point)

    pre_order(node.left, depth + 1, shape_list, batch=batch)
    pre_order(node.right, depth + 1, shape_list, batch=batch)



if __name__ == "__main__":
    xbound = 600
    ybound = 600
    arbol.insert([350,420])
    arbol.insert([520,100])
    arbol.insert([320,237])
    arbol.insert([200,134])
    arbol.insert([50,450])
    arbol.insert([270,350])

    if arbol.search([7,46]) is not None:
        print("Si esta")
    else:
        print("No esta")

    arbol.print_in_order()


    window = pyglet.window.Window(600, 600, "Visualizacion 2-D Tree")
    batch = pyglet.graphics.Batch()

    shape_list = []
    drawBoard(shape_list, batch=batch)


    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    pyglet.app.run()
    

    