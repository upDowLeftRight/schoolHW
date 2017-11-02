import tkinter, math, time, _thread, queue

class Mat2:
    def __init__(self, a, b, c, d):
        self.a1 = a#  |a1 a2|
        self.a2 = b#  |b1 b2|
        self.b1 = c
        self.b2 = d
    def vecMult(self, vec):
        return Vec2(self.a1*vec.a+self.a2*vec.b, self.b1*vec.a+self.b2*vec.b)
    def matMult(self, mat):
        return Mat2((self.a1 * mat.a1) + (self.a2 * mat.b1), (self.a1 * mat.a1) +(self.a2 * mat.b1),
                    (self.b1 * mat.a1) + (self.b2 * mat.b1), (self.b1 * mat.a1) +(self.b2 * mat.b1))
    def preMatMult(self, mat):
        return Mat2((mat.a1 * self.a1) + (mat.a2 * self.b1), (mat.a1 * self.a1) +(mat.a2 * self.b1),
                    (mat.b1 * self.a1) + (mat.b2 * self.b1), (mat.b1 * self.a1) +(mat.b2 * self.b1))
                    
class Vec2:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def degToRad(ang):
    return ang/180*math.pi

def makeRotMat(ang):
    return Mat2(math.cos(ang), -math.sin(ang), math.sin(ang), math.cos(ang))

def makeShearMat(shearFacX, shearFacY):
    return Mat2(1,shearFac,shearFacY,1)

def draw(vecs):
    coords = []
    c.create_line(WIDTH/2, 0, WIDTH/2,HEIGHT)
    c.create_line(0, HEIGHT/2, WIDTH, HEIGHT/2)
    for vec in vecs:
        coords.append([WIDTH/2+vec.a*50, HEIGHT/2-vec.b*50])
        #print("drawing")
    c.create_polygon(coords, fill = "#af01ea")
def graphics():
    while True:
        draw(vectors)
        c.update()
        #print("error")
        
WIDTH = 800
HEIGHT = 600

comQ = queue.Queue(10)

vectors = [Vec2(0,0), Vec2(1,0), Vec2(1,1), Vec2(0,1)]
w = tkinter.Tk()
c = tkinter.Canvas(w, width = WIDTH, height = HEIGHT)
c.pack()

#graphics()
_thread.start_new_thread(graphics,())
while True:
    command = input(">>> ")
