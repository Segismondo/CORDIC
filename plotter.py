import matplotlib.pyplot as plt

def init():
    '''draws the unit circle in the first quadrant'''
    ##interactive mode
    plt.ion()
    fig = plt.figure()
    global ax
    ax = fig.add_subplot(1, 1, 1)
    ##our unit circle
    circle = plt.Circle((0,0),1,edgecolor='k',facecolor='None')
    ax.add_patch(circle)

def plot_line(x:float,y:float,style='D:r',scale=0):
    '''draws a red line from (0,0) to (x,y) and waits 0.1 s'''
    line, = ax.plot((0,x),(0,y),style,scalex=scale,scaley=scale)
    plt.pause(0.5)
