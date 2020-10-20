import nuke

import source/arcade_nuke

menu = nuke.menu("Nuke")
menu.addCommand("Arcade/Start Playing...", arcade_nuke.open_dialog)
