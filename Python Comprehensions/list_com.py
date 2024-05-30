

def odd_fun(l):
    odd=[i for i in l if i%2!=0]
    return odd

def even_fun(l):
    even=[i for i in l if i%2==0]

    return even

def mult_list(l):
    m=[i*i for i in l]
    return m

l=[1,2,3,4,5,6,7,8,9,10]

print(odd_fun(l))

print(even_fun(l))

print(mult_list(l))