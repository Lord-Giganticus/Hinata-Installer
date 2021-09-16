import os
from os import path

def main() :
    home_dir = path.dirname(__file__)

    if os.getcwd() is not home_dir:
        os.chdir(home_dir)

    os.chdir("src")

    with open("main.h", "r") as f:
        lines = f.readlines()
        f.close()

    if lines[21][43:47] == "Men.":
        print("Already setup for Men on main.h")
    else: 
        lines[21] = lines[21].replace("2","")
        lines[23] = lines[23].replace("2","")
        lines[24] = lines[24].replace("2","")

        with open("main.h","w") as f:
            f.writelines(lines)
            f.close()
            print("Setup Men for main.h")

    with open("main.c","r") as f:
        lines = f.readlines()
        f.close()
        
    if lines[299][37:41] == "Men.":
        print("Already setput for Men on main.c")
    else:
        lines[299] = lines[299].replace("2","")
        lines[317] = lines[317].replace("2","")

        with open("main.c","w") as f:
            f.writelines(lines)
            f.close()
            print("Setup Men for main.c")
    
if __name__ == "__main__":
    exit(main())