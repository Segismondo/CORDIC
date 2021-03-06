from numpy import pi, sin, cos, arctan, sqrt

def get_angle(beta:str):
    '''returns floating-point value of a symbolic string pi/n'''
    return eval(beta)

def error(n):
    '''returns the error factor for the number of iterations (rotations)'''
    K = 1.0
    for i in range(0, n):
        K = K * (1.0/sqrt(1 + 2.0**(-2*i)))
    return K

def cordic(beta:float,n:int,K=None):
    '''returns cos and sin of beta, calculated using CORDIC algorithm'''
    ##(cos(a) + sin(a)) tuple for a = 0, error after N iterations
    point = (1, 0)
    if K==None:
        K = error(n)
    ##the main loop (basically binary search, lol)
    for i in range(0,n):
        ##go (counter)clockwise, because the desired angle is (larger) smaller
        d = 1.0
        if beta < 0:
            d = -1.0
        x, y    = point[0], point[1]
        point   = (x - (d * (2.0 ** (-i))) * y, y +  (d * (2.0 ** (-i))))
        beta    = beta - (d*arctan(2**(-i)))
        
    return K*point[0], K*point[1]

def menu():
    beta, n = input("Angle in radians, num of iterations like (ex. pi/2 30): ").split()
    beta, n = get_angle(beta), int(n)
    return beta, n

def init(beta:float):
    '''returns cos and sin of beta, calculated with numpy'''
    return cos(beta), sin(beta),

if __name__ == '__main__':
    beta, n = menu()

    print("{0} Pi approximation: {1} {2}".format(5*"=",pi,5*"="))
    print("Actual cos(%f) = %f" % (beta, cos(beta)))
    print("Actual sin(%f) = %f\n" % (beta, sin(beta)))

    cos_val, sin_val = cordic(beta,n)
    
    print ("CORDIC cos(%f) = %f" % (beta, cos_val))
    print ("CORDIC sin(%f) = %f" % (beta, sin_val))
