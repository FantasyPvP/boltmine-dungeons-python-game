import character
import console
import world

character = character.Character()
console = console.Console()
console.output_("console is working", "status", None)
character.name = console.input_("enter a name for your character:\n╰─> ", "colour", "cyan-bold")
console.output_(f"╰─> character name set to {character.name}", "colour", "green-bold")
bozo = console.input_("are you a bozo?\n╰─> ", "colour", "magenta-bold")


