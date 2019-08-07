'''This script shows turtle race according to the points kids get at the class'''

import turtle
from random import shuffle, choice, randint

#Setting up variables for students
colours = ['green', 'orange', 'blue', 'red', 'yellow', 'purple', 'pink', 'cyan']
student_names = ['Kid 4', 'Kid 3', 'Kid', 'Kid 0', 'Kid 1', 'Kid 2']
for ilist in [student_names, colours]:
	shuffle(ilist)
students = {}

#setting up variables for the screen
window = turtle.Screen()
window.title('Points')
turtle.bgcolor('black')
X,Y = window.screensize()
TSIZE = 60
TOP = Y-TSIZE
length = abs(X-TSIZE)*2
start = length//(len(student_names)+1)
zerox = TSIZE+start-X

def mark(name, num):
	students[name].speed = num

class Student:
	def __init__(self, name, colour, x1):
		self.name = name
		students[name] = self
		self.speed = 0
		self.colour = colour

		#setting staring position, shape, colour, writing a name 
		tur = turtle.Turtle()
		tur.penup()
		tur.setpos(x1, 40-Y)
		tur.color('white')
		tur.write(self.name, font = ('Arial', 16, "normal"), align = 'center')
		tur.setpos(x1, TSIZE-Y)
		tur.pendown()
		tur.shape('turtle')
		tur.color(colour)
		tur.left(90)
		self.tur = tur

	def draw_points(self):
		#if students got any points: show after turtle reaches it's max
		if self.speed:
			self.tur.penup()
			px,py = self.tur.pos()
			self.tur.color('white')
			self.tur.setpos(px,py-30)
			self.tur.write(self.speed, font = ('Arial', 16, "normal"), align = 'center')
			self.tur.color(self.colour)
			self.tur.setpos(px,py)
			self.tur.pendown()

	@property 
	def pos(self):
		return self.tur.pos()

	def move(self):
		#moving accoarding to speed. if reached the top - stop
		sx,sy = self.tur.pos()
		if self.speed + sy <= TOP:
			return self.tur.forward(self.speed)
		self.tur.setpos(sx, TOP)

#creating Student instances
for name in student_names:
	Student(name, colours.pop(), zerox)
	zerox += start

ilist = student_names[:]
for x in range(6):
	shuffle(ilist)
	mark(ilist.pop(), randint(1,15))

#running
def mainloop():
	try:
		i = max(s.pos[1] for s in students.values())
		while i < TOP:
			for s in students.values():
				s.move()
				if i < s.pos[1]: 
					i = s.pos[1]
		for s in students.values():
			s.draw_points()
		turtle.done()
	except Exception as e:
		print(e)

mainloop()


