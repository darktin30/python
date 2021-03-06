import math
import numpy as np
import numdifftools as nd

def f(x):
    	return np.array([ 1-7*x[0]+3*math.pow(x[0],3)+4*x[1]-3*math.pow(x[1],3), -6+4*math.pow(x[0],2)+4*math.pow(x[1],4) ])

def newton(x):
	f_jacob = nd.Jacobian(f)
	f_j = f_jacob(x)
	det = np.divide(1,np.linalg.det(f_j))
	f_j_i = np.multiply(det, np.array([[f_j[1][1],-f_j[0][1]],[-f_j[1][0], f_j[0][0]]]))
	new_x = np.dot(f_j_i, f(x))
	new_x = np.subtract(x, new_x)
	return new_x
	

def main(steps, x):
	print("Iteration for ", steps, " steps with x0 = ", x)
	
	for i in range(steps):
		 x = newton(x)
		print("x",i+1," = ",x)
	
	print()
		
	
	
	
		
		

main(5, [0, 1])
