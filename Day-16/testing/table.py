from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Game", ['Sekiro', 'Elden Ring', 'Bloodborne'])
table.add_column("Genre", ['SoulsBorne', 'SoulsBorne', 'SoulsBorne'])
table.align = 'l'
print(table)

