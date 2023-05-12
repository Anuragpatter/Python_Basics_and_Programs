# Program to find the cube root of a number if its a perfect cube 
def perfectCube(N) :    # define function where N is the argument in the function
 
    cube = 0
    # for loop 
    for i in range(N + 1) :
 
        cube = i * i * i
        if (cube == N) :
            print("The number is perfect cube")
            cr= N**(1/3)
            print("Cube root of the number is: ",cr)
            return
     
        elif (cube > N) :
            print("The number is not a perfect cube")
            return

if __name__ == "__main__" :
    N=int(input("Enter the value of Number: "))    # Input the number whose cube root to find  
    perfectCube(N)     # Function Call