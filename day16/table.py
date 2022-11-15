from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

table = ColorTable()
table = ColorTable(theme=Themes.OCEAN)
table.padding_width = 7

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)