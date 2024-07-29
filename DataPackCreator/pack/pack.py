import sys
from pathlib import Path
import os
import shutil
from presets import *


Load.load(["say Loaded"])
Tick.load([])


def init():
    shutil.rmtree("./pack/functions")
    os.mkdir("./pack/functions")
    
    example_function = Function("example_function", 
    [
    "say Executed",
    "give @p diamond"
    ])
    
    example_egg = SpawnEgg("example_egg", 
    [
    "summon minecraft:tnt ~ ~ ~",
    ])
    
    Tick.build()
    Load.build()
