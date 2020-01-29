import matplotlib.pyplot as plt

ORIGIN, RADIUS = (0,0),1

def init():
    '''draws the unit circle in the first quadrant'''
    ##interactive mode
    plt.ion()
    fig = plt.figure()
    plt.title("The unit circle")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    
    global ax
    ax = fig.add_subplot()

    ##axis
    X_AXIS = plt.plot([-1,1],[0,0],'k')
    Y_AXIS = plt.plot([0,0],[-1,1],'k')
    
    ##our unit circle
    circle = plt.Circle(ORIGIN,RADIUS,edgecolor='k',facecolor='None')
    ax.add_patch(circle)

def plot_line(x:float,y:float,style='o:r',scale=0,annotate=False):
    '''draws a red line from (0,0) to (x,y) and waits 0.5 s'''
    line, = ax.plot((0,x),(0,y),style,scalex=scale,scaley=scale)
    if annotate:
        ax.annotate('(%.16f, %.16f)' % (x,y), xy=(x,y), textcoords='data') 
    plt.pause(0.5)

if __name__ == '__main__':
    init()
    input("Press key to terminate...")
