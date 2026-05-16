# v0.2.rpy
# coding: utf-8

default linda_tried_open = False
default linda_tried_kick = False
default linda_body_hover = "none"

image anim84 = Movie(play="videos/anim84.webm", loop=False)
image anim85 = Movie(play="videos/anim85.webm", loop=True)
image anim86 = Movie(play="videos/anim86.webm", loop=True)
image anim87 = Movie(play="videos/anim87.webm", loop=True)
image anim88 = Movie(play="videos/anim88.webm", loop=True)
image anim89 = Movie(play="videos/anim89.webm", loop=False)
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
    
    scene 287 with vpunch
    "Ты поворачиваешь ручку... но дверь заперта."
    yth "Чёрт. Закрыто. Придётся выбирать другой способ."
    
    jump linda_door_choice
label linda_kick_door:
    scene 288 with dissolve
    "Ты замахиваешься ногой."
    show anim84 at fullscreen
    $renpy.pause(1.375)
    scene 289 
    "С размаху выбиваешь дверь. Она с грохотом падает на пол."
    
    scene 290 with vpunch
    l "Эй, какого хуя?!"
    l "Ты что, совсем ебанутый?! Что ты делаешь?!"
    
    you "Расслабься, тётя Линда. Это всего лишь я. Не нужно так орать... Я просто решил, что тебе не помешает компания."
    l "Выйди немедленно отсюда!"
    
    scene 291 with dissolve
    "Ты подходишь ближе к занавеске и кладешь руку на ткань."
    you "Тихо. Если будешь орать — только хуже сделаешь. Давай без истерик, ладно? Я просто хочу тебя."
    l "Ты больной? Это я, твоя тётя! Как ты можешь даже думать об этом?!"
    
    scene 292 with dissolve
    "Занавеска резко отодвигается. Линда сидит в ванне, выставив руку вперёд, пытаясь остановить тебя."
    l "Нет! Не подходи! Убирайся отсюда!"
    you "Не надо делать вид. Я вижу, как ты на меня смотришь."
    
    scene 293 with dissolve
    "Ты закидываешь одну ногу в ванну, пытаясь залезть."
    you "Подвинься немного. Места хватит... будет тесно, но мне нравится тесно."
    l "Нет! Убери ногу! Я тебя предупреждаю!"
    l "Ещё на сантиметр ближе ко мне и я убью тебя!"
    you "Да ладно теб..."
    
    scene 294 with dissolve
    l "Получи!"    
    "Линда резко бьёт тебя ногой в живот."
    
    scene 295 with dissolve
    "Ты теряешь равновесие и падаешь назад на пол."
    you "Ааааа! Бляяять!!"
    l "Я сказала нет, ублюдок!"
    
    scene 296 with fade
    "Ты лежишь на полу без сознания. Линда тяжело дышит, всё ещё в шоке."
    l "Чёрт... чёрт... Эй! Ты меня слышишь? Очнись! Не смей здесь умирать, идиот..."
    
    scene 297 with dissolve
    "Ты медленно приходишь в себя. Всё размыто. Прямо над тобой стоит какая-то женщина. Ты видишь только глубокий разрез между её ягодицами."
    mo "Очнись уже, придурок. Что за хуйню ты тут устроил?"
    you "Ухх... Что это за вид... Ммм, чьи это булки надо мной? Моника? Ты стоишь прямо над моим лицом..."
    
    scene 298 with dissolve
    "Зрение постепенно проясняется."
    scene 299 with dissolve
    l "Этот урод хотел меня изнасиловать! Вышиб дверь и полез ко мне в ванну!"
    mo "Ты серьёзно, ублюдок? В моём доме? С моей сестрой? Ты совсем ебанутый на голову?!"
    
    yth "Чёрт...может надо было быть чуть по-легче.."
    
    jump linda_door_choice


label linda_knock:
    scene 301 with dissolve
    "Ты стучишь в дверь."

    scene 302 with dissolve
    l "Кто там?"

    you "Это я, [player_name]. Тётя Линда, мне срочно нужно в туалет."

    scene 303 with dissolve
    l "Подожди минуту, я сейчас выйду!"

    menu:
        "Что сказать?"

        "Обычный":
            jump linda_knock_normal

        "С шуткой":
            jump linda_knock_funny

        "Грубоватый":
            jump linda_knock_rude

# ============================================
# ВАРИАНТ 1 — Обычный
# ============================================
label linda_knock_normal:
    you "Тётя Линда, мне правда очень нужно. Можно я быстро зайду?"

    l "Я же в ванне... Подожди, я сейчас вылезу."

    you "Я не буду смотреть, честно. Просто мне уже совсем туго."

    l "Ладно... сейчас открою. Только быстро, хорошо?"

    jump linda_knock_she_opens

# ============================================
# ВАРИАНТ 2 — С шуткой + шантаж
# ============================================
label linda_knock_funny:
    you "Тётя Линда, подумай о семейных ценностях. Ты же не хочешь, чтобы твой племянник описался прямо у тебя под дверью?"

    l "Серьезно? Ты меня сейчас шантажируешь?"

    you "Немного. Но если честно — я уже реально не могу терпеть. Открывай, пока не стало ещё хуже."

    l "Боже... ладно. Сейчас открою. Только быстро, ясно?"

    jump linda_knock_she_opens

# ============================================
# ВАРИАНТ 3 — Грубоватый
# ============================================
label linda_knock_rude:
    you "Тётя Линда, мне пиздец как нужно. Открывай, пока я не обосрался у тебя под дверью."

    l "Ты серьёзно это сказал?"

    you "Серьёзно. Открывай."

    l "Боже... ладно, сейчас открою. И не думай пялиться на меня."

    jump linda_knock_she_opens

# ============================================
# Общий лейбл — Линда открывает дверь
# ============================================
label linda_knock_she_opens:
    scene 304 with dissolve
    l "Сейчас... только не входи сразу, ладно?"

    you "Хорошо."

    scene 305 with dissolve
    l "Я сейчас вернусь в ванну. Подожди секунду..."

    scene 306 with dissolve
    "Ты слышшь, как она быстро идёт обратно к ванне."

    scene 307 with dissolve
    l "Можешь уже заходить... но быстро и без глупостей."

    scene 308 with dissolve
    you "Понял."

    scene 309 with dissolve
    "Ты открываешь дверь."

    scene 310 with dissolve
    "За занавеской виднеется её голый силуэт."

    menu:
        "Что сделать с дверью?"

        "Закрыть на замок":
            scene 311 with dissolve
            "Ты тихо закрываешь дверь на замок."
            $ persistent.linda_door_locked = True
            jump linda_bath_main

        "{sexy} Оставить открытой":
            jump linda_bath_main

label linda_bath_main:
    scene 313 with dissolve

    you "Знаешь, тётя Линда... я тут подумал."

    l "О чём?"

    you "О том, от кого ты беременна."

    scene 314 with dissolve

    l "Что ты имеешь в виду?"

    you "Я знаю, от кого у тебя ребёнок, тётя."

    you "И знаю, от кого беременна Сара."

    scene 315 with dissolve

    you "Обе вы беременны от Коннора."

    you "От твоего сына."

    you "От её родного брата."

    l "Ты... ты с ума сошёл."

    scene 316 with dissolve

    you "У меня есть видео."

    you "Где Сара дрочит Коннору."

    you "А потом он подходит к тебе и кончает тебе спящей на лицо."

    l "Ты... ты больной ублюдок. Откуда у тебя это?!"

    scene 317 with dissolve

    you "Если я выложу это в интернет..."

    you "То увидят очень многие."

    you "Твои знакомые. Соседи. Коллеги. Боб."

    scene 318 with dissolve

    l "Не смей... не смей этого делать."

    scene 319 with dissolve

    l "Что... что тебе нужно?"

    scene 320 with dissolve

    you "Теперь ты слушаешь. Хорошо."

    you "Я могу уничтожить это видео."

    you "Могу сделать так, чтобы его никто никогда не увидит."

    you "Но за это ты будешь делать то, что я скажу."

    l "Ты... ты серьёзно? Я беременна! Я твоя тётя!"

    you "Именно поэтому ты и будешь послушной."

    you "Потому что если это видео выложат в интернет..."

    you "Твоя жизнь закончится. Публично и позорно."

    l "Ахах... хорошая попытка, ублюдок. Но нет. Иди нахуй отсюда."

    scene 321 with dissolve

    you "Как скажешь."

    you "Только учти: если я сейчас уйду, то к вечеру это видео уже будет в открытом доступе."

    scene 322 with dissolve

    yth "3... 2... 1..."
    l "Ладно, стой!"
    scene 323 with dissolve

    l "Вернись."
    yth "Сработало."

    scene 324 with dissolve

    l "Ну и что ты хочешь, маленький ублюдок?"

    scene 325 with dissolve

    you "Хм... пока не решил. Дай подумать..."
   

    scene 326 with dissolve
    l "У меня не так много времени, как у тебя, фрик. Думай быстрее, пока я не передумала."
   
    $ linda_body_hover = "none"
    call screen linda_body_selection


label linda_handjob:
    scene 330 with dissolve

    you "Хочу, чтобы рука моей тёти подрочила мне. Прямо сейчас."

    l "Ты... ты реально больной. Как у тебя вообще такое в голове помещается?"

    scene 331 with dissolve

    you "А ты ещё не видела, что у меня в трусах помещается."
    you "Аа... хотя нет, видела только что. Ну не важно."

    scene 332 with dissolve

    you "Красивый, правда? Сейчас твоя очередь с ним поработать."

    scene 333 with dissolve

    l "Ты серьёзно хочешь, чтобы я это сделала?"

    scene 334 with dissolve
    you "Да"
    you "Но для начала убери руку. Хочу видеть обе груди. Полностью."
    lth "Это отвратительно... Он стоит передо мной с этим огромным членом и улыбается. Я его ненавижу."
    scene 335 with dissolve

    l "Доволен? Или ещё что-то придумаешь, чтобы меня унизить?"

    scene 336 with dissolve

    you "Бери в руку и начинай двигать. Я уверен, ты уже знаешь, как это делать."

    scene 337 with dissolve

    l "Ох, конечно. Я же каждый день дрочу своему племяннику, как же я могу не знать."

    scene 339 with dissolve

    l "Ты глубоко ошибаешься, если думаешь, что это тебе так просто с рук сойдёт."

    you "Как раз твоими руками я и собираюсь пользоваться. Приступай, тетя"
    l "..урод"
    

    show screen handjob_anim85
    show screen handjob_controls

    you "Вот так... не останавливайся."
    l "Заткнись..."

    you "Сильнее. Не расслабляйся."

    $ handjob_seen.add("85")
    $ current_handjob_anim = "85"
    pause
    


label view_anim86:
    hide screen handjob_anim85
    hide screen handjob_anim86
    hide screen handjob_anim87
    hide screen handjob_anim88

    show screen handjob_anim86
    show screen handjob_controls

    you "Хороший вид... продолжай."
    l "Не разговаривай со мной."

    you "Тогда просто дрочи"
    you "Теперь возьми его в обе руки"
    l "..."


    $ handjob_seen.add("86")
    $ current_handjob_anim = "86"
    pause
    


label view_anim87:
    hide screen handjob_anim85
    hide screen handjob_anim86
    hide screen handjob_anim87
    hide screen handjob_anim88

    show screen handjob_anim87
    show screen handjob_controls

    you "Так намного лучше... Молодец, тётя."
    l "Заткнись..."
    
    you "Если тебе будет легче — можешь представить, что ты дрочишь не мне, а Коннору."

    l "Иди нахуй. И никогда больше не говори про него."
   

    $ handjob_seen.add("87")
    $ current_handjob_anim = "87"
    pause
    


label view_anim88:
    hide screen handjob_anim85
    hide screen handjob_anim86
    hide screen handjob_anim87
    hide screen handjob_anim88

    show screen handjob_anim88
    show screen handjob_controls

    you "Продолжай. Уже не так сильно морщишься, как в начале."
    l "Я тебя презираю..."
    you "Вижу. Но руки почему-то всё равно работают. Продолжай."
    l "..."
    l "Скоро уже?"
    you "Очень скоро."
    l "Только предупреди, я не хочу, чтобы ты....."
    $ handjob_seen.add("88")
    $ current_handjob_anim = "88"
    pause
    


label handjob_cum:
    hide screen handjob_controls
    hide screen handjob_anim85
    hide screen handjob_anim86
    hide screen handjob_anim87
    hide screen handjob_anim88

    show screen handjob_anim89
    pause
    hide screen handjob_anim89
    scene 347
    you "Оооо, это было охуенно."
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