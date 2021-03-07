from qfunction import *
#from qfunction.plot import Plot
import matplotlib.pyplot as plt
global q 
#this.q = .9

print(q_exp(0,1))

t = np.linspace(-6,6,95)
y = [q_exp(float(i),.9) for i in t]
#Plot(t,x).savefig('test.png')


filenames = []
for i in range(len(t)):
	q = .8
	plt.plot(t[:i],[q_exp(float(s),.8) for s in t[:i]],label=f'q ={q}')
#plt.grid()
	print(f'foi {q}_{i}')
	q = .9
	plt.plot(t[:i],[q_exp(float(s),.9) for s in t[:i]],label=f'q={q}')
	q = 1.
	plt.plot(t[:i],[q_exp(float(s),1.0) for s in t[:i]],label=f'q={q}')
	q = 1.1
	plt.plot(t[:i],[q_exp(float(s),1.1) for s in t[:i]],label=f'q={q}')
	q = 1.2
	plt.plot(t[:i],[q_exp(float(s),1.2) for s in t[:i]],label=f'q={q}')
	plt.legend()
	plt.title(f'função exponencial deformada time [{i}]')
	plt.grid()
	#plt.plot(t[:i],[q_exp(float(s),.9) for s in t[:i]],label=f>
	filename = f'gif/plot{i}.png'
	filenames.append(filename)
	plt.savefig(filename)
	plt.cla()
	plt.clf()
	print(f'{i}/{len(t)} [{round(100*i/len(t),2)}% das fotos feitas]')


import os
import imageio

png_dir = ''
images = []
i = 0
for file_name in filenames:
    i += 1
    images.append(imageio.imread(file_name))
    print(f'produzindo gif {file_name}')
imageio.mimsave('movie.gif', images)

