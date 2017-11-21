from random import random,randint
import math

class BoundsRedefinitionException(Exception):
    pass

class ChaseActor(object):
    """This is a mobile random walk actor in a continuous chase scenario.
    
    Keyword arguments:
    x_i -- Initial x position (default 0.0)
    y_i -- Initial y position (default 0.0)
    bounds -- symetrical (x,y) bounds in tuple form (default None)
    """
    def __init__(self,x_i=0.,y_i=0.,bounds = None):
        """
        """
        self.x = x_i
        self.y = y_i
        self.curr_count = 0
        self.curr_head = (0.,0.)
        self.bounds = bounds

    def walk(self):
        """Function that takes a single step in the random walk."""
        if self.curr_count == 0:
            self.curr_head = (2*random()*math.pi,1+(random()*9))
            self.curr_count = randint(1,10)

        self.x = max(min(self.x + math.cos(self.curr_head[0])*self.curr_head[1],self.bounds[0]),-self.bounds[0])
        self.y = max(min(self.y + math.sin(self.curr_head[0])*self.curr_head[1],self.bounds[1]),-self.bounds[1])
        self.curr_count -= 1

    def set_bounds(self,bounds):
        """Update the bounds for the current actor. Raises BoundsRedefinitionException if redefinition is attempted."""
        if self.bounds is None:
            self.bounds = bounds
        else:
            raise BoundsRedefinitionException("Bounds have already been defined for this actor. If createing a new chase use a new actor.")
    
class StationaryActor(object):
    """This is the stationary actor in a continuous chase scenario."""
    def __init__(self,x_i=0.,y_i=0.):
        """Creates a new stationary actor with initial position, default is 0,0. 
    
        Keyword arguments:
        x_i -- Initial x position (default 0.0)
        y_i -- Initial y position (default 0.0)
        """
        self.x = x_i
        self.y = y_i

    def walk(self):
        pass
    
    def set_bounds(self,bounds):
        pass

if __name__ == "__main__":
    c_actor = ChaseActor()
    c_actor.set_bounds((1000,1000))
    for i in range(1000):
        c_actor.walk()
        print(c_actor.x,c_actor.y)
        
        
