#begin
#    set sum to 0
#    define n as [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    create an empty list called list

#    for each element i in n 
#        add i to sum
#        append sum to list
#    end for

#    print list
#end


n=[1,2,3,4,5,6,7,8,9,10]
sum=0  
list=[]
for i in n:
    sum+=i  
    list.append(sum) 
print(list) 