from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='color', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.shape_var = StringVar()
        self.shape_var.set('None')  # default value
        self.shape_menu = OptionMenu(self.root, self.shape_var, 'None', 'T-shirt', 'Pant', 'Frock', 'Skirt', 'Shoes', command=self.update_paint_mode)
        self.shape_menu.grid(row=0, column=5)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=6)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.paint_mode = 'pen'
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def update_paint_mode(self, shape):
        if shape == 'None':
            self.paint_mode = 'pen'
        else:
            self.paint_mode = shape

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.paint_mode == 'pen':
            if self.old_x and self.old_y:
                self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                                   width=self.line_width, fill=paint_color,
                                   capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.old_x = event.x
            self.old_y = event.y
        else:
            if self.paint_mode == 'T-shirt':
                self.draw_tshirt(event.x, event.y, paint_color)
            elif self.paint_mode == 'Pant':
                self.draw_pant(event.x, event.y, paint_color)
            elif self.paint_mode == 'Frock':
                self.draw_frock(event.x, event.y, paint_color)
            elif self.paint_mode == 'Skirt':
                self.draw_skirt(event.x, event.y, paint_color)
            elif self.paint_mode == 'Shoes':
                self.draw_shoes(event.x, event.y, paint_color)

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def draw_tshirt(self, x, y, color):
        self.c.create_rectangle(x, y, x+50, y+100, fill='', outline=color)

    def draw_pant(self, x, y, color):
        self.c.create_rectangle(x, y, x+20, y+100, fill='', outline=color)
        self.c.create_rectangle(x+30, y, x+50, y+100, fill='', outline=color)

    def draw_frock(self, x, y, color):
        self.c.create_polygon(x, y, x+50, y, x+50, y+100, x, y+100, fill='', outline=color)

    def draw_skirt(self, x, y, color):
        self.c.create_oval(x, y, x+50, y+100, fill='', outline=color)

    def draw_shoes(self, x, y, color):
        self.c.create_rectangle(x, y, x+50, y+20, fill='', outline=color)
        self.c.create_rectangle(x, y+30, x+50, y+50, fill='', outline=color)


if __name__ == '__main__':
    Paint()