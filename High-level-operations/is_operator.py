




def main():



    lst1=[1,2]
    lst2=[1,2]


    #check whether the elements in the list are same
    print(lst1==lst2)

    lst1_copy=lst1


    print(lst1==lst1_copy)


    #check shares the same memory location
    print(lst1 is lst1_copy)  # return true

    print(lst1 is lst2)  #return false


    # lst1_copy is the pointer for the lst1  so shares the same memory 

    #if do any modification in lst1_copy then it will reflect on the lst1 also

    






if __name__=="__main__":

    main()