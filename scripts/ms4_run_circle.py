from some_consts import *
from system.lib.minescript import player_orientation

phi, _ = ms.player_orientation()
step = 2

timer = Timer(30)
ms.player_press_sprint(True)
ms.player_press_forward(True)
while not timer.is_ended():
    phi += step
    ms.player_set_orientation(phi, player_orientation()[1])
    time.sleep(DELTA)

ms.player_press_forward(False)
ms.player_press_sprint(False)
