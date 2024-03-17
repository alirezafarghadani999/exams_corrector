from libs.color import color
import datetime

now = datetime.datetime.now()
class Log:
    
    def __init__(self,active = False) -> None:
        self.active = active
        if active:
            print(f"{color.reset}{color.fg.yellow}{color.bg.black}{color.bold}DEBUG MOD ACTIVATED{color.reset}")

    def e(self,msg): # error log
        if self.active :
            print(f"{now.time()} | {color.fg.red}{color.bold}ERROR :{color.reset}{color.fg.red} {msg}{color.reset}")

    def w(self,msg):
        if self.active :
            print(f"{now.time()} | {color.fg.yellow}{color.bold}WARNING :{color.reset}{color.fg.yellow} {msg}{color.reset}")

    def p(self,msg):
        if self.active :
            print(f"{now.time()} |  {color.fg.blue}{color.bold}Print :{color.reset}{color.fg.blue} {msg}{color.reset}")


