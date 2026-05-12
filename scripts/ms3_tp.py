import system.lib.minescript as ms
from sys import argv

pstr = "0 56 0"
if len(argv) == 4:
    pstr = ' '.join(argv[1:])

ms.echo(f"Телепорт к точке {pstr}...")
ms.execute(f'tp {pstr}')
