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

    if lines[21][43:47] == "Men2":
        exit(print("Already setup for Men2."))
    else:
        lines[21] = lines[21].replace("Men","Men2")
        lines[23] = lines[23].replace("Men","Men2")
        lines[24] = lines[24].replace("Men","Men2")

        with open("main.h","w") as f:
            f.writelines(lines)
            f.close()

    with open("main.c","r") as f:
        lines = f.readlines()
        f.close()
        
    if lines[299][37:41] == "Men2":
        print("Already setput for Men2 on main.c")
    else:
        lines[299] = lines[299].replace("Men","Men2")
        lines[317] = lines[317].replace("Men","Men2")

        with open("main.c","w") as f:
            f.writelines(lines)
            f.close()

if __name__ == "__main__":
    exit(main())