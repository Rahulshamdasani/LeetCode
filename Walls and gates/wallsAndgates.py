class solution:

    def getAllGates(self,mat):
        g = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(mat[i][j] == 0):
                    g.append((i,j))
        return g

    def recurse(self,mat,x,y):
        # go left
        row =  x
        col = y-1
        while(col>=0):
            if(mat[row][col] < mat[row][col+1]+1):
                break
            else:
                mat[row][col] = mat[row][col+1]+1
                self.recurse(mat,row,col)
            col-=1

        # go Right
        row =  x
        col = y+1
        while(col<len(mat[0])):
            if(mat[row][col] < mat[row][col-1]+1):
                break
            else:
                mat[row][col] = mat[row][col-1]+1
                self.recurse(mat,row,col)
            col+=1
        
        #go up
        row =  x-1
        col = y
        while(row>=0):
            if(mat[row][col] < mat[row+1][col]+1):
                break
            else:
                mat[row][col] = mat[row+1][col]+1
                self.recurse(mat,row,col)
            row -= 1
        #print("Going down from ",roomi,roomj)
        #go down
        row =  x+1
        col = y
        while(row<len(mat)):
            if(mat[row][col] < mat[row-1][col]+1):
                #print("Broke for",roomi,j)
                break
            else:
                #print(roomi,j)
                mat[row][col] = mat[row-1][col]+1
                #print("****",mat[roomi][j-1]+1,mat[roomi][j])
                self.recurse(mat,row,col)
            row += 1

    def wallsAndGates(self,mat):
        # this will be a set of tuples of coordinates of all gates
        g = self.getAllGates(mat)
        print(g)
        for row in mat:
            print (row) 
        print("Iter")

        for x in g:
            print("Iterating for",x)
               
            print("*"*6)
            self.recurse(mat,x[0],x[1])    
            for row in mat:
                print (row) 

mat = [ [1000, -1, 0, 1000],
        [1000, 1000, 1000, -1],
        [1000, -1, 1000, -1],
        [0, -1, 1000, 1000]
    ]

solution().wallsAndGates(mat)