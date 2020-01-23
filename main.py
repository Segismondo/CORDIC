import CORDIC

beta,n = CORDIC.menu()
sin,cos = CORDIC.cordic(beta, n)
print("sin = %f\ncos = %f"% (sin, cos))
