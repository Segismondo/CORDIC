import math


def cordic_trig(beta,N=40):
    def K_vals(n):
        K = []
        acc = 1.0
        for i in range(0, n):
            acc = acc * (1.0/math.sqrt(1 + 2.0**(-2*i)))
            K.append(acc)
        return K


    K = 0.6072529350088812561694
    atans = [math.atan(2.0**(-i)) for i in range(0,N)]
    x = 1
    y = 0

    for i in range(0,N):
        d = 1.0
        if beta < 0:
            d = -1.0

        (x, y) = (x - (d * (2.0 ** (-i)) * y), (d * (2.0 ** (-i)) * x) + y)
        beta = beta - (d*math.atan(2**(-i)))
    return K*x, K*y

if __name__ == '__main__':
    beta = math.pi
    print("Actual cos(%f) = %f" % (beta, math.cos(beta)))
    print ("Actual sin(%f) = %f" % (beta, math.sin(beta)))
    cos_val, sin_val = cordic_trig(beta)
    print ("CORDIC cos(%f) = %f" % (beta, cos_val))
    print ("CORDIC sin(%f) = %f" % (beta, sin_val))