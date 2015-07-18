import maya.cmds as cmds
import random



class growth():


#Growth is a multi-functional modeling tool.
#Its versatility extends for individual geometry and also for edges that they belong to.
#The x,y,z, angles and scales are changeable, but at least one edge and one angle should be selected.
#It is automatically set to randomize the entirety of the geometry with every click of the button "grow".
#But, the user can select any edge of the geometry and adjust its extrusion values. 
#Also, if one selects a lone edge and click "grow", the edge itself becomes a changing line that can be manipulated.
#The user can then opt to click on the entire geometry and click "grow" again to extrude the faces out 
#of the line that is made out of various edges. 
#In summary, Growth has three main functions:
#1) controlled geometry extrusion based on x,y,z choices
#2) randomized geometry extrusion after the first click of "grow"
#3) controlled and randomized extrusion of the edges of a given geometry. 

#Created by Minha Lee 
#Last modified by Minha Lee on 05/09/10
#0minhalee0@gmail.com



	def __init__(self):
		self.name="growthUI"
		self.title="growth"
		if(cmds.window(self.name, exists=True,query=True)):
			cmds.deleteUI(self.name)
		self.window=cmds.window(self.name, title=self.title)
		self.form= cmds.formLayout()
		self.windowHeight = 300
		self.windowWidth = 100
		cmds.columnLayout(columnAlign="center")
		cmds.text(label="angleX")
		self.fltSliderXangle=cmds.floatSlider("angleX", min=-5, max=5, value=0, step=0.1)
		cmds.text(label="angleY")
		self.fltSliderYangle=cmds.floatSlider("angleY", min=-5, max=5, value=0, step=0.1)
		cmds.text(label="angleZ")
		self.fltSliderZangle=cmds.floatSlider("angleZ", min=-5, max=5, value=0, step=0.1)
		cmds.text(label="scaleX")
		self.fltSliderXscale=cmds.floatSlider("scaleX", min=-5, max=5, value=0, step=0.1)
		cmds.text(label="scaleY")
		self.fltSliderYscale=cmds.floatSlider("scaleY", min=-5, max=5, value=0, step=0.1)
		cmds.text(label="scaleZ")
		self.fltSliderZscale=cmds.floatSlider("scaleZ", min=-5, max=5, value=0, step=0.1)
		self.growth_size_button=cmds.button(label='grow', align="center", height=50, width=100, command=self.process)
		cmds.showWindow(self.window)
	

	def queryAngle(self):
		angleVariableX= cmds.floatSlider("angleX",q=True, v=True)
		print angleVariableX
		angleVariableY= cmds.floatSlider("angleY", q=True, v=True)
		print angleVariableY
		angleVariableZ= cmds.floatSlider("angleZ", q=True, v=True)
		print angleVariableZ
		valsAngle = [angleVariableX, angleVariableY, angleVariableZ]
		print valsAngle
		return valsAngle	

		
			
	def process(self, *args):
		valsAngle = self.queryAngle()
		self.face(valsAngle)
		
	def face(self, angle):
		self.poly=cmds.ls(selection=1)[0]
		edge= cmds.polyListComponentConversion (self.poly, fromFace=1, toEdge=1)
		flattenE= cmds.ls(selection=1, flatten=1)
		r=random.choice(flattenE)
		if (self.poly==[ ]):
			pass
		else:
	
			angleVariableChange=cmds.polyExtrudeEdge(r,keepFacesTogether=False, localTranslate=(angle[0],angle[1],angle[2]), localScale=(angle[0],angle[1],angle[2]), rotate=(angle[0],angle[1],angle[2]) )
			return(edge)
		

		
		
		


growth = growth()	
