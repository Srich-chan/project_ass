from some_consts import *
from random import randint
from sys import argv
from ms5_runrunrun import set_block_to

t = 3
if len(argv) == 2:
    t = float(argv[1])

blocks = {}
timer = Timer(t)

while not timer.is_ended():
    block = [int(i) for i in ms.player_position()]
    block[1] -= 1;
    block = tuple(block)

    if block not in blocks:
        blocks[block] = ms.get_block(*block)
        set_block_to(block, 'red_concrete')
    time.sleep(DELTA)

for block in blocks:
    set_block_to(block, 'air')
    ms.execute(f"/summon tnt {' '.join(map(str, block))}")

time.sleep(3)
ms.execute('kill @e[type=minecraft:tnt]')

for block in blocks:
    set_block_to(block, blocks[block])

for x, z in [(randint(-20, 20), randint(-20, 20)) for _ in range(100)]:
    ms.execute(f"/summon tnt ~{x} ~10 ~{z}")

time.sleep(3)
ms.execute('/kill @e[type=minecraft:tnt]')
