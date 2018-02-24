import os
import fire
from core import repl
from core import filereader
read = filereader.read
if __name__ == '__main__':
    repl.activate()