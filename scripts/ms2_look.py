from some_consts import *
from random import randint

timer = Timer(30)
while not timer.is_ended():
    # Случайный блок
    x, y, z = o = [randint(-50, 50) + p for _, p in
                   zip(range(3), ms.player_position())]
    # Зырим на центр блока на уровне глаз
    ms.player_look_at(x + 0.5, y + 1.65, z + 0.5)
    ms.echo(f"Смотрю на на [{x:.3f} {y:.3f} {z:.3f}] : {ms.get_block(*o)}\n")
    time.sleep(0.5)
