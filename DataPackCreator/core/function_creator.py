import os
from pathlib import Path

func_path = "pack/functions/"
tags_path = "pack/tags/"

def tick(commands):
    if commands:
    
        os.system(f'cd . > {tags_path}tick.json')
        f = open(f"{tags_path}tick.json", "a")
        f.write('{"values":["mypack:tick"]}')
        f.close()
        
        print(f"changing function tick.mcfunction")

        os.system(f'echo # tick.mcfunction, made by DPC > {func_path}tick.mcfunction')

        f = open(f"{func_path}tick.mcfunction", "a")
        for c in commands:
            f.write(c + "\n")
        f.close()

def load(commands):
    if commands:
    
        os.system(f'cd . > {tags_path}load.json')
        f = open(f"{tags_path}load.json", "a")
        f.write('{"values":["mypack:load"]}')
        f.close()
        
        print(f"changing function load.mcfunction")
        
        os.system(f'echo # load.mcfunction, made by DPC > {func_path}load.mcfunction')
            
        f = open(f"{func_path}load.mcfunction", "a")
        for c in commands:
            f.write(c + "\n")
        f.close()

def build(name, commands):
    print(f"building function {name}.mcfunction")
    os.system(f'echo # {name}.mcfunction, made by DPC > {func_path}{name}.mcfunction')
    f = open(f"pack/functions/{name}.mcfunction", "a")
    for c in commands:
        f.write(c + "\n")
    f.close()
    print("done")
    