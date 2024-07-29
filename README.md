# datapackcreator
Making data packs for minecraft is easier. Alpha version

you also need Python 3.4+ installed

How to use:
  you can change name in name.txt
  and redact pack.mcmeta
  
  then go to /pack/pack.py
  to add function use 
  
    Function(name, [command, command, ...]) --- creates function with name
  
  there alse some presets (only 1 for now):

    SpawnEgg(name, [command, command, ...]) --- adds function egg giver named as {name}_give_spawn_egg, executes at position of spawned entity and immeadeatly kills it

  when everything is ready click on build.bat then move finished data pack to minecraft
