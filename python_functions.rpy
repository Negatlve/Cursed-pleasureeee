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
        order = ["15", "90", "16"]

        global current_boobjob_anim

        if current_boobjob_anim in order:
            idx = order.index(current_boobjob_anim)
            if idx < len(order) - 1:
                current_boobjob_anim = order[idx + 1]
            else:
                current_boobjob_anim = order[0]
        else:
            current_boobjob_anim = "15"

        boobjob_seen.add(current_boobjob_anim)

        renpy.hide_screen("boobjob_anim15")
        renpy.hide_screen("boobjob_anim90")
        renpy.hide_screen("boobjob_anim16")

        renpy.show_screen("boobjob_anim" + current_boobjob_anim)

        # обновляем controls, чтобы Cum появился сразу при 3+ просмотрах
        renpy.hide_screen("boobjob_controls")
        renpy.show_screen("boobjob_controls")


    def BackBoobjobView():
        order = ["15", "90", "16"]

        global current_boobjob_anim

        if current_boobjob_anim in order:
            idx = order.index(current_boobjob_anim)
            if idx > 0:
                current_boobjob_anim = order[idx - 1]
            else:
                current_boobjob_anim = order[-1]
        else:
            current_boobjob_anim = "15"

        boobjob_seen.add(current_boobjob_anim)

        renpy.hide_screen("boobjob_anim15")
        renpy.hide_screen("boobjob_anim90")
        renpy.hide_screen("boobjob_anim16")

        renpy.show_screen("boobjob_anim" + current_boobjob_anim)

        # обновляем controls
        renpy.hide_screen("boobjob_controls")
        renpy.show_screen("boobjob_controls")
default footjob_seen = set()
default current_footjob_anim = "18"

# ===================== ФУНКЦИИ =====================
init python:

    def NextFootjobView():
        order = ["18", "19", "21", "22"]

        global current_footjob_anim

        if current_footjob_anim in order:
            idx = order.index(current_footjob_anim)
            if idx < len(order) - 1:
                current_footjob_anim = order[idx + 1]
            else:
                current_footjob_anim = order[0]
        else:
            current_footjob_anim = "18"

        footjob_seen.add(current_footjob_anim)

        renpy.hide_screen("footjob_anim18")
        renpy.hide_screen("footjob_anim19")
        renpy.hide_screen("footjob_anim21")
        renpy.hide_screen("footjob_anim22")

        renpy.show_screen("footjob_anim" + current_footjob_anim)

        # обновляем controls, чтобы Cum появился сразу при 4+ просмотрах
        renpy.hide_screen("footjob_controls")
        renpy.show_screen("footjob_controls")


    def BackFootjobView():
        order = ["18", "19", "21", "22"]

        global current_footjob_anim

        if current_footjob_anim in order:
            idx = order.index(current_footjob_anim)
            if idx > 0:
                current_footjob_anim = order[idx - 1]
            else:
                current_footjob_anim = order[-1]
        else:
            current_footjob_anim = "18"

        footjob_seen.add(current_footjob_anim)

        renpy.hide_screen("footjob_anim18")
        renpy.hide_screen("footjob_anim19")
        renpy.hide_screen("footjob_anim21")
        renpy.hide_screen("footjob_anim22")

        renpy.show_screen("footjob_anim" + current_footjob_anim)

        # обновляем controls
        renpy.hide_screen("footjob_controls")
        renpy.show_screen("footjob_controls")        
init python:

    def thought_tag(tag, argument, contents):
        return [
            (renpy.TEXT_TAG, "color=#aaaaaa"),
            (renpy.TEXT_TAG, "i")
        ] + contents + [
            (renpy.TEXT_TAG, "/i"),
            (renpy.TEXT_TAG, "/color")
        ]

    config.custom_text_tags["th"] = thought_tag
init python:
    def show_tall(img, height=2060):
        renpy.scene()
        renpy.show("expression", what=img, at_list=[Transform(
            xpos=0.5, 
            xanchor=0.5, 
            ypos=-(height - 1080), 
            yanchor=0.0
        )])
        renpy.call_screen("tall_scroll_helper")            