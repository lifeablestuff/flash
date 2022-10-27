from fltk import *

class flash(Fl_Window):
	def __init__(self,w,h,l):
		Fl_Window.__init__(self,w,h,l)
		self.begin()
		self.but_list = []
		for x in range(3):
			self.but_list.append(Fl_Box(80+90*x,80,70,70))
			self.but_list[-1].box(FL_FLAT_BOX)
			self.but_list[-1].color(FL_GREEN)
		self.flash = Fl_Button(160,180,90,40,'flash')
		self.end()
		self.flash.callback(self.flash_cb)
	
	def flash_cb(self,wid):
		for x in range(len(self.but_list)):
			Fl.add_timeout(2.0+ 2.0*x,self.change_colour,x)
			Fl.add_timeout(3.0+ 2.0*x,self.change_back,x)
	
	def change_colour(self,num):
		self.but_list[num].color(FL_RED)
		Fl_Window.redraw(self)
	
	def change_back(self,num):
		self.but_list[num].color(FL_GREEN)
		Fl_Window.redraw(self)
			
			
		

app = flash(400,400,'stopwatch')
app.show()
Fl.run()

