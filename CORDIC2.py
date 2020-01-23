import numpy

def get_angle(beta:str):
    beta = beta.split("/")
    return numpy.pi/int(beta[1])

def cordic_trig(beta,N=40):
    def K_vals(n):
        K = []
        acc = 1.0
        for i in range(0, n):
            acc = acc * (1.0/numpy.sqrt(1 + 2.0**(-2*i)))
            K.append(acc)
        return K


    K = K_vals(N)
    atans = [numpy.arctan(2.0**(-i)) for i in range(0,N)]
    x = 1
    y = 0

    for i in range(0,N):
        d = 1.0
        if beta < 0:
            d = -1.0

        (x, y) = (x - (d * (2.0 ** (-i)) * y), (d * (2.0 ** (-i)) * x) + y)
        beta = beta - (d*numpy.arctan(2**(-i)))
    return K*x, K*y

if __name__ == '__main__':
    beta, n = input("Angle in radians, num of iterations like (ex. pi/2 30): ").split()
    beta, n = get_angle(beta), int(n)

    print("Actual cos(%f) = %f" % (beta, numpy.cos(beta)))
    print ("Actual sin(%f) = %f\n" % (beta, numpy.sin(beta)))

##    cos_val, sin_val = cordic_trig(beta,3)
##    
##    print ("CORDIC cos(%f) = %f" % (beta, cos_val))
##    print ("CORDIC sin(%f) = %f" % (beta, sin_val))
