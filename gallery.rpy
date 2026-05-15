# gallery.rpy — updated version with main menu style
default persistent.gallery_prologue = False
default persistent.gallery_monica_boobs = False
default persistent.gallery_firstjerk = False
default persistent.gallery_monica_boobs_jerk = False
default persistent.gallery_sara_pool_hj = False
default persistent.gallery_bonus1 = False

default last_replay = None
default show_all_scenes = False  # Флаг для показа всех сцен

# Функция для проверки, доступна ли сцена в текущем режиме
init python:
    def is_scene_visible_in_gallery(scene_flag):
        # Если включен режим показа всех сцен, то все доступны
        if store.show_all_scenes:
            return True
        # Иначе проверяем реальный прогресс игрока
        return scene_flag

transform calm_glow_gallery:
    alpha 0.08
    block:
        easein 3.0 alpha 0.12
        easeout 3.0 alpha 0.08
        repeat

transform hover_pulse_gallery:
    on hover:
        additive 0.0
        zoom 1.0
        easein 0.15 additive 0.15 zoom 1.02
        easeout 0.3 additive 0.0 zoom 1.0
    on idle:
        additive 0.0
        zoom 1.0

transform neon_text_flash_gallery:
    alpha 0.0
    block:
        easein 2.0 alpha 0.5
        easeout 2.0 alpha 0.0
        repeat

# Трансформ для текста LOCKED - появляется и быстро исчезает при наведении
transform locked_text_appear:
    alpha 0.0
    on hover:
        alpha 1.0
        pause 0.8  # Показывается 0.8 секунды
        linear 0.3 alpha 0.0  # Затем исчезает за 0.3 секунды
    on idle:
        alpha 0.0

# Кастомное действие для закрытия галереи
init python:
    class CloseGalleryAction(Action):
        def __call__(self):
            # Сначала скрываем галерею
            renpy.hide_screen("gallery", layer="screens")
            # Затем возвращаемся в главное меню
            renpy.full_restart()
        
        def get_sensitive(self):
            return True
    
    # Кастомное действие для показа/скрытия всех сцен
    class ToggleShowAllScenesAction(Action):
        def __call__(self):
            # Переключаем режим показа
            store.show_all_scenes = not store.show_all_scenes
            if store.show_all_scenes:
                renpy.notify("Showing all scenes")
            else:
                renpy.notify("Showing only unlocked scenes")
            
            # Обновляем экран
            renpy.restart_interaction()
        
        def get_selected(self):
            return store.show_all_scenes

screen gallery():
    tag menu
    modal True

    # Main menu background style с сильным затемнением
    add "images/background.webp" at full_fit
    add Solid("#000000DD")  # Сильное затемнение

    # Gallery title с вашим шрифтом
    text "GALLERY":
        xalign 0.5
        yalign 0.12
        size 56
        color "#ffffff"
        outlines [(3, "#000000", 0, 0), (1, "#00ccff", 0, 0)]
        font "ttf/Comfortaa-Bold.ttf"

    # Grid of gallery items
    grid 3 2:
        xalign 0.5
        yalign 0.55
        xspacing 40
        yspacing 40

        # Scene 1: Prologue
        fixed:
            xysize (360, 240)
            
            # Проверяем, видна ли сцена в текущем режиме
            $ scene_visible = is_scene_visible_in_gallery(persistent.gallery_prologue)
            
            # Превью
            button:
                xysize (360, 240)
                background None
                at hover_pulse_gallery
                if scene_visible:
                    action [Hide("gallery", dissolve), 
                           SetVariable("is_gallery_replay", True), 
                           Start("replay_prologue")]
                else:
                    action NullAction()
                
                if scene_visible:
                    add "253.webp" xysize (360, 240)
                else:
                    # Для невидимых сцен делаем картинку темной
                    add "253.webp" xysize (360, 240) at transform:
                        matrixcolor BrightnessMatrix(-0.4)  # Темная картинка
                
                # Текст LOCKED внутри кнопки - появляется при наведении на невидимую сцену
                if not scene_visible:
                    text "LOCKED":
                        align (0.5, 0.5)
                        size 28
                        color "#ffffff"
                        outlines [(4, "#000000", 0, 0)]
                        font "ttf/Comfortaa-Bold.ttf"
                        at locked_text_appear

        # Scene 2: Monica - Boobs
        fixed:
            xysize (360, 240)
            
            $ scene_visible = is_scene_visible_in_gallery(persistent.gallery_monica_boobs)
            
            # Превью
            button:
                xysize (360, 240)
                background None
                at hover_pulse_gallery
                if scene_visible:
                    action [Hide("gallery", dissolve), 
                           SetVariable("is_gallery_replay", True), 
                           Start("replay_monica_boobs")]
                else:
                    action NullAction()
                
                if scene_visible:
                    add "images/101.webp" xysize (360, 240)
                else:
                    add "images/101.webp" xysize (360, 240) at transform:
                        matrixcolor BrightnessMatrix(-0.4)
                
                # Текст LOCKED
                if not scene_visible:
                    text "LOCKED":
                        align (0.5, 0.5)
                        size 28
                        color "#ffffff"
                        outlines [(4, "#000000", 0, 0)]
                        font "ttf/Comfortaa-Bold.ttf"
                        at locked_text_appear

        # Scene 3: First Jerk
        fixed:
            xysize (360, 240)
            
            $ scene_visible = is_scene_visible_in_gallery(persistent.gallery_firstjerk)
            
            # Превью
            button:
                xysize (360, 240)
                background None
                at hover_pulse_gallery
                if scene_visible:
                    action [Hide("gallery", dissolve), 
                           SetVariable("is_gallery_replay", True), 
                           Start("replay_firstjerk")]
                else:
                    action NullAction()
                
                if scene_visible:
                    add "images/131.webp" xysize (360, 240)
                else:
                    add "images/131.webp" xysize (360, 240) at transform:
                        matrixcolor BrightnessMatrix(-0.4)
                
                # Текст LOCKED
                if not scene_visible:
                    text "LOCKED":
                        align (0.5, 0.5)
                        size 28
                        color "#ffffff"
                        outlines [(4, "#000000", 0, 0)]
                        font "ttf/Comfortaa-Bold.ttf"
                        at locked_text_appear

        # Scene 4: Monica Pool
        fixed:
            xysize (360, 240)
            
            $ scene_visible = is_scene_visible_in_gallery(persistent.gallery_monica_boobs_jerk)
            
            # Превью
            button:
                xysize (360, 240)
                background None
                at hover_pulse_gallery
                if scene_visible:
                    action [Hide("gallery", dissolve), 
                           SetVariable("is_gallery_replay", True), 
                           Start("replay_monica_pool")]
                else:
                    action NullAction()
                
                if scene_visible:
                    add "images/188.webp" xysize (360, 240)
                else:
                    add "images/188.webp" xysize (360, 240) at transform:
                        matrixcolor BrightnessMatrix(-0.4)
                
                # Текст LOCKED
                if not scene_visible:
                    text "LOCKED":
                        align (0.5, 0.5)
                        size 28
                        color "#ffffff"
                        outlines [(4, "#000000", 0, 0)]
                        font "ttf/Comfortaa-Bold.ttf"
                        at locked_text_appear

        # Scene 5: Sara HJ
        fixed:
            xysize (360, 240)
            
            $ scene_visible = is_scene_visible_in_gallery(persistent.gallery_sara_pool_hj)
            
            # Превью
            button:
                xysize (360, 240)
                background None
                at hover_pulse_gallery
                if scene_visible:
                    action [Hide("gallery", dissolve), 
                           SetVariable("is_gallery_replay", True), 
                           Start("replay_sara_hj")]
                else:
                    action NullAction()
                
                if scene_visible:
                    add "images/236.webp" xysize (360, 240)
                else:
                    add "images/236.webp" xysize (360, 240) at transform:
                        matrixcolor BrightnessMatrix(-0.4)
                
                # Текст LOCKED
                if not scene_visible:
                    text "LOCKED":
                        align (0.5, 0.5)
                        size 28
                        color "#ffffff"
                        outlines [(4, "#000000", 0, 0)]
                        font "ttf/Comfortaa-Bold.ttf"
                        at locked_text_appear

        # Scene 6: Bonus
        fixed:
            xysize (360, 240)
            
            $ scene_visible = is_scene_visible_in_gallery(persistent.gallery_bonus1)
            
            # Превью
            button:
                xysize (360, 240)
                background None
                at hover_pulse_gallery
                if scene_visible:
                    action [Hide("gallery", dissolve), 
                           SetVariable("is_gallery_replay", True), 
                           Start("replay_bonus1")]
                else:
                    action NullAction()
                
                if scene_visible:
                    add "279.webp" xysize (360, 240)
                else:
                    add "279.webp" xysize (360, 240) at transform:
                        matrixcolor BrightnessMatrix(-0.4)
                
                # Текст LOCKED
                if not scene_visible:
                    text "LOCKED":
                        align (0.5, 0.5)
                        size 28
                        color "#ffffff"
                        outlines [(4, "#000000", 0, 0)]
                        font "ttf/Comfortaa-Bold.ttf"
                        at locked_text_appear

    # Кнопка закрытия
    button:
        xalign 0.9
        yalign 0.1
        xysize (70, 70)
        background None
        action CloseGalleryAction()
        keysym "game_menu"
        
        text "X":
            xalign 0.5
            yalign 0.5
            size 70
            color "#aaaaaa"
            outlines [(3, "#00ccff", 0, 0)]
            hover_color "#ffffff"
            font "ttf/Comfortaa-Bold.ttf"

    # Кнопка показа/скрытия всех сцен
    vbox:
        xalign 0.03
        yalign 0.97
        spacing 10
        
        if show_all_scenes:
            textbutton "{size=20}SHOW ONLY UNLOCKED{/size}":
                text_font "ttf/Comfortaa-Bold.ttf"
                text_color "#00ccff"  # Синий когда активен
                text_hover_color "#00ffff"
                text_outlines [(2, "#000000", 0, 0)]
                background None
                hover_background None
                action ToggleShowAllScenesAction()
                at hover_pulse_gallery
        else:
            textbutton "{size=20}SHOW ALL SCENES{/size}":
                text_font "ttf/Comfortaa-Bold.ttf"
                text_color "#aaaaaa"  # Серый когда не активен
                text_hover_color "#00ccff"
                text_outlines [(2, "#000000", 0, 0)]
                background None
                hover_background None
                action ToggleShowAllScenesAction()
                at hover_pulse_gallery

# Replay end screen с вашим шрифтом
screen replay_end_screen():
    tag replay_end
    modal True
    zorder 200

    add Solid("#000000DD")

    vbox:
        xalign 0.5
        yalign 0.4
        spacing 30

        text "REPLAY END":
            size 56
            color "#ffffff"
            bold True
            outlines [(4, "#000000", 0, 0), (2, "#00ccff", 0, 0)]
            font "ttf/Comfortaa-Bold.ttf"
            xalign 0.5

        # REPLAY button - без синей подсветки
        textbutton "REPLAY":
            xalign 0.5
            text_size 32
            text_color "#ffffff"
            text_hover_color "#00ffff"
            text_font "ttf/Comfortaa-Bold.ttf"
            background None
            action [Hide("replay_end_screen"), 
                    SetVariable("is_gallery_replay", True), 
                    Jump(last_replay)]
            at hover_pulse_gallery

        # Return to Gallery button - возвращает в галерею
        textbutton "RETURN TO GALLERY":
            xalign 0.5
            text_size 28
            text_color "#ffffff"
            text_hover_color "#00ffff"
            text_font "ttf/Comfortaa-Bold.ttf"
            background None
            action [Hide("replay_end_screen", dissolve),
                    ShowMenu("gallery")]
            at hover_pulse_gallery

        timer 3.0 action [Hide("replay_end_screen", dissolve),
                         ShowMenu("gallery")]

    text "Auto-return in 3 seconds...":
        size 20
        color "#888888"
        italic True
        font "ttf/Comfortaa-Bold.ttf"
        xalign 0.5
        yalign 0.9

# All replay labels
label replay_prologue:
    $ player_name = persistent.player_name or "Hero"
    $ is_gallery_replay = True
    $ last_replay = "replay_prologue"
    call prolog from _call_prolog_gallery
    $ is_gallery_replay = False
    call screen replay_end_screen
    return

label replay_monica_boobs:
    $ player_name = persistent.player_name or "Hero"
    $ is_gallery_replay = True
    $ last_replay = "replay_monica_boobs"
    call monicaboobs from _call_monicaboobs_gallery
    $ is_gallery_replay = False
    call screen replay_end_screen
    return

label replay_firstjerk:
    $ player_name = persistent.player_name or "Hero"
    $ is_gallery_replay = True
    $ last_replay = "replay_firstjerk"
    call frist_jerk from _call_frist_jerk_gallery
    $ is_gallery_replay = False
    call screen replay_end_screen
    return

label replay_monica_pool:
    $ player_name = persistent.player_name or "Hero"
    $ is_gallery_replay = True
    $ last_replay = "replay_monica_pool"
    call mon_pool from _call_mon_pool_gallery
    $ is_gallery_replay = False
    call screen replay_end_screen
    return

label replay_sara_hj:
    $ player_name = persistent.player_name or "Hero"
    $ is_gallery_replay = True
    $ last_replay = "replay_sara_hj"
    call sara_hj from _call_sara_hj_gallery
    $ is_gallery_replay = False
    call screen replay_end_screen
    return

label replay_bonus1:
    $ player_name = persistent.player_name or "Hero"
    $ is_gallery_replay = True
    $ last_replay = "replay_bonus1"
    call play_bonus_video from _call_play_bonus_video_gallery
    $ is_gallery_replay = False
    call screen replay_end_screen
    return