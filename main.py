import os
from colorama import Fore, Back, Style
from prozac import Prozac

def run():
    startup()
    prints()
    Prozac().listen()

def startup():
    os.system("color")
    os.system(f"title Prozac")

def prints():
    ascii_art = """
                                                                                                                                                                                                                                
    """
    ascii_art = ascii_art.replace("@", f"{Fore.GREEN}@{Style.RESET_ALL}").replace(".", f"{Fore.WHITE}.{Style.RESET_ALL}")

    
    print(ascii_art)

    
run()
