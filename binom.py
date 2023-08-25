from math import exp
def factorial(n:int)->int:
   return int(n*factorial(n-1)) if n>1 else 1

def combination(n:int,p:float)->int:
   return int(factorial(n)/(factorial(n-p)*factorial(p))) if n>=p else None

def binomDist(x:int,n:int,p:float,cumul=False)->float:
   if p<=1 and p>=0:
      return (combination(n,x)*(p**x)*((1-p)**(n-x)) if cumul==False or x==0 else combination(n,x)*(p**x)*((1-p)**(n-x))+binomDist(x-1,n,p,True))

def poissonDist(x:int, mean:float,cumul=False)->float:
   return (1/exp(mean))*((mean**x)/factorial(x)) if cumul==False or x==0 else (1/exp(mean))*((mean**x)/factorial(x)) + poissonDist(x-1, mean, True)