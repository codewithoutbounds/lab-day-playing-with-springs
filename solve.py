# Credit for code goes to http://bulldog2.redlands.edu/facultyfolder/deweerd/tutorials/Tutorial-ODEs.pdf.
# This code is heavily based on the above link, which is fantastic if you want to know more.

from scipy.integrate import odeint
from pylab import *

def derivatives(y, t):
    m = 10 # mass is 10 kg
    c = 2 # damping constant is 2 N/m/s
    k = 5  # spring constant is 5 N/m
    return array([y[1], (-c*y[1]-k*y[0])/m]) # we return x' and y', as y[0] is x and y[1] is y

time = linspace(0.0, 50.0, 1000) # get 1000 points from 0 to 50
init = array([1, 50]) # here we give initial x and y, position and velocity
sol = odeint(derivatives, init, time) # and now we find our solutions

figure() # create a new figure
plot(time, sol[:, 0]) # solver gave us back both x and y values - just plot x
xlabel('time')
ylabel('position') # we set our labels
show() # and display it all

    
