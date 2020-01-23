import CORDIC

beta,n = CORDIC.menu()
sin,cos = CORDIC.cordic(beta, n)
print("sin = %f\ncos = %f"% (sin, cos))

'''
This will:
    -get angle beta and number of iterations
    -draw actual cos(B) + sin(B)
    -draw the vector (0,0) -> cos(Bi) + sin(Bi) in each iteration
    Ima start working, so that we pass the maths classes xD
'''
