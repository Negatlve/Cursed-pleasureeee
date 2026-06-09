################################################################################
## Initialization
################################################################################

init offset = -1

default current_anim = "85"
transform about_appear:
    alpha 0.0
    yoffset 30
    easein 0.5 alpha 1.0 yoffset 0

transform glow_pulse:
    alpha 0.05
    linear 2.0 alpha 0.15
    linear 2.0 alpha 0.05
    repeat

transform text_appear(delay=0.0):
    alpha 0.0
    yoffset 15
    pause delay
    easein 0.4 alpha 1.0 yoffset 0

transform button_hover:
    on hover:
        ease 0.2 yoffset -3
    on idle:
        ease 0.2 yoffset 0

transform button_click:
    on selected:
        ease 0.1 zoom 0.95
        ease 0.1 zoom 1.0

transform parallax_bg:
    subpixel True
    xalign 0.5 yalign 0.5
    zoom 1.05
    ease 30.0 xalign 0.51 yalign 0.51
    ease 30.0 xalign 0.49 yalign 0.49
    repeat
transform full_fit:
    fit "contain"
transform ken_burns_effect:
    zoom 0.30
    align (0.5, 0.5)
    
    # Плавное движение по эллипсу
    block:
        ease 3.0 xalign 0.580 yalign 0.420
        ease 3.0 xalign 0.580 yalign 0.580
        ease 3.0 xalign 0.420 yalign 0.580
        ease 3.0 xalign 0.420 yalign 0.420
        ease 3.0 xalign 0.580 yalign 0.420
        repeat

################################################################################
## Styles
################################################################################
# В файле screens.rpy (или где у тебя экраны)

screen simple_elegant_epilogue():
    tag epilogue
    modal True
    
    add Solid("#000022")
    add Solid("#001144", alpha=0.5)
    add Solid("#002266", alpha=0.3)
    
    # Плавные движущиеся точки (остаются без изменений)
    for i in range(50):
        $ x_pos = renpy.random.uniform(0.0, 1.0)
        $ y_pos = renpy.random.uniform(0.0, 1.0)
        $ size = renpy.random.randint(2, 5)
        $ duration = renpy.random.uniform(3.0, 6.0)
        
        add Solid("#88FFFF", alpha=0.15, xsize=size, ysize=size):
            align (x_pos, y_pos)
            at transform:
                alpha 0.0
                pause i * 0.05
                linear 1.0 alpha 0.15
                block:
                    linear duration xoffset renpy.random.randint(-30, 30) yoffset renpy.random.randint(-30, 30)
                    linear duration xoffset 0 yoffset 0
                    repeat
    
    vbox:
        align (0.5, 0.4)
        spacing 20
        
        text _("PROLOGUE COMPLETE"):
            size 46
            color "#FFFFFF"
            align (0.5, 0.5)
            at transform:
                alpha 0.0
                linear 1.5 alpha 1.0
        
        text _("Thank you for playing"):
            size 28
            color "#CCDDFF"
            align (0.5, 0.5)
            at transform:
                alpha 0.0
                pause 0.7
                linear 1.0 alpha 1.0
        
        text _("Save your progress to continue"):
            size 20
            color "#8899CC"
            align (0.5, 0.5)
            at transform:
                alpha 0.0
                pause 1.4
                linear 1.0 alpha 0.8
    
    # === НОВАЯ КНОПКА v0.2 ===
    textbutton "Продолжить":
        align (0.5, 0.62)
        text_size 36
        text_color "#ff3366"
        text_hover_color "#ffffff"
        text_selected_color "#ff6699"
        background None
        action [SetVariable("persistent.prologue_completed", True), Jump("v02_start")]
        at transform:
            alpha 0.0
            pause 2.0
            linear 0.6 alpha 1.0
    
    textbutton _("RETURN TO MENU"):
        align (0.5, 0.7)
        text_size 24
        text_color "#88FFFF"
        text_hover_color "#FFFFFF"
        background None
        action Return()
        at transform:
            alpha 0.0
            pause 2.0
            linear 0.5 alpha 1.0
     # Кнопка бонусной сцены - запускает обычную сцену Ren'Py
    textbutton _("bonus scene"):
        align (0.5, 0.77)
        text_size 18
        text_color "#8899CC"  # Тот же цвет что у подсказки
        text_hover_color "#CCDDFF"  # Светлее при наведении
        text_selected_color "#FFFFFF"
        background None
        # Едва заметное подчёркивание при наведении
        hover_background None
        # Очень лёгкий эффект при наведении
        action Jump("play_bonus_video")
        at transform:
            alpha 0.0
            pause 2.3
            linear 0.5 alpha 0.7 
style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on
    ## the phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window:
    xalign 0
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    focus_mask False
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

## ====================== ЭКРАН ВЫБОРА (3 типа: normal / danger / sexy) ======================
screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            if "{bad}" in i.caption or "{danger}" in i.caption or "GAME OVER" in i.caption.upper() or "КОНЕЦ" in i.caption or "СМЕРТЬ" in i.caption:
                textbutton i.caption.replace("{bad}", "").replace("{danger}", "") action i.action style "choice_button_danger" at danger_pulse
                
            elif "{sexy}" in i.caption:
                textbutton i.caption.replace("{sexy}", "") action i.action style "choice_button_sexy" at sexy_pulse
                
            else:
                textbutton i.caption action i.action at button_hover


## ====================== ОБЫЧНЫЙ ВЫБОР (сине-бирюзовый) ======================
style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button:
    xsize None
    xpadding 55
    ypadding 22
    xminimum 420
    
    background "#0a0a14dd"
    hover_background "#16162bcc"
    drop_shadow (0, 4, 12, "#000000cc")

style choice_button_text:
    font gui.choice_button_text_font
    size gui.choice_button_text_size
    color gui.choice_button_text_idle_color
    hover_color gui.choice_button_text_hover_color
    xalign 0.5
    text_align 0.5
    bold True
    outlines [(4, "#000000", 0, 0), (1, "#00ccff", 0, 0)]
    hover_outlines [(4, "#000000", 0, 0), (2, "#00ffff", 0, 0), (1, "#33C5F0", 0, 0)]


## ====================== ОПАСНЫЙ ВЫБОР (красный) ======================
style choice_button_danger:
    xsize None
    xpadding 55
    ypadding 26
    xminimum 420
    
    background "#2a0a0add"
    hover_background "#440f0fcc"
    drop_shadow (0, 6, 20, "#ff0000aa")

style choice_button_danger_text:
    font gui.choice_button_text_font
    size gui.choice_button_text_size + 2
    color "#ff5555"
    hover_color "#ff7777"
    xalign 0.5
    text_align 0.5
    bold True
    outlines [(5, "#000000", 0, 0), (2, "#ff2222", 0, 0)]
    hover_outlines [(5, "#000000", 0, 0), (3, "#ff0000", 0, 0), (2, "#ff8888", 0, 0)]


## ====================== SEXY ВЫБОР (розово-сексуальный) ======================
style choice_button_sexy:
    xsize None
    xpadding 55
    ypadding 26
    xminimum 420
    
    background "#2a0a1add"
    hover_background "#3f0f2acc"
    drop_shadow (0, 5, 18, "#ff69b4aa")

style choice_button_sexy_text:
    font gui.choice_button_text_font
    size gui.choice_button_text_size + 1
    color "#ff69b4"
    hover_color "#ff99cc"
    xalign 0.5
    text_align 0.5
    bold True
    outlines [(4, "#000000", 0, 0), (2, "#ff1493", 0, 0)]
    hover_outlines [(4, "#000000", 0, 0), (3, "#ff69b4", 0, 0), (2, "#ffb6ff", 0, 0)]


## ====================== АНИМАЦИИ ======================
transform button_hover:
    on hover:
        ease 0.2 yoffset -4
    on idle:
        ease 0.2 yoffset 0

transform danger_pulse:
    zoom 1.0
    on hover:
        linear 0.7 zoom 1.04
        linear 0.7 zoom 1.0
        repeat
    on idle:
        linear 0.4 zoom 1.0

transform sexy_pulse:
    zoom 1.0
    on hover:
        linear 0.6 zoom 1.035
        linear 0.6 zoom 1.0
        repeat
    on idle:
        linear 0.5 zoom 1.0


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-
## game menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button:
    background None
    xpadding 15
    ypadding 0

style quick_button_text:
    font gui.interface_text_font
    size gui.quick_button_text_size                     # 21 — как было
    idle_color "#aaaaaa14"      # оригинальный gui.idle_small_color (#aaaaaa) + 8% прозрачность
    hover_color gui.accent_color  # #33C5F0 — яркий при наведении
    selected_color gui.quick_button_text_selected_color
    insensitive_color "#88888814" # серый + небольшая прозрачность
    outlines [(2, "#00000099", 0, 0)]   # лёгкая обводка
    xalign 0.5
    text_align 0.5

style quick_menu:
    xalign 0.5
    yalign 1.0




################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

transform calm_glow:
    alpha 0.12
    block:
        easein 3.0 alpha 0.18
        easeout 3.0 alpha 0.12
        repeat

transform hover_pulse:
    on hover:
        additive 0.0
        zoom 1.0
        easein 0.15 additive 0.3 zoom 1.05
        easeout 0.3 additive 0.0 zoom 1.0
    on idle:
        additive 0.0
        zoom 1.0

transform neon_text_flash:
    alpha 0.0
    block:
        easein 2.0 alpha 0.7
        easeout 2.0 alpha 0.0
        repeat

screen main_menu():
    tag menu
    modal True

    add "images/background.webp" at full_fit
    add Solid("#00000066")

    hbox:
        xalign 0.98
        yalign 0.02
        spacing 10
        
        textbutton "EN" action Language("english"):
            style "language_button"
        textbutton "RU" action Language(None):
            style "language_button"
            
    vbox:
        xpos 40
        yalign 0.5  # Центрирование (как было изначально)
        # !!! ИЗМЕНЕНО: Сдвигаем весь блок на 100 пикселей вверх !!!
        yoffset -50
        # !!! ИЗМЕНЕНО !!!
        spacing 80
        fixed:
            xysize (380, 90)

        # Список элементов, теперь включает "Gallery"
        for item in ["Start", "Load", "Preferences", "Gallery", "About", "Quit"]:

            fixed:
                xysize (380, 90)

                # Спокойное свечение под кнопкой
                add Solid("#00ccff"):
                    xalign 0.5 yalign 0.5
                    xysize (380, 90)
                    alpha 0.12
                    at calm_glow

                # Кнопка с вспышкой при наведении
                imagebutton:
                    xalign 0.5 yalign 0.5
                    xysize (380, 90)
                    idle Solid("#00ccff00")
                    hover Solid("#00ccff88")
                    
                    # Список действий
                    action [Start(), ShowMenu("load"), ShowMenu("preferences"), Show("gallery"), ShowMenu("about"), Quit(confirm=False)]\
                        [["Start","Load","Preferences","Gallery","About","Quit"].index(item)]
                    at hover_pulse

                # Основной текст
                text item:
                    xalign 0.5 yalign 0.5
                    size 46
                    color "#ffffff"
                    outlines [(7, "#000000", 0, 0), (3, "#00ccff", 0, 0)]

                # Неоновая вспышка текста
                text item at neon_text_flash:
                    xalign 0.5 yalign 0.5
                    size 46
                    color "#00ffff"
                    outlines [(5, "#00ccff", 0, 0), (2, "#00ffff", 0, 0)]

    # Информация о игре в правом нижнем углу
    vbox:
        xalign 0.95
        yalign 0.98
        spacing 5
        
        text "Cursed Pleasure":
            size 56
            color "#ffffff"
            outlines [(3, "#000000", 0, 0), (1, "#00ccff", 0, 0)]
            
        text "Prologue":
            xpos 10
            size 27
            color "#cccccc"
            outlines [(2, "#000000", 0, 0), (1, "#00ccff", 0, 0)]
    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    



style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
    tag menu
    modal True
    
    # Фон с параллакс-эффектом
    add "background.png" at full_fit
    add "#0008"
    
    # Центральная панель с анимацией появления
    fixed at about_appear:
        xsize 900
        ysize 700 
        align (0.5, 0.5)
        
        # Фон панели с эффектом стекла
        add Solid("#000000", alpha=0.8):
            xsize 900
            ysize 700
        
        # Пульсирующее свечение по краям
        add Solid("#88FFFF", alpha=0.05, xsize=904, ysize=4) at glow_pulse:
            align (0.5, 0.0) yoffset -2
        add Solid("#88FFFF", alpha=0.05, xsize=904, ysize=4) at glow_pulse:
            align (0.5, 1.0) yoffset 2
        add Solid("#88FFFF", alpha=0.05, xsize=4, ysize=704) at glow_pulse:
            align (0.0, 0.5) xoffset -2
        add Solid("#88FFFF", alpha=0.05, xsize=4, ysize=704) at glow_pulse:
            align (1.0, 0.5) xoffset 2
        
        # Содержимое с последовательным появлением
        vbox:
            align (0.5, 0.5)
            spacing 35
            xsize 800
            
            # Заголовок
            text "ABOUT" at text_appear(0.1):
                size 48
                color "#88FFFF"
                outlines [(3, "#000000", 0, 0)]
                xalign 0.5
                yoffset 23
            
            # Разделитель с анимацией
            add Solid("#88FFFF", xsize=500, ysize=1, alpha=0.3) at text_appear(0.2):
                xalign 0.5
            
            # Основная информация
            vbox at text_appear(0.3):
                spacing 25
                xsize 750
                xalign 0.5
                
                text "[config.name]":
                    size 36
                    color "#FFFFFF"
                    xalign 0.5
                
                text "Created by [gui.author]":
                    size 20
                    color "#AABBEE"
                    xalign 0.5
            
            # Описание 1
            frame at text_appear(0.4):
                background Solid("#001122", alpha=0.4)
                xsize 700
                padding (30, 25)
                xalign 0.5
                
                vbox:
                    spacing 15
                    
                    text "About this project:":
                        size 20
                        color "#88FFFF"
                        xalign 0.5
                    
                    text "This visual novel is the reason I'm sorely lacking good games about corruption and taboos, and I don't want to wait three months for good games to be updated. So I decided to keep myself busy by creating my own game.":
                        size 16
                        color "#CCDDFF"
                        text_align 0.5
                        line_leading 8
            
            # Описание 2
            frame at text_appear(0.5):
                background Solid("#001122", alpha=0.4)
                xsize 700
                padding (30, 25)
                xalign 0.5
                
                vbox:
                    spacing 15
                    
                    text "Special thanks:":
                        size 20
                        color "#88FFFF"
                        xalign 0.5
                    
                    text "To all the people who make DAZ3D/Ren'py guides on YouTube, and to Elon Musk for creating Grok.":
                        size 16
                        color "#CCDDFF"
                        text_align 0.5
                        line_leading 8
            
            # Кнопка закрытия с улучшенным стилем
            textbutton "CLOSE" at text_appear(0.6), button_hover, button_click:
                style "about_close_button"
                xalign 0.5
                yoffset -10
                action Return()

# Стиль для кнопки Close (добавьте в стили или в screen)
style about_close_button:
    background Solid("#00000000")
    
    insensitive_background Solid("#00000044")
    padding (0, 0)
    xsize 100
    
style about_close_button_text:
    color "#88FFFF"
    hover_color "#FFFFFF"
    insensitive_color "#666666"
    size 24
    bold True
    outlines [(2, "#000000", 0, 0)]
    hover_outlines [(2, "#000000", 0, 0)]
    insensitive_outlines [(2, "#000000", 0, 0)]

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of
            ## the buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better
## suit themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                        

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
                    
                ## Additional vboxes of type "radio_pref" or "check_pref" can
                ## be added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character,
                        ## if set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly
        ## if config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed
## at once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using
## speech bubbles. The bubble screen takes the same parameters as the say
## screen, must create a displayable with the id of "what", and can create
## displayables with the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"



style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

        # ← сюда просто копируй новые блоки для следующих сцен
# ===================================================================
# ВВОД ИМЕНИ — ФИНАЛЬНАЯ ВЕРСИЯ (картинки видны, всё работает)
# ===================================================================

transform fade_in_image(t=0.8):
    alpha 0.0
    easein t alpha 1.0

transform button_hover_effect:
    on hover:
        ease 0.2 yoffset -4 zoom 1.05
    on idle:
        ease 0.3 yoffset 0 zoom 1.0

transform particle_drift(seed):
    alpha 0.12
    xsize 3 ysize 3
    xpos renpy.random.uniform(0.0, 1.0)
    ypos renpy.random.uniform(0.0, 1.0)
    block:
        linear renpy.random.uniform(4.0, 8.0) xpos (renpy.random.uniform(-0.1, 1.1)) ypos (renpy.random.uniform(-0.1, 1.1))
        linear renpy.random.uniform(4.0, 8.0) xpos renpy.random.uniform(0.0, 1.0) ypos renpy.random.uniform(0.0, 1.0)
        repeat

screen name_input_particles():
    for i in range(40):
        add Solid("#88FFFF") at particle_drift(i)

# ЭКРАН ВВОДА ИМЕНИ
screen sexy_name_input():
    modal True
    zorder 100

    # 1. Сначала — лёгкое затемнение (фон)
    add Solid("#000000", alpha=0.35)

    # 2. Потом — твоя картинка НАД затемнением
    add "images/281.png":
        xalign 0.5 yalign 0.5
        fit "cover"          # идеально заполняет экран, не обрезая
        at fade_in_image(0.6)

    # 3. Частицы и текст — сверху
    use name_input_particles

    vbox xalign 0.5 yalign 0.68 spacing 40:

        text _("Скажи мне своё настоящее имя…\nЯ хочу кричать его, пока ты делаешь со мной всё, что захочешь.\nНе стесняйся, милый. Сегодня я полностью твоя."):
            font "ttf/Comfortaa-Bold.ttf"
            size 44 color "#ff88cc"
            outlines [(4, "#000000",0,0), (2, "#ff3399",0,0)]
            text_align 0.5 xalign 0.5
            slow_cps 28
            at fade_in_image(1.4)

        frame:
            background None                     # ← Убираем бирюзовую рамку
            hover_background None               # ← Убираем подсветку при наведении
            xsize 950 ysize 90 xalign 0.5

            input:
                value VariableInputValue("persistent.player_name", returnable=True)
                length 20
                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя -"
                default (persistent.player_name or "")
                color "#ffffff"
                size 54
                font "ttf/Comfortaa-Bold.ttf"
                xalign 0.5 yalign 0.5
                # Добавляем красивый неоновый контур только вокруг текста
                outlines [(3, "#00ccff", 0, 0)]

    textbutton _("ГОТОВО"):
        xalign 0.5 yalign 0.86
        text_font "ttf/Comfortaa-Bold.ttf" text_size 48
        text_color "#88FFFF" text_hover_color "#ffffff"
        text_outlines [(4,"#000000",0,0),(2,"#00ccff",0,0)]
        background None
        action Return()
        at button_hover_effect, fade_in_image(1.8)

# ЭКРАН ПОДТВЕРЖДЕНИЯ
screen name_confirmed():
    modal True
    zorder 100

    add Solid("#000000", alpha=0.35)

    add "images/282.png":
        xalign 0.5 yalign 0.5
        fit "cover"
        at fade_in_image(0.6)

    use name_input_particles

    vbox xalign 0.5 yalign 0.82 spacing 30:
        text "[persistent.player_name]…":
            font "ttf/Comfortaa-Bold.ttf" size 72 color "#ff66cc"
            outlines [(5,"#000000",0,0),(2,"#ff3399",0,0)]
            xalign 0.5 at fade_in_image(0.8)

        text _("Я уже вся горю от нетерпения.\nПора начинать."):
            font "ttf/Comfortaa-Bold.ttf" size 48 color "#ff99dd"
            outlines [(3,"#000000",0,0)]
            xalign 0.5 at fade_in_image(1.5)

    timer 3.2 action Return()        

# Кастомный стиль для menu
style my_menu_vbox is vbox:
    xalign 0.5
    ypos 260
    spacing 35

style my_menu_button is button:
    xsize 820
    ysize 88
    background None
    hover_background Solid("#ffffff", alpha=0.12)

style my_menu_button_text is button_text:
    size 31
    color "#ffffff"
    hover_color "#ff6699"
    outlines [(3, "#000000", 0, 0)]
    xalign 0.5
    yalign 0.5        
# ====================== ВЫБОР ЧАСТИ ТЕЛА ======================
screen linda_body_selection():
    modal True
    zorder 200
    
    if linda_body_hover == "boobs":
        add "329.webp" at truecenter
    elif linda_body_hover == "foot":
        add "328.webp" at truecenter
    elif linda_body_hover == "hand":
        add "327.webp" at truecenter
    else:
        add "326.webp" at truecenter
    
    imagebutton:
        idle Solid("#00000000", xsize=569, ysize=408)
        hover Solid("#00000000", xsize=569, ysize=408)
        xpos 389 ypos 672
        action [Hide("linda_body_selection"), Hide("tooltip"), Jump("linda_footjob")]
        hovered [SetVariable("linda_body_hover", "foot"), Show("tooltip", text="Ноги (Footjob)"), renpy.restart_interaction]
        unhovered [SetVariable("linda_body_hover", "none"), Hide("tooltip"), renpy.restart_interaction]
    
    imagebutton:
        idle Solid("#00000000", xsize=301, ysize=248)
        hover Solid("#00000000", xsize=301, ysize=248)
        xpos 693 ypos 424
        action [Hide("linda_body_selection"), Hide("tooltip"), Jump("linda_boobjob")]
        hovered [SetVariable("linda_body_hover", "boobs"), Show("tooltip", text="Сиськи (Boobjob)"), renpy.restart_interaction]
        unhovered [SetVariable("linda_body_hover", "none"), Hide("tooltip"), renpy.restart_interaction]
    
    imagebutton:
        idle Solid("#00000000", xsize=640, ysize=599)
        hover Solid("#00000000", xsize=640, ysize=599)
        xpos 958 ypos 424
        action [Hide("linda_body_selection"), Hide("tooltip"), Jump("linda_handjob")]
        hovered [SetVariable("linda_body_hover", "hand"), Show("tooltip", text="Рука (Handjob)"), renpy.restart_interaction]
        unhovered [SetVariable("linda_body_hover", "none"), Hide("tooltip"), renpy.restart_interaction]

screen tooltip(text=""):
    zorder 300
    frame:
        background None
        xalign 0.5 yalign 0.92
        padding (20, 8)
        
        text text:
            size 28
            color "#88FFFF"
            outlines [(4, "#003333", 0, 0), (2, "#aaffff", 0, 0)]
            text_align 0.5
screen handjob_controls():
    zorder 200
    modal False

    frame:
        xalign 0.95
        yalign 0.5
        xsize 200
        background "#1a1a2ecc"

        vbox:
            spacing 12
            xalign 0.5

            textbutton "Next":
                action Function(NextHandjobView)
                xsize 160

            textbutton "Back":
                action Function(BackHandjobView)
                xsize 160

            null height 20

            if len(handjob_seen) >= 4:
                textbutton "Cum":
                    action Jump("handjob_cum")
                    xsize 160
                    text_color "#ff4444"
screen handjob_anim85():
    zorder 0
    add "anim85" at fullscreen

screen handjob_anim86():
    zorder 0
    add "anim86" at fullscreen

screen handjob_anim87():
    zorder 0
    add "anim87" at fullscreen

screen handjob_anim88():
    zorder 0
    add "anim88" at fullscreen

screen handjob_anim89():
    zorder 0
    add "anim89" at fullscreen                
screen boobjob_anim15():
    zorder 0
    add "anim15" at fullscreen

screen boobjob_anim90():
    zorder 0
    add "anim90" at fullscreen

screen boobjob_anim16():
    zorder 0
    add "anim16" at fullscreen

screen boobjob_controls():
    zorder 200
    modal False

    frame:
        xalign 0.95 yalign 0.5 xsize 200
        background "#1a1a2ecc"

        vbox:
            spacing 12 xalign 0.5

            textbutton "Next":
                action Function(NextBoobjobView)
                xsize 160

            textbutton "Back":
                action Function(BackBoobjobView)
                xsize 160

            null height 20

            if len(boobjob_seen) >= 3:
                textbutton "Cum":
                    action Jump("boobjob_choose_cum")
                    xsize 160
                    text_color "#ff4444"
screen footjob_controls():
    zorder 200
    modal False

    frame:
        xalign 0.95
        yalign 0.5
        xsize 200
        background "#1a1a2ecc"

        vbox:
            spacing 12
            xalign 0.5

            textbutton "Next":
                action Function(NextFootjobView)
                xsize 160

            textbutton "Back":
                action Function(BackFootjobView)
                xsize 160

            null height 20

            if len(footjob_seen) >= 4:
                textbutton "Cum":
                    action Jump("footjob_cum")
                    xsize 160
                    text_color "#ff4444"

screen footjob_anim18():
    zorder 0
    add "anim18" at fullscreen

screen footjob_anim19():
    zorder 0
    add "anim19" at fullscreen

screen footjob_anim21():
    zorder 0
    add "anim21" at fullscreen

screen footjob_anim22():
    zorder 0
    add "anim22" at fullscreen                    
screen tall_scroll_helper(img, img_height=2160, start_from_bottom=True):
    modal True

    # Прокрутка (само изображение уже показано через show)
    key "mousedown_5" action NullAction()  # вверх
    key "mousedown_4" action NullAction()  # вниз

    # Реальная прокрутка будет работать через показанное изображение, но для удобства оставляем
    key "mouseup_1" action Return()
    key "K_ESCAPE" action Return()

    text "Колёсико ↑↓ • ЛКМ/Esc = Закрыть" size 26 color "#cccccc" xalign 0.98 yalign 0.02