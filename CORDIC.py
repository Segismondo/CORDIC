from numpy import pi, sin, cos, arctan, sqrt

def get_angle(beta:str):
    if beta != "0":
        beta = beta.split("/")
        return pi/int(beta[1])
    else:
        return 0
    
def cordic(beta:float,N:int):
    ##the error factor for the number of iterations (rotations)
    def error(n):
        K = 1.0
        for i in range(0, n):
            K = K * (1.0/sqrt(1 + 2.0**(-2*i)))
        return K

    ##(sin(a) + cos(a)) tuple for a = 0, error after N iterations
    point, K = (1, 0), error(N)
    ##the main loop (basically binary search, lol)
    for i in range(0,N):
        ##go (counter)clockwise, because the desired angle is (larger) smaller
        d = 1.0
        if beta < 0:
            d = -1.0
        x, y    = point[0], point[1]
        point   = (x - (d * (2.0 ** (-i))) * y, d * (2.0 ** (-i)) * x + y)
        beta    = beta - (d*arctan(2**(-i)))
        
    return K*point[0], K*point[1]

if __name__ == '__main__':
    beta, n = input("Angle in radians, num of iterations like (ex. pi/2 30): ").split()
    beta, n = get_angle(beta), int(n)

    print("{0} Pi approximation: {1} {2}".format(5*"=",pi,5*"="))
    print("Actual cos(%f) = %f" % (beta, cos(beta)))
    print("Actual sin(%f) = %f\n" % (beta, sin(beta)))

##    print("CORDIC in the works")

    cos_val, sin_val = cordic(beta,n)
    
    print ("CORDIC cos(%f) = %f" % (beta, cos_val))
    print ("CORDIC sin(%f) = %f" % (beta, sin_val))
