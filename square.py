import sys

nb=int(sys.argv[1]) 


def draw_line(x):
        for a in range(0, nb):

            print("#", end=" ")
      

def draw_colonne(x):
    print(" ")
    for a in range(0, nb-2):                        #vertical
            
            print("#", end=" ")
            for dolor in range (0,nb-2):      
                print(" ",end=" ")
            print("#") 





def draw_final_line(x):
     for a in range(0, nb):
            print("#", end=" ")








if nb <= 0:
    print("error")
else :
    draw_line(nb)
    draw_colonne(nb)
    draw_final_line(nb)


print("")














