## ============================================================
## Кастомные экраны выбора
## ============================================================

screen choice_mila_insert():
    default hover_side = "left"
    default anim_progress = 1.0   # 1.0 = левый фокус, 0.0 = правый

    if hover_side == "left":
        $ target_progress = 1.0
    else:
        $ target_progress = 0.0

    timer 0.02 repeat True action SetScreenVariable(
        "anim_progress",
        anim_progress + (target_progress - anim_progress) * 0.15
    )

    $ left_alpha  = anim_progress
    $ right_alpha = 1.0 - anim_progress

    fixed:
        # Левый фокус (безопасный) – 30% размыто справа
        add Transform(
            Fixed(
                "536.webp",
                Transform("536.webp", blur=8, crop=(0.7, 0.0, 0.3, 1.0), xalign=1.0),
                Solid("#00224422")   # синий оттенок безопасности
            ),
            alpha=left_alpha
        )

        # Правый фокус (рискованный) – 30% размыто слева
        add Transform(
            Fixed(
                "537.webp",
                Transform("537.webp", blur=8, crop=(0.0, 0.0, 0.3, 1.0), xalign=0.0),
                Solid("#44000022")   # красный оттенок риска
            ),
            alpha=right_alpha
        )

        # Тексты (левый вернулся на своё место)
        add Text("Просто кончить", color="#aaccff", size=60):
            xpos 130 ypos 480 alpha left_alpha
        add Text("Рискнуть вставить", color="#ff8888", size=60):
            xpos 1200 ypos 480 alpha right_alpha

        # Кликабельные зоны
        button:
            xsize 0.5 yfill True xalign 0.0
            hovered SetScreenVariable("hover_side", "left")
            action Jump("mila_safe_choice")
        button:
            xsize 0.5 yfill True xalign 1.0
            hovered SetScreenVariable("hover_side", "right")
            action Jump("mila_risky_choice")