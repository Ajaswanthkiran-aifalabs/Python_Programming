
from typing import List


import re
class CustomException(Exception):
    pass




class ArrayManagement():
    
    def __init__(self):
        self.glo=[]
        self.string_arr=  []
        self.integer_arr=[]
        self.boolean_arr=[]

    def insert_integer(self,inp):
        try: 
            if not isinstance(inp,int):
                raise CustomException("The provided value is not integer")
            
            if self.search_in(inp,self.integer_arr):
                self.integer_arr.append(inp)
                self.glo.append(inp)
                print("The integer element is inserted: ",inp)
        except Exception as e:
            print(e)
        

    def insert_string(self,s):
        if self.search_in(s,self.string_arr):
            self.string_arr.append(s)
            self.glo.append(s)
            print("The string element is inserted: ",s)

    def insert_boolean(self,inp):
        try:
            if isinstance(inp,bool):
                if self.search_in(inp,self.boolean_arr):
                    self.boolean_arr.append(inp)
                    self.glo.append(inp)
                    print("The Boolean element is inserted: ",inp)
            else:
                raise CustomException("The provided value is not Boolean")
        except Exception as e:
            print(e)

    
    
    def search_in(self,inp,arr):
        if inp in arr:
            print("Element already present")
            return False
        return True



    def print_int_in_global(self): 
        for i in self.glo:
            if isinstance(i,int):
                print(i, " ")
        
    def print_str_in_global(self): 
        for i in self.glo:
            if isinstance(i,str):
                print(i, " ")

    def print_bool_in_global(self): 

        for i in self.glo:
            if isinstance(i,bool):
                print(i+" ")

    def delete_bool(self,inp):
        try:
            self.boolean_arr.remove(inp)
            self.glo.remove(inp)
            print("The element is deleted: ", inp)
        except:
            print("Element is not present in boolean array or global array")

    def delete_int(self,inp):
        try:
            self.integer_arr.remove(inp)
            self.glo.remove(inp)
            print("The element is deleted: ",inp)
        except:
            print("Element is not present in integer array or global array")
    
    def delete_str(self,inp):
        try:
            self.string_arr.remove(inp)
            self.glo.remove(inp)
            print("The element is deleted: ",inp)
        except:
            print("Element is not present in string array or global array")
    
    def remove_str(self):
        self.glo=[i for i in self.glo if i not in self.string_arr] 
    
    def remove_bool(self):
        self.glo=[i for i in self.glo if i not in self.boolean_arr] 
    
    def remove_int(self):
        self.glo=[i for i in self.glo if i not in self.integer_arr] 


    def str_num_matching(self):
        nums=[i  for i in self.string_arr if i.isnumeric() and int(i) in self.integer_arr ]

        print(nums)
    
    def print_all_arrays(self):
        print()
        print("Integer array: ",self.integer_arr)
        
        print("String array: ",self.string_arr)
        
        print("Boolean array: ",self.boolean_arr)
        
        print("Global array: ",self.glo)

        print()

       


if __name__=="__main__":

    array_instance=ArrayManagement()
    array_instance.insert_boolean(True)
    array_instance.insert_boolean(False)
    array_instance.insert_integer(12)
    array_instance.insert_boolean(False)
    array_instance.insert_integer(13)
    array_instance.insert_integer(16)
    array_instance.insert_integer(13)
    array_instance.insert_string("121")
    array_instance.insert_string("dssfsdf")
    array_instance.insert_string("324dsaf")
    array_instance.insert_string("232")
    array_instance.insert_string("13")
    array_instance.insert_string("16")
    array_instance.print_all_arrays()
    array_instance.delete_bool(True)
    array_instance.delete_int(54)
    array_instance.delete_str("232")


    print("String Matching with numbers: ")
    array_instance.str_num_matching()

    array_instance.print_all_arrays()

    array_instance.remove_bool()
    print("\nThe global array after deleting boolean array")
    array_instance.print_all_arrays()

    array_instance.remove_int()
    print("\nThe global array after deleting integer array")
    array_instance.print_all_arrays()

    array_instance.remove_str()
    print("\nThe global array after deleting string array")
    array_instance.print_all_arrays()



