from numpy import *

class algorithm(object): #Our Algorithm class to do algorithm
    def __init__(self,n): #Class initialize
        self.n = n
        self.d = []
        self.m = zeros((self.n+1,self.n+1))
        self.min_ans = []
        self.list_k = []
        self.p = zeros((self.n+1,self.n+1))
        self.answer = zeros((self.n,self.n))
        self.p_matrix = zeros((self.n,self.n))
        self.order_list = []
        #self.i = i
        #self.j = j
        self.order_str = ""
        
    def row_column(self): #This get row and column of matrix from user and add them to list d.
        print()
        print("Enter row and column of {} first matrix: \n".format(self.n-1))
        for i in range(self.n-1):
            r = int(input("Enter row: "))
            c = int(input("Enter Column: "))
            if r not in self.d:
                self.d.append(r)

            if c not in self.d:
                self.d.append(c)
            print()

        c = int(input("Enter last matrix columns: "))
        self.d.append(c)
        print()
        
    def optimize(self): #This do algorithm.
        algorithm.row_column(self)
        for i in range(1,self.n+1): #Main Diaogonal is zero.
            self.m[i,i] = 0

        for di in range(1,self.n):
            for i in range(1,(self.n-di)+1):
                j = i + di
                for k in range(i,j):
                    self.min_ans.append(self.m[i,k] + self.m[k+1,j] + self.d[i-1]*self.d[k]*self.d[j]) #Add all answers from k=0 to k=n.
                    self.list_k.append(k)    #Add all k's in list
                    
                a = min(self.min_ans)        #Which answer is minimum??
                b = self.min_ans.index(a)    #Find index of that minimum answer.
                self.p[i,j] = self.list_k[b] #In list_k find that minimum answer k and add minimum k to matrix p.
                self.m[i,j] = a              #add minimum answer in matrix m.
                
                self.min_ans.clear() #Clear our lists to add new items.
                self.list_k.clear()

    def print_m(self): #Print Matrix m(minimum answers).
        algorithm.optimize(self)
        for i in range(self.n):
            for j in range(self.n):
                self.answer[i,j] = self.m[i+1,j+1]

        print("M is: \n",self.answer)
        print()

    def print_p(self): #Print Matrix p(minimum answers k).
        for i in range(self.n):
            for j in range(self.n):
                self.p_matrix[i,j] = self.p[i+1,j+1]
                
        print("P is: \n",self.p_matrix)

    """def print_order(self): #Print order of matrix mulitply.
        i = self.i
        j = self.j
        def order(i,j):
            if(i == j):
                self.order_list.append("A{}".format(i)) #Add A's to list
            else:
                k = int(self.p_matrix[i-1,j-1])
                self.order_list.append("(") #Add "(" and ")" To lis
                order(i,k) #Recursion Function to print order.
                order(k+1,j)
                self.order_list.append(")")
        order(i,j)
        print()
        print("A{} to A{} Best Multiply is: ".format(i,j),self.order_str.join(self.order_list))"""
