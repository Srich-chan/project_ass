import time

from some_consts import *
from random import randint


x, y, z = map(int, ms.player_position())
_x = x - 3, x + 3
_y = y-1, y+3
_z = z - 3, z + 3
def rand_block():
    x = randint(*_x)
    y = randint(*_y)
    z = randint(*_z)
    return x, y, z

def set_block_to(block, type):
    if ms.get_block(*block) == type: return;
    ms.execute(f"setblock {' '.join(map(str, block))} {type}")

def trashy_search(type: str):
    for x in range(_x[0], _x[1] + 1):
        for y in range(_y[0], _y[1]+1):
            for z in range(_z[0], _z[1] + 1):
                ms.player_look_at(x, y, z)
                if (v:=ms.get_block(x, y, z).lower()) == type:

                    ms.echo(f"Нашёлся! {x, y, z}")
                    set_block_to((x, y, z), 'lime_concrete')
                    time.sleep(1)
                    return x, y, z
                ms.echo(f"{x, y, z}: {v}")
                time.sleep(DELTA/3)
    ms.echo(f"Не нашлось блоков типа {type}")

if __name__ == '__main__':
    for _ in range(10):
        b = rand_block()
        bt = ms.get_block(*b)
        st = "minecraft:light_blue_terracotta"
        set_block_to(b, st)
        r = trashy_search(st)

        set_block_to(b, bt)