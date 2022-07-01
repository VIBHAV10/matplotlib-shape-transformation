import numpy as np
import streamlit as st  
import matplotlib.pyplot as plt


class Shape:
   
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        figure, axes = plt.subplots()
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()
        # st.pyplot(figure)




        



class Polygon(Shape):
    
    def __init__(self, A):
        '''
        Initializations here
        '''
        super().__init__()
        self.coordinates = A #stores coordinates of polygon
        self.coordinates_old = A #stores coordinates of polygon before transformation for plotting
 
    
    def translate(self, dx, dy):
        
        self.coordinates_old = self.coordinates.copy()
        #self.coordinates_old = np.around(self.coordinates_old, 2) 

        #To change value of translate matrix attribute(T_t) in shape class
        #This attribute is used for translation
        super().translate(dx, dy)
        translate_matrix = self.T_t
        self.coordinates = self.coordinates @ translate_matrix.transpose()

        temp = self.coordinates.copy()
        temp = temp.transpose()

        #forming list of x and y coordinates of polygon
        x = np.around(temp[0], 2)
        y = np.around(temp[1], 2)
        return (x, y)
    
    def scale(self, sx, sy):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        temp_coor = self.coordinates.transpose()
        center_x = sum(temp_coor[0])/len(temp_coor[0])  #x coordinate of center of polygon
        center_y = sum(temp_coor[1])/len(temp_coor[1])  #y coordinate of center of polygon
        
        self.coordinates_old = self.coordinates.copy()
        #self.coordinates_old = np.around(self.coordinates_old, 2)

        #performing translation on polygon to bring it to origin
        super().translate(-center_x, -center_y)
        translate_matrix1 = self.T_t
        self.coordinates = self.coordinates @ translate_matrix1.transpose()

        #To change value of scale matrix attribute(T_s) in shape class
        #This attribute is used for scaling 
        super().scale(sx, sy)
        scaling_matrix = self.T_s
        self.coordinates = self.coordinates @ scaling_matrix

        #performing translation on polygon to take its center back to original position
        super().translate(center_x, center_y)
        translate_matrix2 = self.T_t
        self.coordinates = self.coordinates @ translate_matrix2.transpose()

        temp = self.coordinates.copy()
        temp = temp.transpose()

        x = np.around(temp[0], 2)
        y = np.around(temp[1], 2)
        return (x, y)


 
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''

        self.coordinates_old = self.coordinates.copy()
        #self.coordinates_old = np.around(self.coordinates_old, 2)

        #performing translation on polygon to bring it to origin
        super().translate(-rx, -ry)
        translate_matrix1 = self.T_t
        self.coordinates = self.coordinates @ translate_matrix1.transpose()

        #To change value of rotate matrix attribute(T_r) in shape class
        #This attribute is used for rotating
        super().rotate(-deg)
        rotating_matrix = self.T_r
        self.coordinates = self.coordinates @ rotating_matrix

        #performing translation on polygon to take its center back to original position
        super().translate(rx, ry)
        translate_matrix2 = self.T_t
        self.coordinates = self.coordinates @ translate_matrix2.transpose()

        temp = self.coordinates.copy()
        temp = temp.transpose()

        x = np.around(temp[0], 2)
        y = np.around(temp[1], 2)
        return (x, y)  

    def plot(self):
        '''
        Function to plot the polygon
    
        '''
        a = self.coordinates.transpose() #coordinates of polygon after transformation
        b = self.coordinates_old.transpose() #coordinates of polygon before transformation
        
        x1 = np.append(a[0], a[0][0])  
        y1 = np.append(a[1], a[1][0])
        x2 = np.append(b[0], b[0][0])
        y2 = np.append(b[1], b[1][0])

        plt.plot(x1, y1) #plot of tranformed ploygon
        plt.plot(x2, y2, '--') #plot of before tranformation polygon

        x_dim = max(abs(np.min(a[0])), abs(np.min(b[0])), np.max(a[0]), np.max(b[0])) #calculation of maximmum coordinate values for grid
        y_dim = max(abs(np.min(a[1])), abs(np.min(b[1])), np.max(a[1]), np.max(b[1]))

        #calling plot from shape to make grid and show plots
        super().plot(x_dim, y_dim)



class Circle(Shape):
    
    def __init__(self, x=0, y=0, radius=5):
        
        super().__init__()
        self.center_x = x 
        self.center_y = y
        self.coordinates_center = np.array([self.center_x, self.center_y, 1]) #matrix to perform translation and rotation operation
        self.rad = radius
        self.old_centerx = x #values of center coordinates and radius before transformation stored for plotting
        self.old_centery = y
        self.old_radius = radius
    
    def translate(self, dx, dy):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''

        self.old_centerx = self.center_x
        self.old_centery = self.center_y
        self.old_radius = self.rad

        #changing value of tranlation matrix attribute(T_t) of class shape
        #this matrix is used for translating the circle
        super().translate(dx, dy)
        translate_matrix = self.T_t
        self.coordinates_center = self.coordinates_center @ translate_matrix.transpose()

        self.center_x = self.coordinates_center[0] #changed coordinates of center of circle
        self.center_y = self.coordinates_center[1]

        return_array = np.array([self.center_x, self.center_y, self.rad]) #return tupple
        return_array = np.around(return_array, 2)
        return (return_array[0], return_array[1], return_array[2])


    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        self.old_radius = self.rad
        self.old_centerx = self.center_x
        self.old_centery = self.center_y

        #changing value of scaling matrix attribute(T_s) of class shape
        #this matrix is used for scaling of radius
        super().scale(sx,sx)
        scale_matrix = self.T_s
        self.rad = (np.array([self.rad, 0, 0]) @ scale_matrix)[0] #scales only the radius

        return_array = np.array([self.center_x, self.center_y, self.rad]) #return tuple
        return_array = np.around(return_array, 2)
        return (return_array[0], return_array[1], return_array[2])
    
    def rotate(self, deg, rx = 0, ry = 0):
        
        #Function to rotate the circle
    
        self.old_centerx = self.center_x
        self.old_centery = self.center_y
        self.old_radius = self.rad

        #performing translation on center to bring point about which to rotate to origin
        super().translate(-rx, -ry)
        translate_matrix1 = self.T_t
        self.coordinates_center = self.coordinates_center @ translate_matrix1.transpose()
        self.center_x = self.coordinates_center[0]
        self.center_y = self.coordinates_center[1]

        #changing value of rotate matrix attribute(T_r) of class shape
    
        #-deg is passed as positive thetha does anticlockwise rotation
        super().rotate(-deg)
        rotate_matrix = self.T_r
        self.coordinates_center = self.coordinates_center @ rotate_matrix

        #performing translation on center to take it to its original position
        super().translate(rx, ry)
        translate_matrix2 = self.T_t
        self.coordinates_center = self.coordinates_center @ translate_matrix2.transpose()
        self.center_x = self.coordinates_center[0]
        self.center_y = self.coordinates_center[1]

        return_array = np.array([self.center_x, self.center_y, self.rad]) #return tuple
        return_array = np.around(return_array, 2)
        return (return_array[0], return_array[1], return_array[2])   

    
    def plot(self):
        
        #Function to plot the circle
    
       
        circle_old = plt.Circle((self.old_centerx, self.old_centery), self.old_radius, color='r', fill = False, linestyle = '--')
        circle_new = plt.Circle((self.center_x, self.center_y), self.rad, color='g', fill = False)

        fig, ax = plt.subplots()

        ax.add_patch(circle_old)
        ax.add_patch(circle_new)
        
        max_xy = max(abs(self.old_centerx), abs(self.center_x), abs(self.center_y), abs(self.old_centery))
        max_rad = max(self.old_radius, self.rad)

        x_dim, y_dim = max_xy + max_rad, max_rad + max_xy
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()
        st.pyplot(fig)
        super().plot(x_dim, y_dim)

if __name__ == "__main__":
    
    #menu starts here

    verbose = int(input('Verbose? 1 to plot, 0 otherwise: '))
        
    if verbose == 1:

        tests = int(input('Enter number of test cases: '))
        print()
        
        for i in range(tests):
            
            shape = int(input('Enter type of shape(polygon:0/ circle:1): '))
            print()

            if shape == 0:
                n = int(input('Enter number of sides: '))
                A = np.array([])
                for j in range(n):
                    x, y = map(float, input('Enter (x{},y{}): '.format(j+1, j+1)).split())
                    print()
                    array = np.array([x, y, 1])
                    A = np.append(A, array)
                A = A.reshape(n, 3)
                poly = Polygon(A)

                query_no = int(input('Enter number of queries: '))
                print()
                for k in range(query_no):
                    print('Enter one of following queries: ')
                    print('1) R deg (rx) (ry): To rotate the ploygon')
                    print('2) T dx (dy): To translate the polygon')
                    print('3) S sx (sy): To scale the polygon ')
                    print('4) P: To plot the previous and current state of polygon')

                    query = input('Enter a query: ').split()
                    print()
                    length = len(query)

                    if query[0].lower() == 'r':
                        if length == 2:
                            output = poly.rotate(float(query[1]))
                        elif length == 3:
                            output = poly.rotate(float(query[1]), float(query[2]), float(query[2]))
                        else:
                            output = poly.rotate(float(query[1]), float(query[2]), float(query[3]))

                        old_coor = poly.coordinates_old
                        old_coor = np.around(old_coor, 2)
                        old_coor = old_coor.transpose()

                        print(*old_coor[0], *old_coor[1])
                        print(*output[0], *output[1])
                        print()

                        poly.plot()
                    
                    elif query[0].lower() == 't':
                        if length == 2:
                            output = poly.translate(float(query[1]), float(query[1]))
                        else:
                            output = poly.translate(float(query[1]), float(query[2]))

                        old_coor = poly.coordinates_old
                        old_coor = np.around(old_coor, 2)
                        old_coor = old_coor.transpose()

                        print(*old_coor[0], *old_coor[1])
                        print(*output[0], *output[1])   
                        print() 

                        poly.plot()

                    elif query[0].lower() == 's':
                        if length == 2:
                            output = poly.scale(float(query[1]), float(query[1]))
                        else:
                            output = poly.scale(float(query[1]), float(query[2]))

                        old_coor = poly.coordinates_old
                        old_coor = np.around(old_coor, 2)
                        old_coor = old_coor.transpose()

                        print(*old_coor[0], *old_coor[1])
                        print(*output[0], *output[1])
                        print()

                        poly.plot()
                    
                    elif query[0].lower() == 'p':
                        poly.plot()
    
            else:
                att = input('Enter coordinates of center and radius of circle(x y r): ').split()
                if att == []:
                    cir = Circle()
                elif len(att) == 1:
                    cir = Circle(x = float(att[0]))
                elif len(att) == 2:
                    x, y = map(float, att)
                    cir = Circle(x = x, y = y)
                else:
                    x, y, r = map(float, att)
                    cir = Circle(x = x, y = y, radius = r)

                query_no = int(input('Enter number of queries: '))
                print()

                for k in range(query_no):
                    print('Enter one of following queries: ')
                    print('1) R deg (rx) (ry): To rotate the circle')
                    print('2) T dx (dy): To translate the circle')
                    print('3) S sx (sy): To scale the circle ')
                    print('4) P: To plot the previous and current state of circle')

                    query = input('Enter a query: ').split()
                    print()
                    length = len(query)               

                    if query[0].lower() == 'r':
                        if length == 2:
                            output = cir.rotate(float(query[1]))
                        elif length == 3:
                            output = cir.rotate(float(query[1]), float(query[2]), float(query[2]))
                        else:
                            output = cir.rotate(float(query[1]), float(query[2]), float(query[3]))

                        print(cir.old_centerx, cir.old_centery, cir.old_radius)
                        print(*output)
                        print()

                        cir.plot()
                    
                    elif query[0].lower() == 't':
                        if length == 2:
                            output = cir.translate(float(query[1]), float(query[1]))
                        else:
                            output = cir.translate(float(query[1]), float(query[2]))

                        print(cir.old_centerx, cir.old_centery, cir.old_radius)
                        print(*output)    
                        print() 

                        cir.plot()

                    elif query[0].lower() == 's':
                        output = cir.scale(float(query[1]))

                        print(cir.old_centerx, cir.old_centery, cir.old_radius)
                        print(*output)
                        print()

                        cir.plot()

                    elif query[0].lower() == 'p':
                        cir.plot()
                

    else:

        tests = int(input('Enter number of test cases: '))
        print()
        
        for i in range(tests):
            
            shape = int(input('Enter type of shape(polygon:0/ circle:1): '))
            print()

            if shape == 0:
                n = int(input('Enter number of sides: '))
                A = np.array([])
                for j in range(n):
                    x, y = map(float, input('Enter (x{},y{}): '.format(j+1, j+1)).split())
                    print()
                    array = np.array([x, y, 1])
                    A = np.append(A, array)
                A = A.reshape(n, 3)
                poly = Polygon(A)

                query_no = int(input('Enter number of queries: '))
                print()
                for k in range(query_no):
                    print('Enter one of following queries: ')
                    print('1) R deg (rx) (ry): To rotate the ploygon')
                    print('2) T dx (dy): To translate the polygon')
                    print('3) S sx (sy): To scale the polygon ')
                    print('4) P: To plot the previous and current state of polygon')

                    query = input('Enter a query: ').split()
                    print()
                    length = len(query)

                    if query[0].lower() == 'r':
                        if length == 2:
                            output = poly.rotate(float(query[1]))
                        elif length == 3:
                            output = poly.rotate(float(query[1]), float(query[2]), float(query[2]))
                        else:
                            output = poly.rotate(float(query[1]), float(query[2]), float(query[3]))

                        old_coor = poly.coordinates_old
                        old_coor = np.around(old_coor, 2)
                        old_coor = old_coor.transpose()

                        print(*old_coor[0], *old_coor[1])
                        print(*output[0], *output[1])
                        print()
                    
                    elif query[0].lower() == 't':
                        if length == 2:
                            output = poly.translate(float(query[1]), float(query[1]))
                        else:
                            output = poly.translate(float(query[1]), float(query[2]))

                        old_coor = poly.coordinates_old
                        old_coor = np.around(old_coor, 2)
                        old_coor = old_coor.transpose()

                        print(*old_coor[0], *old_coor[1])
                        print(*output[0], *output[1])   
                        print()                    

                    elif query[0].lower() == 's':
                        if length == 2:
                            output = poly.scale(float(query[1]), float(query[1]))
                        else:
                            output = poly.scale(float(query[1]), float(query[2]))

                        old_coor = poly.coordinates_old
                        old_coor = np.around(old_coor, 2)
                        old_coor = old_coor.transpose()

                        print(*old_coor[0], *old_coor[1])
                        print(*output[0], *output[1])
                        print()
                    
                    elif query[0].lower() == 'p':

                        poly.plot()  
                
            else:
                att = input('Enter coordinates of center and radius of circle(x y r): ').split()
                if att == []:
                    cir = Circle()
                elif len(att) == 1:
                    cir = Circle(x = float(att[0]))
                elif len(att) == 2:
                    x, y = map(float, att)
                    cir = Circle(x = x, y = y)
                else:
                    x, y, r = map(float, att)
                    cir = Circle(x = x, y = y, radius = r)

                query_no = int(input('Enter number of queries: '))
                print()

                for k in range(query_no):
                    print('Enter one of following queries: ')
                    print('1) R deg (rx) (ry): To rotate the circle')
                    print('2) T dx (dy): To translate the circle')
                    print('3) S sx (sy): To scale the circle ')
                    print('4) P: To plot the previous and current state of circle')

                    query = input('Enter a query: ').split()
                    print()
                    length = len(query)               

                    if query[0].lower() == 'r':
                        if length == 2:
                            output = cir.rotate(float(query[1]))
                        elif length == 3:
                            output = cir.rotate(float(query[1]), float(query[2]), float(query[2]))
                        else:
                            output = cir.rotate(float(query[1]), float(query[2]), float(query[3]))
                        
                        print(cir.old_centerx, cir.old_centery, cir.old_radius)
                        print(*output)
                        print()
                        
                    
                    elif query[0].lower() == 't':
                        if length == 2:
                            output = cir.translate(float(query[1]), float(query[1]))
                        else:
                            output = cir.translate(float(query[1]), float(query[2]))

                        print(cir.old_centerx, cir.old_centery, cir.old_radius)
                        print(*output)    
                        print()                  

                    elif query[0].lower() == 's':
                        output = cir.scale(float(query[1]))

                        print(cir.old_centerx, cir.old_centery, cir.old_radius)
                        print(*output)
                        print()

                    elif query[0].lower() == 'p':
                        cir.plot()                              
        