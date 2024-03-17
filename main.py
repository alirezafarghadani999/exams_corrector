import sys , os
from libs.log import Log


path = {
    "pkgs":"requerment.txt" ,
}

Dpkg = {
    "opencv-python":"cv2"
}

log = Log()

def get_pkg() -> list:
    pkgs= []
    with open(path["pkgs"],"r") as f :
        pkgs = f.read().split("\n")
        f.close()
    return pkgs

def main(arg) -> None:
    # setup debug mod
    if "--debug" in arg:
        log = Log(True)

    # check pkg / call gui
    pkgs = get_pkg()
    for pkg in pkgs:
        try:
            exec(f"import {Dpkg[pkg]}")
        except:
            log.w(f"{pkg} pkg not installed")
    

    return

if __name__ == "__main__":
    arg = sys.argv
    main(arg)

