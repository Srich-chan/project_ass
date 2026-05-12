from some_consts import *
from random import randint
from math import dist
from ms4_puk import set_block_to

def goto_hor(x: int , z: int):
    st_block = list(map(int, ms.player_position()))
    st_block[1] -= 1
    st_type = ms.get_block(*st_block)

    block = x, st_block[1], z
    b_type = ms.get_block(*block)
    # Метим цель
    set_block_to(st_block, 'red_concrete')
    set_block_to(block, 'lime_concrete')

    # Смотрим ровно на центр блока, сохраняя угол головы
    if dist(st_block, block):
        ms.echo(f"Бегу до {block}")
        ms.player_press_sprint(True)
    else:
        ms.echo(f"Иду до {block}")

    target = x + 0.5, st_block[1]+2.65, z + 0.5
    while not is_near_hor(target, ms.player_position()):
        ms.player_look_at(*target)
        ms.player_press_forward(True)
        time.sleep(DELTA)

    set_block_to(st_block, st_type)
    set_block_to(block, b_type)

    ms.player_press_forward(False)
    ms.player_press_sprint(False)
    time.sleep(0.1)

if __name__ == '__main__':
    from sys import argv
    args = argv[1:]
    if not len(args) == 2:
        x, y, z = map(int, ms.player_position())
        for _ in range(5):
            goto_hor(randint(-10, 10) + x, randint(-10, 10) + z)
        goto_hor(x, z)
    else:
        goto_hor(*map(int, args))