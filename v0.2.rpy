# v0.2.rpy
# coding: utf-8

default linda_tried_open = False
default linda_tried_kick = False
default linda_body_hover = "none"

label v02_start:
    scene black with fade
    centered "v0.2 — Вторая половина дня"
    pause 1.0
    
    scene 284 with dissolve
    "Ты тихо подходишь к двери ванной на втором этаже."
    "Из-за двери доносится шум воды и тихие стоны."
    
    yth "Она одна... в ванне... беременная, голая, расслабленная."
    yth "Идеальный момент. Только нужно правильно подойти."
    
    jump linda_door_choice

label linda_door_choice:
    scene 285 with dissolve
    
    menu:
        "Что ты сделаешь?"
        
        "Попытаться открыть дверь" if not linda_tried_open:
            $ linda_tried_open = True
            jump linda_try_open
        "Постучать":
            jump linda_knock
        "{bad}Выбить дверь силой" if not linda_tried_kick:
            $ linda_tried_kick = True
            jump linda_kick_door

label linda_try_open:
    scene 286 with dissolve
    "Ты кладешь руку на ручку двери."
    
    scene 287 with dissolve
    "Ты поворачиваешь ручку... но дверь заперта."
    yth "Чёрт. Закрыто. Придётся выбирать другой способ."
    
    jump linda_door_choice

label linda_kick_door:
    scene 288 with dissolve
    "Ты замахиваешься ногой."
    
    scene 289 with dissolve
    "С размаху выбиваешь дверь. Она с грохотом падает на пол."
    
    scene 290 with vpunch
    l "ААААА!!! КАКОГО ХУЯ?!"
    "Линда в шоке прячется за занавеской."
    
    scene 291 with dissolve
    "Ты заходишь и отодвигаешь занавеску."
    
    scene 292 with dissolve
    "Перед тобой стоит голая беременная тётя Линда."
    
    scene 293 with dissolve
    l "Ты... ты совсем ебанутый?! Выйди отсюда немедленно!"
    
    scene 294 with dissolve
    "Ты пытаешься залезть в ванну. Линда пинает тебя ногой в живот."
    
    scene 295 with dissolve
    "Ты падаешь на пол."
    
    scene 296 with fade
    "Ты теряешь сознание."
    
    scene 297 with dissolve
    "Ты приходишь в себя. Перед тобой стоит Моника... и Линда."
    "Моника смотрит на тебя сверху вниз. Её разрез между ног прямо перед твоим лицом."
    
    scene 298 with dissolve
    "Теперь ты отчётливо видишь всё."
    
    scene 299 with dissolve
    l "Этот урод хотел меня изнасиловать! Он вышиб дверь!"
    mo "Ты серьёзно, ублюдок? В моём доме? С моей сестрой?"
    
    yth "Блять... проебался. Надо было по-другому..."
    
    jump linda_door_choice

label linda_knock:
    scene 301 with dissolve
    "Ты стучишь в дверь."
    
    scene 302 with dissolve
    l "Кто там?"
    you "Это я, [player_name]. Тётя Линда, мне срочно в туалет, можно?"
    
    scene 303 with dissolve
    l "Подожди минуту! Я сейчас выйду!"
    
    menu:
        "Что сказать Линде?"
        
        "Попросить её выйти, пока ты ссышь":
            jump linda_comes_out
        "Сказать, что ты подождешь":
            jump linda_comes_out
        "Надавить на жалость":
            jump linda_comes_out

label linda_comes_out:
    scene 304 with dissolve
    "Линда встаёт из ванны и идёт к двери."
    
    scene 305 with dissolve
    "Она открывает замок."
    l "Подожди, я сейчас спрячусь обратно..."
    
    scene 306 with dissolve
    "Она возвращается в ванну."
    
    scene 307 with dissolve
    "Линда заходит одной ногой в воду."
    
    scene 308 with dissolve
    "Ты кладёшь руку на ручку двери."
    
    scene 309 with dissolve
    "Ты поворачиваешь ручку."
    
    scene 310 with dissolve
    "Дверь открывается. За занавеской едва просвечивает голый силуэт Линды."
    
    menu:
        "Что сделать с дверью?"
        
        "Закрыть дверь на замок":
            scene 311 with dissolve
            "Ты тянешься к замку."
            scene 312 with dissolve
            "Ты закрываешь дверь на замок."
            $ persistent.linda_door_locked = True
            jump linda_bath_main
        "{sexy}Оставить дверь открытой":
            jump linda_bath_main

label linda_bath_main:
    scene 313 with dissolve
    "Ты подходишь к унитазу и начинаешь ссать."
    you "Знаешь, тётя Линда... я видел видео с Сарой и Коннором."
    you "Твоя дочь трахается со своим родным братом."
    
    scene 314 with dissolve
    "Линда резко отодвигает занавеску."
    l "Что... что ты сказал?!"
    "Она смотрит вниз и видит твой член. Её взгляд застывает."
    
    scene 315 with dissolve
    you "Да. И я знаю всё. Если хочешь, чтобы это осталось между нами... ты сделаешь то, что я скажу."
    
    scene 316 with dissolve
    "Линда смотрит на тебя с ненавистью."
    
    scene 317 with dissolve
    "Она замечает твой член и уставилась на него."
    
    scene 318 with dissolve
    "Её мысли явно не о шантаже."
    
    scene 319 with dissolve
    l "Что... что тебе нужно за молчание?"
    
    scene 320 with dissolve
    you "Выбирай."
    l "Ты... ты серьёзно? Нет. Я не буду этого делать!"
    
    scene 321 with dissolve
    "Ты делаешь вид, что уходишь."
    you "Ладно, тогда я пойду расскажу Монике..."
    
    scene 322 with dissolve
    "Ты идёшь в сторону выхода."
    
    scene 323 with dissolve
    l "Стой! Подожди..."
    "План сработал."
    
    scene 324 with dissolve
    "Линда лежит в ванне и смотрит на тебя с недовольным взглядом."
    l "Говори уже. Что тебе от меня надо?"
    
    scene 325 with dissolve
    you "Выбирай."
    
    $ linda_body_hover = "none"
    call screen linda_body_selection


label linda_handjob:
    scene 327 with dissolve
    "Линда неохотно берёт твой член в руку."
    l "Я ненавижу тебя..."
    "Она начинает медленно дрочить тебе."
    "Ты кончаешь ей на грудь."
    jump v02_end

label linda_footjob:
    scene 328 with dissolve
    "Линда поднимает ноги из воды и зажимает твой член ступнями."
    "Она дрочит тебе ногами, пока ты не кончаешь ей на живот."
    jump v02_end

label linda_boobjob:
    scene 329 with dissolve
    "Линда встаёт на колени в ванне и сжимает твой член между своих больших сисек."
    "Она дрочит тебе сиськами, пока ты не кончаешь ей в лицо."
    jump v02_end

label v02_end:
    scene black with fade
    centered "Сцена v0.2 завершена (заглушка)."
    centered "Галерея разблокирована."
    pause 2.0
    return

label v02_bad_end:
    scene black with fade
    centered "Ты облажался. Эта концовка пока не дописана."
    return