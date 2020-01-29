'''
This:
    -gets angle beta and number of iterations
    -draw actual cos(B) + sin(B)
    -draws the vector (0,0) -> cos(Bi) + sin(Bi) in each iteration
'''

import CORDIC
import plotter
from decimal import Decimal

beta,n, = CORDIC.menu()
cos_init, sin_init = CORDIC.init(beta)

plotter.init()
plotter.plot_line(cos_init,sin_init,style='o:g')

for i in range(0,n):
    cos,sin = CORDIC.cordic(beta, i+1)
    print("iteration = %d\nsin = %f\ncos = %f\n"% (i+1,sin, cos))
    plotter.plot_line(cos,sin) if i < n-5 else plotter.plot_line(cos,sin,annotate=True)

plotter.plot_line(cos_init,sin_init,style='D:g',annotate=True)

input("Any key to terminate...")

