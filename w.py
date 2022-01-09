import numpy as np
import pandas as pd
eng = pd.read_csv("sowpods.txt", header=None)
eng.columns = ["w"]
print(eng.shape)
ww = eng.w
step,current = 0,0


def inc(step,current,ww):
    maxx=len(ww)
    step = step+1
    delta=np.maximum(1,maxx//2**(step))
    current=current+delta
    for i in range(-5,5):
        print(ww[current+i])
    return step,current

def dec(step,current,ww):
    maxx=len(ww)
    step = step+1
    delta=np.maximum(1,maxx//2**(step))
    current=current-delta
    for i in range(-5, 5):
        print(ww[current+i])
    return step,current

def next5(current,ww):
    for i in range(5):
        print(ww[current+i])
    return current

step,current = inc(step,current,ww)
print(step,current)

while(True):
	nn = input("j or k? ")

	if (nn=="j"):
		step,current = dec(step,current,ww)
		print(step,current)
	elif (nn=="k"):
		step,current = inc(step,current,ww)
		print(step,current)
	else:
		step,current = 0,0
		print('reset')
		step,current = inc(step,current,ww)
		print(step,current)
