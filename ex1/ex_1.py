from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np


data_1, data_2 = np.loadtxt('ex1data1.txt',
                 unpack = True,
                 delimiter = ",")
plt.plot(data_1, data_2 , '+', label='Training Data')
plt.legend(loc='best')

plt.xlabel("Population of City in 10,000s")
plt.ylabel('Profit in $10,000s')


X = data_1
y = data_2

a = np.array([data_2])   # load in data in array
y = a.T                 #transpose it to for later addition

##print("a.shape",a.shape)


m = len(y)

def computeCost(X, y, theta):
    m = len(y)
    J = 0
    x_theta = np.matmul(X, theta)
    x_theta_y = x_theta - y
    x_theta_y_squared = x_theta_y * x_theta_y
##    J = (1/(2*m)) * sum(((np.matmul(X, theta))-y))
##    J = (1/(2*m)) * sum(  ((  np.matmul(X, theta)  )  -y)**2  )
    J = (1/(2*m)) * sum(x_theta_y_squared)
    return J


ones_vec = np.ones((len(data_1),))

X = np.c_[ones_vec, X]


theta = np.zeros((2,1))


theta_test = theta
theta_test[0] =0
theta_test[1] = 0


x_theta = np.matmul(X, theta)
x_theta_y = x_theta - y

i = x_theta + y


iterations = 1500
alpha = 0.01

##J = computeCost(X, y, theta_test)

print("With theta = [0 ; 0] ")
print("Expected cost value (approx) 32.07")
print("J =", end = "")
print(computeCost(X, y, theta_test))

print(" ") 

print("With theta = [-1 ; 2]")
print("Expected cost value (approx) 54.24")
print("J =", end = " ")

theta_2 = theta
theta_2[0] = -1
theta_2[1] = 2

print(computeCost(X, y, theta_2))
print(" ")


#X[:,:2]


def gradientDescent(X, y, theta, alpha, num_iters):
    m = len(y)
    J_history = np.zeros((num_iters,1))

    for i in range(num_iters):
        x_theta = np.matmul(X, theta)
        x_theta_y = x_theta - y
##        temp0 = theta[0] - ((alpha/m)*sum(((X * theta) - y)))    
        temp0 = theta[0] - ((alpha/m)*sum(x_theta_y))
##        temp1 = theta[1] - ((alpha/m)*sum(((X * theta) - y).*X(:,2)));
        temp1_term_0 = (alpha/m)
        X_term = X[ : , 1] 
        X_term_dim = np.array([X_term]) #create (1,x) array, transpose to get (x,1). should be easier.
        X_ready = X_term_dim.T 
        temp1_term_1 = sum(np.multiply(x_theta_y, X_ready))
        temp1 = theta[1] - temp1_term_0*temp1_term_1     
        

        theta[0] = temp0
        theta[1] = temp1
##        print(temp0,temp1)
        J_history[i] = computeCost(X, y, theta)
##    print(">>>", theta[1],theta[0])
    return theta[0],theta[1]

theta = np.zeros((2,1))

theta = gradientDescent(X, y, theta, alpha, iterations)
print("Expected theta values (approx)");
print(" -3.6303   1.1664");
print("Theta >>",theta)
        


X_term = X[ : , 1]
X_term_dim = np.array([X_term])#create (1,x) array, transpose to get (x,1). should be easier. 
X_ready = X_term_dim.T 
x_theta = np.matmul(X, theta)
plt.plot(X_ready,x_theta , '-', label='Fit')
plt.legend(loc='best')
















plt.show()

