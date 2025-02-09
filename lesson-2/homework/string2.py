""" Extract car names from this text: 
txt = 'LMaasleitbtui'   """

txt = 'LMaasleitbtui' 
a = len(txt)
b = int(a%2)
fn = ""
sn = ""
for i in range(a):
    if (i%2==0):
        fn += txt[i]
      
for i in range(a):
    if (i%2>0):
        sn += txt[i]

print("Congragualtions, you successfully managed to solve problem. \n You extracted both car names from \'LMaasleitbtui\':")
print(f"The name of the first car is {fn}")
print(f"The name of the second car is {sn}")
  
#sm = snm
#print(fm, sm)
    


