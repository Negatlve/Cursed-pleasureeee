## ============================================================
## Кастомные экраны выбора
## ============================================================

screen choice_mila_insert():
    modal True
    zorder 200

    # Левая сторона — безопасный выбор
    imagebutton:
        idle "536.webp"
        hover "536.webp"
        xpos 0
        ypos 0
        xsize 960
        ysize 1080
        action Jump("mila_safe_choice")

    # Правая сторона — рискованный выбор
    imagebutton:
        idle "537.webp"
        hover "537.webp"
        xpos 960
        ypos 0
        xsize 960
        ysize 1080
        action Jump("mila_risky_choice")

    # Текст на левом выборе
    text "Просто кончить":
        xpos 280
        ypos 920
        size 48
        color "#ffffff"
        outlines [(3, "#000000", 0, 0)]

    # Текст на правом выборе
    text "Рискнуть вставить":
        xpos 1250
        ypos 920
        size 48
        color "#ffffff"
        outlines [(3, "#000000", 0, 0)]