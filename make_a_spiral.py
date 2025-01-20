import numpy
def spiralize(size):
    
    #we make a square matrix with the size given with all elements 0
    M= [[0 for i in range(size)]for j in range(size)]

    #this part wraps a square matrix in 1, except [0][1] element kept zero
    def wrapping(mat_size):
        Mat= [[0 for l in range(mat_size)]for j in range(mat_size)]
        for i in range(mat_size):
            Mat[0][i]=Mat[i][0]=Mat[i][mat_size-1]=Mat[mat_size-1][i]='_'
        Mat[1][0]=0
        return Mat

    #here we build the spiral layer by layer
    for i in range(0,int(size/2),2):
        M[i][i-1]='_'
        for j in range(i,size-i):
            for k in range(i,size-i):
                M[j][k]= wrapping(size-2*i)[j-i][k-i]    
    if size%4==1:
        M[int(size/2)][int(size/2)]=M[int(size/2)][int(size/2)-1]='_'
    return M

print(numpy.array(spiralize(10)))
                

