def miles_to_kilometer(miles,):
#      miles_value= float(miles)/1.60934
#      print(miles_value)
#      miles_to_kilometer("1")

 def miles_to_kilometer(miles,):

   
   return float (miles)/100
 miles=(input("enter miles value to convert"))
 miles_value=miles_to_kilometer(miles)
 print(miles_value)
 return float(miles)/100
# # miles_to_kilometer(miles,):
# #print (miles_value)
# data=inpt(input("enter miles value to convert"))
# miles_value=miles_to_kilometer(miles)
# print(data*3.0)

# def calc_sum(a,b):
#  sum = a + b
#  print(sum)
#  return sum
 

# calc_sum(5,10)

# calc_sum(2,10)

# calc_sum(12,17)

# def calc_sum(k,n):
#   sum = k + n
#   print(sum)
#   return sum

# calc_sum(500,100)

# calc_sum(2,3)
# calc_sum(7,3)


# def calc_sum(w,n):
#   sum= w + n
#   print(sum)
#   return sum


# calc_sum(10,17)

# calc_sum(8,2)

# def calc_sum(f,n):
#   sum = f+n
#   print(sum)
#   return sum

# calc_sum(2,7)

# calc_sum(4,7)


# def calc_sum(t,r):
#   sum = t + r
#   print(sum)
#   return sum

# calc_sum(4,9)

# calc_sum(8,11)


# def clac_sum(a,m):
#   sum = a+m
#   print(sum)
#   return sum

# clac_sum(3,7)
# calc_sum(6,9) 
  
# def clac_sum(s,h):
#   sum= s+h
#   print(sum)
#   return sum

# calc_sum(44,6)

# calc_sum(66,44)

# def miles_to_kilometer(miles):
#    return float(miles)/1.6093420


# miles = input("enter miles value to conver")
# miles_value=miles_to_kilometer(miles)
# print(miles_value)

def temp_func() :
  y = 20
  print('inside funtion:',y) 
  temp_func()
# print(y)#tihi w20
  
def my_funt():
  global x
  x = 30
  # x = 30
  print(x)
my_funt()

def my_funt():
  global y
  y = 70
 # y = 70
  print(y)
my_funt() 


def my_funt():
  global r
  r = 50
 # r = 50
  print(r)
my_funt() 

def temp_func():
  global x
  x = 30
  s = 20
  print('msk function:',x)

temp_func()
print('rsk function:',r) 





