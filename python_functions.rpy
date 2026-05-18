# ===================== ПЕРЕМЕННЫЕ =====================
default handjob_seen = set()
default current_handjob_anim = "85"
default boobjob_seen = set()
default current_boobjob_anim = "15"


# ===================== ФУНКЦИИ =====================
init python:

    def NextHandjobView():
        order = ["85", "86", "87", "88"]

        global current_handjob_anim

        if current_handjob_anim in order:
            idx = order.index(current_handjob_anim)
            if idx < len(order) - 1:
                current_handjob_anim = order[idx + 1]
            else:
                current_handjob_anim = "89"
        else:
            current_handjob_anim = "85"

        handjob_seen.add(current_handjob_anim)

        renpy.hide_screen("handjob_anim85")
        renpy.hide_screen("handjob_anim86")
        renpy.hide_screen("handjob_anim87")
        renpy.hide_screen("handjob_anim88")

        if current_handjob_anim != "89":
            renpy.show_screen("handjob_anim" + current_handjob_anim)
        else:
            renpy.jump("handjob_cum")


    def BackHandjobView():
        order = ["85", "86", "87", "88"]

        global current_handjob_anim

        if current_handjob_anim in order:
            idx = order.index(current_handjob_anim)
            if idx > 0:
                current_handjob_anim = order[idx - 1]
            else:
                current_handjob_anim = "85"
        else:
            current_handjob_anim = "85"

        renpy.hide_screen("handjob_anim85")
        renpy.hide_screen("handjob_anim86")
        renpy.hide_screen("handjob_anim87")
        renpy.hide_screen("handjob_anim88")

        renpy.show_screen("handjob_anim" + current_handjob_anim)
init python:
    def NextBoobjobView():
        global current_boobjob_anim
        hide_all_boobjob_anims()
        
        if current_boobjob_anim == "15":
            renpy.jump("boobjob_view90")
        elif current_boobjob_anim == "90":
            renpy.jump("boobjob_view16")
        elif current_boobjob_anim == "16":
            renpy.jump("boobjob_view15")  # цикл

    def BackBoobjobView():
        global current_boobjob_anim
        hide_all_boobjob_anims()
        
        if current_boobjob_anim == "15":
            renpy.jump("boobjob_view16")
        elif current_boobjob_anim == "90":
            renpy.jump("boobjob_view15")
        elif current_boobjob_anim == "16":
            renpy.jump("boobjob_view90")

    def hide_all_boobjob_anims():
        renpy.hide_screen("boobjob_anim15")
        renpy.hide_screen("boobjob_anim90")
        renpy.hide_screen("boobjob_anim16")
        renpy.restart_interaction()