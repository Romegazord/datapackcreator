import os
import sys

sys.path.append("../DataPackCreator/pack")
sys.path.append("../DataPackCreator/core")
sys.path.append("../DataPackCreator")

import pack

print("Starting creator")
f = open("pack/name.txt", "r")
datapack_name = f.read()

pack.init()

def build():

    os.system("mkdir " + datapack_name)
    os.system(f"robocopy ./core/ExamplePack ./{datapack_name} /E")
    os.system(f"robocopy ./pack ./{datapack_name} pack.mcmeta")
    os.system(f"robocopy ./pack/functions ./{datapack_name}/data/mypack/functions /E")
    os.system(f"robocopy ./pack/tags ./{datapack_name}/data/minecraft/tags/functions /E")
    
    print("Success")
    input("Press any key...")
    
build()