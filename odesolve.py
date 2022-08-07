# odesolve.py
#
# Author: <insert name>
# Date:   <insert date>
# Description: <insert description>
#
# You should fill out the code for the functions below so that they pass the 


import matplotlib.pyplot as plt

#euler method function
def euler(f, x, t, h):
    """Perform one step of the Euler method"""
    return x + f(x, t)*h
    pass

#rk4 method function
def rk4(f, x, t, h):
    """Perform one step of the RK$ method"""
    k1 = f(x, t)
    k2 = f((x + k1*(h/2)), (t + (h/2)))
    k3 = f((x + k2*(h/2)), (t + (h/2)))
    k4 = f((x + k3*h), (t + h))
    k = (k1 + 2*k2 + 2*k3 + k4)
    return x + (k*(h/6))
    pass


def solveto(f, x1, t1, t2, hmax, method=euler):
    """Use many steps of method to get from x1,t1 to x2,t2"""
    
    
    if method == rk4:
        
        global rk4_estimation
        global t_list
        
        while t1 < t2:
            #setting up lists to append the estiomated values to 
            rk4_estimation = [x1]
            t_list = [t1]
            
            # only runs if the hmax is at its normal value
            if (t2 - t1) >= hmax:
                
                k1 = f(x1, t1)
                k2 = f((x1 + k1*(hmax/2)), (t1 + (hmax/2)))
                k3 = f((x1 + k2*(hmax/2)), (t1 + (hmax/2)))
                k4 = f((x1 + k3*hmax), (t1 + hmax))
                k = (k1 + 2*k2 + 2*k3 + k4)
                #adds the updated values to the list
                rk4_estimation.append(k*(hmax/6))
                #updates the vlues of x and t
                x1 = x1 + (k*(hmax/6))
                t1 = t1 + hmax
                t_list.append(t1 + hmax)
                
                # only runs when hmax changes to jump to x2
            else:
                hmax = (t2 - t1)
                t1 = t2
                
                k1 = f(x1, t1)
                k2 = f((x1 + k1*(hmax/2)), (t1 + (hmax/2)))
                k3 = f((x1 + k2*(hmax/2)), (t1 + (hmax/2)))
                k4 = f((x1 + k3*hmax), (t1 + hmax))
                k = (k1 + 2*k2 + 2*k3 + k4)
                rk4_estimation.append(k*(hmax/6))
                t_list.append(t2)
        
        #adds the values in the list to give the final position of the ode at point t2
        rk4_value = sum(rk4_estimation)
                
        print (rk4_value)
        
        return rk4_value
        
    #only runs when the method isnt rk4
    else:

        global estimation
        global t_euler_list
        
        
        while t1 < t2:
            
            estimation = [x1]
            t_euler_list = [t1]
            
            # only runs if the hmax is at its normal value
            if (t2 - t1) >= hmax:
                estimation.append(f(x1, t1)*hmax)
                t_euler_list.append(t1 + hmax)
                x1 = x1 + f(x1, t1)*hmax
                t1 = t1 + hmax
            
                
                
            # only runs when hmax changes to jump to x2
            else:
                hmax = t2 - t1
            
                t1 = t2
        
                
                estimation.append(f(x1, t1)*hmax)
                t_euler_list.append(t2)
                
        #sums the values in the list to only return the value of x at t2
        estimation = sum(estimation)
        
        print (estimation)
        
        return estimation
        
    


    pass


def odesolve(f, X0, t, hmax, method=euler):
    """Compute the solution at different values of t"""
   
    #setting up a list with the starting x value
    true_x_values = [X0[0]]
    
    
    for i in range(1, len(t)):
        
        #passing the values of tvals into the list with a for loop to then append them to the list
        x_values = (solveto(f, X0[0], t[0], t[i], hmax, method))
        true_x_values.append(x_values)
        
    
    return true_x_values
    
    x = t
    # corresponding y axis values
    y = true_x_values
  
    # plotting the points
    plt.plot(x, y)
  
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
  
    # giving a title to my graph
    plt.title("odesolve")
  
    plt.show()
    pass
