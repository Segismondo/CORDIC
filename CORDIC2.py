from numpy import pi, sin, cos, arctan, sqrt

def get_angle(beta:str):
    if beta != "0":
        beta = beta.split("/")
        return pi/int(beta[1])
    else:
        return 0
    
def cordic(beta,N=40):
    ##the error factor for the number of iterations (rotations)
    def K_vals(n):
        K = []
        acc = 1.0
        for i in range(0, n):
            acc = acc * (1.0/sqrt(1 + 2.0**(-2*i)))
            K.append(acc)
        return K

    K = K_vals(N)
    ##sin(a) + cos(a) for a = 0
    x, y = 1, 0
    
    ##the main loop
    for i in range(0,N):
        ##go (counter)clockwise, because the desired angle is (larger) smaller
        d = 1.0
        if beta < 0:
            d = -1.0
        (x, y) = (x - (d * (2.0 ** (-i)) * y), (d * (2.0 ** (-i)) * x) + y)
        beta = beta - (d*arctan(2**(-i)))
        
    return K*x, K*y

if __name__ == '__main__':
    beta, n = input("Angle in radians, num of iterations like (ex. pi/2 30): ").split()
    beta, n = get_angle(beta), int(n)

    print("{0} Pi approximation: {1} {2}".format(5*"=",pi,5*"="))
    print("Actual cos(%f) = %f" % (beta, cos(beta)))
    print("Actual sin(%f) = %f\n" % (beta, sin(beta)))

    print("CORDIC in the works")

##    cos_val, sin_val = cordic(beta,3)
##    
##    print ("CORDIC cos(%f) = %f" % (beta, cos_val))
##    print ("CORDIC sin(%f) = %f" % (beta, sin_val))
