from epbot import epic
from os import sys,mkdir,path

if __name__ == "__main__":
    if not path.exists("cache"):
        mkdir("cache")
    epic().run()
