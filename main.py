'''
This:
    -gets angle beta and number of iterations
    -draw actual cos(B) + sin(B)
    -draws the vector (0,0) -> cos(Bi) + sin(Bi) in each iteration
'''

import CORDIC
import plotter

beta,n, = CORDIC.menu()
sin_init,cos_init = CORDIC.init(beta)

plotter.init()
plotter.plot_line(cos_init,sin_init,style='o:g')

for i in range(0,n):
    cos,sin = CORDIC.cordic(beta, i+1)
    print("sin = %f\ncos = %f"% (sin, cos))
    plotter.plot_line(cos,sin)



