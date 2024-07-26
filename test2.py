import sys
import concurrent.futures



nb = int(sys.argv[1]) 

def draw_colonne(x):
    for a in range(0, nb-2):                        #vertical
            print("#", end=" ")
            print("")

def abc(x):
    for maria in range(0, nb):
        print("  ", end="")
    print("#")
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(draw_colonne(nb))
    for a in range(0, nb):
        executor.submit(abc(nb))
    