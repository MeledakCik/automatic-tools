import os


from bs4 import BeautifulSoup
from rich import print as prints
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree



def lgoin():
    tree = Tree(Panel.fit(f"[bold green]Login instagram menggunakan username dan password",style='blue'))
    prints(tree)
    username = input("+ Masukkan username: ")
    password = input("+ Masukkan password: ")
    
    link = ''
    
    
if __name__ == "__main__":
    os.system('clear')
    lgoin()