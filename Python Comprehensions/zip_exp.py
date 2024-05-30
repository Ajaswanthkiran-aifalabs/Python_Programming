



def main():

    lst1=[1,2,3,4,5,6]
    lst2=["A","B","C","D","F"]
    lst3=["A","B","C","D","F"]


    for i,j,k in zip(lst2,lst1,lst3):
        print(i,j,k)
if __name__=="__main__":


    main()