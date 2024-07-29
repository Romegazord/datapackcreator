import function_creator

class Function:
    def __init__(self, name, commands):
        self.name = name
        function_creator.build(f"{name}", commands)

tick_commands = ""
load_commands = "" 

class Tick:
     
    def load(commands):
        global tick_commands
        for c in commands:
            tick_commands += c + "\n"
    def build():
        function_creator.tick([tick_commands])

class Load:
    def load(commands):
        global load_commands
        for c in commands:
            load_commands += c + "\n"
    def build():
        function_creator.load([load_commands])
class SpawnEgg:
    def __init__(self, name, commands):
        self.name = name
        condition = f"execute if entity @e[tag={name}] run execute at @e[tag={name}] run"
        self.command = ""
        for c in commands:
            self.command = f"{self.command}{condition} {c}\n"
        Tick.load([self.command, condition + f" kill @e[tag={name}]"])
        function_creator.build(f"{name}_give_spawn_egg", 
        [
        'give @p bat_spawn_egg{EntityTag:{NoAI:1b,NoGravity:1b,PersistenceRequired:1b,Tags:["' +name+ '"],Silent:1b,ActiveEffects:[{Id:14,Duration:999999,Amplifier:1,ShowParticles:0b}]},display:{Name:\'[{"text":"' +name+ '","italic":false}]\'}} 1'
        ])
        