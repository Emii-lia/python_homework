from binom import poissonDist

def probabitity(beg:int, end:int, mean:float)->float:
   
   if beg <= end:
      if beg ==0:
         return poissonDist(end, mean, cumul=True)
      elif beg == end:
         return poissonDist(end, mean, cumul=False)
      else:
         return poissonDist(end, mean, cumul=True) - poissonDist(beg, mean, cumul=True)

def main():
   print("================================================")
   print("         Probabilite annuelle des Cyclone       ")
   print("================================================")
   
   try:
      mean = int(input("Entrez le nombre moyenne de cyclone passant par an: "))
   except:
      print("Entrez un nombre")
      exit()
   
   interval = input("Entrez l'interval de nombre de cyclone à estimer en une année(séparez par un tiret): ")
   try:
      beg,end = interval.split("-")
      beg = int(beg)
      end = int(end)
      
   except:
      print("Entrez une interval de nombre")
   
   print(f"La probabilité est {probabitity(beg=beg, end=end, mean=mean)}")

if __name__ == "__main__":
   main()
   