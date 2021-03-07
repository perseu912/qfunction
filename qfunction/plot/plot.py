#biblioteca de plotagem 12:35 18/01/2020
#Reinan Bezerra
import matplotlib.pyplot as plt
import imageio
import cv2
import numpy as np

#fig = plt.figure()

class Plot:
	def __init__(self,x,y,label=None,kind=None,c=None):
		import matplotlib.pyplot as plt
		self.x = x
		self.y = y
		self.label = label
		self.kind = kind
		self.c = c

		self.plt = plt

		self.plt.plot(x,y,label=label,kind=kind,c=c)
	
	def savefig(self,namefile,dpi):
		self.plt.savefig(namefile,dpi=dpi)


