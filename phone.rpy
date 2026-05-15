# phone.rpy — ФИНАЛЬНАЯ ВЕРСИЯ С ПЛАВНЫМ ЗАКРЫТИЕМ

default current_phone_owner = "you"
default expecting_thought = False
default pending_thought = None

init python:
    phone_themes = {
        "sara": {
            "name": "Sara",
            "bg_color": "#ffc0cb",
            "header_color": "#ff4081",
            "bubble_me": "#ff4081",
            "contacts": [
                {"name": "Konnor", "gender": "male",
                 "avatar": "gui/avatars/Connor.png", "small_avatar": "gui/avatars/Connor.png",
                 "chat_history": [
                     {"sender": "her", "text": ("Привет, дорогая! Как дорога?"), "media": None},
                     {"sender": "her", "text": "Вы уже приехали?", "media": None},
                     {"sender": "me",   "text": "Привет! Нет, ещё. Остановились в кафе.", "media": None},
                     {"sender": "me",   "text": "Мама ушла заказывать еду. Я сижу одна в машине, думаю чем бы заняться..🫦", "media": None},
                     {"sender": "me",   "text": "Может ты скинешь видео с прошлых выходных, которые ты снял? 😏", "media": None},
                     {"sender": "her", "text": "Ты про то ночное видео, которое нельзя показывать маме? 😈", "media": None},
                     {"sender": "her", "text": "Хорошо, но я тоже хочу фап-контент в обмен. Скинешь свои сиськи? 🍒", "media": None},
                     {"sender": "me", "text": "Сисек Каролины тебе уже не хватает? Ах..ладно, извращенец.", "media": None},
                     {"sender": "me", "text": "Держи", "media": None},
                     {"sender": "me", "text": None, "media": "images/273.webp",
                     "thought_after": [
                          "Что за видео? И почему она просто отправляет своему брату сиськи, будто это её парень?",
                          "У неё же есть влиятельный жених..или нет?",
                      ]},
                     {"sender": "her", "text": "Спасибо, я так скучаю по ним, сис! 💞", "media": None},
                     {"sender": "her", "text": "Держи видео, как обещал. И помни, 🤫", "media": None},
                     {"sender": "her", "text": None,
                      "media": "videos/anim1.png",
                      "is_video": True,
                      "video_file": "videos/anim1.webm",
                      "thought_after": [
                          "Какого черта происходит в этой семье..?!",
                          "Она дрочила брату, чтобы кончить на лицо их мамы?!",
                          "Блять, хорошая идея. Этот Коннор, не такой уж и придурок! Может спросить у него как ему это удалось..",
                          "Ладно…надо быстро переслать это себе.."
                      ]},
                      {"sender": "me", "text": "Спасибо! Теперь будет чем заняться😜", "media": None},
                      {"sender": "me", "text": "Кстати, я надеюсь ты не забыл потом вытереть её лицо? 😳", "media": None},
                      {"sender": "her", "text": "Эмм...я думал ты это сделаешь 🤔", "media": None},
                      {"sender": "me", "text": "Что? Но я же сказала тебе это сделать!😰", "media": None},
                      {"sender": "her", "text": "Расслабься, я пошутил 😊", "media": None},
                      {"sender": "me", "text": "Ты получишь у меня дома за такие шутки!😡 ", "media": None},
                      {"sender": "her", "text": "😘", "media": None},

                 ], "unread":0, "last_msg": "😘", "last_time": "14:32"},
                  {"name": "Dad", "gender": "male",
                 "avatar": "gui/avatars/Dad.png", "small_avatar": "gui/avatars/Dad.png",
                 "chat_history": [
                     {"sender": "her", "text": None, "media": "images/274.webp"},
                     {"sender": "her", "text": "Cмотри, как ты на меня действуешь… хочу прямо сейчас в тебя зайти 🥵💦", "media": None},
                     {"sender": "me",   "text": "ПАП! ТЫ ОХУЕЛ? ЧТО ЭТО?!", "media": None},
                     {"sender": "her",   "text": "Боже мой!", "media": None},
                     {"sender": "her",   "text": "Извини, Сара. Я кажется перепутал чаты..😟", "media": None},
                     {"sender": "me",   "text": "Бывает..😏", "media": None},
                     {"sender": "me",   "text": "Так ты нашел себе новую девушку? Рада за тебя.", "media": None},
                     {"sender": "her", "text": "Ну..несовсем.", "media": None},
                     {"sender": "her", "text": "Может встретимся как-нибудь, сходим в кафе, поговорим?", "media": None},
                     {"sender": "her", "text": "Я очень сильно скучаю по вам..🥹", "media": None},
                     {"sender": "me", "text": "Извини, но мама не разрешает общаться и видеться с тобой.", "media": None},
                     {"sender": "her", "text": "Я знаю… просто иногда так хочется тебя обнять.", "media": None},
                     {"sender": "me", "text": "Ладно, у меня дела, пап. В следующий раз поговорим. Пока!", "media": None},
                     {"sender": "her", "text": "Пока, доченька. Люблю тебя ❤️.", "media": None},

                 ], "unread": 0, "last_msg": "Пока, доченька. Люблю тебя ❤️", "last_time": "14:32"},
                 {"name": "Lily", "gender": "female",
                 "avatar": "gui/avatars/Lily.png", "small_avatar": "gui/avatars/Lily.png",
                 "chat_history": [
                     {"sender": "her", "text": "Привет, Сара!", "media": None},
                      {"sender": "her", "text": "Как там твои беременные будни?🍉  Что-то ты не пишешь в последнее время.", "media": None},
                      {"sender": "me",   "text": "Привеет, Lily❤️", "media": None},
                      {"sender": "me",   "text": "Извини, не было времени.", "media": None},
                      {"sender": "her", "text": "Понимаю, без проблем. Как там с ребенком? Уже пинается?⚽", "media": None},
                      {"sender": "me",   "text": "Пинается еще как! Вчера весь покоя не давал..😭 ", "media": None},
                      {"sender": "her", "text": "Весь в папу!😂", "media": None},
                      {"sender": "her", "text": "Кстати, как он? Чем занимается?", "media": None},
                     {"sender": "me",   "text": "Он...сейчас немного занят 😛", "media": None},
                     {"sender": "me", "text": None, "media": "images/275.webp"},
                     {"sender": "her", "text": "Ох, я даже не знаю кому я больше завидую, ха-ха 😈🫦", "media": None},
                     {"sender": "her", "text": "Ладно, вижу ты занята, не буду отвлекать, кайфуй 😘", "media": None},
                     {"sender": "me", "text": "Спасибо, спишемся позже 😜", "media": None},
                     

                 ], "unread": 0, "last_msg": "Пока, доченька. Люблю тебя ❤️", "last_time": "14:32"},
                 
            ]
        },
        "you": {
            "name": "You",
            "bg_color": "#e3f2fd",
            "header_color": "#0277bd",
            "bubble_me": "#0277bd",
            "contacts": [
                {"name": "Sara", "gender": "female", "avatar": "images/avatar_sara.png", "small_avatar": "images/avatar_sara_small.png",
                 "chat_history": [
                     {"sender": "her", "text": "Привет, милый", "media": None},
                     {"sender": "me",  "text": "Привет, Сара", "media": None},
                     {"sender": "her", "text": None, "media": "images/sara_photo1.jpg"},
                 ], "unread": 3, "last_msg": "фото", "last_time": "14:32"},
            ]
        }
    }

    def get_phone_theme():
        return phone_themes.get(current_phone_owner, phone_themes["you"])
    
    def show_hero_thought(thought):
        if not thought:
            return
        thoughts = thought if isinstance(thought, list) else [thought]
        renpy.show_screen("thought_queue", thoughts=thoughts, index=0)

# ====================== ТРАНСФОРМЫ ======================
transform phone_appear:
    xpos -500 alpha 0.0          # стартует сильно за левым краем
    ease 0.35 xpos 55 alpha 1.0 # плавно приезжает на нужное место (меняй 220 на любое значение)

transform phone_disappear:
    xpos 55 alpha 1.0           # уезжает обратно влево
    ease 0.35 xpos -500 alpha 0.0

transform play_icon_transform:
    zoom 0.75 alpha 0.6
    on hover:
        linear 0.18 zoom 0.85 alpha 0.95
    on idle:
        linear 0.18 zoom 0.75 alpha 0.6

# Трансформ для плавного появления фото/видео
transform scale_in:
    zoom 0.9 alpha 0.0
    linear 0.3 zoom 1.0 alpha 1.0

# Трансформ для плавного закрытия фото/видео
transform scale_out:
    zoom 1.0 alpha 1.0
    linear 0.3 zoom 0.9 alpha 0.0

# Трансформ для появления мыслей
transform thought_appear:
    alpha 0.0
    linear 0.3 alpha 1.0

# Трансформ для закрытия мыслей
transform thought_disappear:
    alpha 1.0
    linear 0.3 alpha 0.0

# Трансформ для круглых аватарок
transform circular_avatar:
    crop_relative True
    crop (0, 0, 1.0, 1.0)
    xysize (60, 60)

transform circular_small_avatar:
    crop_relative True
    crop (0, 0, 1.0, 1.0)
    xysize (38, 38)

# ====================== СТИЛИ И ФРЕЙМЫ ======================
# Закругленные фреймы для разных радиусов
image rounded_frame_small = Frame("gui/rounded_bg.png", 12, 12)
image rounded_frame_medium = Frame("gui/rounded_bg.png", 20, 20)
image rounded_frame_large = Frame("gui/rounded_bg.png", 30, 30)
image rounded_frame_xlarge = Frame("gui/rounded_bg.png", 40, 40)

# Если нет изображений для закругленных фреймов, создаем их программно
init python:
    def create_rounded_rect(width, height, radius, color):
        return Fixed(
            Solid(color, xsize=width, ysize=height),
            xsize=width, ysize=height
        )
    
    # Создаем закругленные фреймы если их нет
    if not renpy.loadable("gui/rounded_bg.png"):
        renpy.image("rounded_frame_small", Frame(Solid("#000000"), 12, 12))
        renpy.image("rounded_frame_medium", Frame(Solid("#000000"), 20, 20))
        renpy.image("rounded_frame_large", Frame(Solid("#000000"), 30, 30))
        renpy.image("rounded_frame_xlarge", Frame(Solid("#000000"), 40, 40))

# ====================== ЭКРАНЫ ======================
screen phone_frame():
    fixed xsize 490 ysize 990:
        # Внешняя рамка телефона с большим скруглением
        add Frame(Solid("#1c1c1c"), 40, 40) xsize 490 ysize 990
        add Frame(Solid("#2a2a2a"), 36, 36) xsize 478 ysize 978 xpos 6 ypos 6
        add Frame(Solid("#000000"), 32, 32) xsize 466 ysize 966 xpos 12 ypos 12
        
        # Закругленный вырез для камеры
        add Frame(Solid("#000000"), 25, 25) xpos 150 ypos 32 xsize 190 ysize 48 alpha 0.92
        
        # Верхняя панель с закруглением внизу
        add Frame(Solid("#ffffff10"), 0, 0, 20, 20) xpos 0 ypos 0 xsize 490 ysize 70 alpha 0.07

# Полноэкранный просмотр фото с плавным закрытием
screen image_viewer(img):
    modal True
    zorder 300
    add "#000000cc"
    $ img_width, img_height = renpy.image_size(img)
    $ screen_width, screen_height = config.screen_width, config.screen_height
    $ scale_x = screen_width / img_width
    $ scale_y = screen_height / img_height
    $ scale = min(scale_x, scale_y)
    $ new_width = int(img_width * scale)
    $ new_height = int(img_height * scale)
    add img:
        size (new_width, new_height)
        xalign 0.5
        yalign 0.5
        at scale_in
    
    # Закругленная кнопка закрытия
    button:
        xalign 0.96 yalign 0.04
        xysize (60, 60)
        background Frame(Solid("#333333"), 30, 30)
        hover_background Frame(Solid("#555555"), 30, 30)
        action [Hide("image_viewer", transition=Dissolve(0.3))]
        text "×":
            size 40
            color "#ffffff"
            hover_color "#ff4444"
            xalign 0.5
            yalign 0.5

    key "mousedown_1" action [Hide("image_viewer", transition=Dissolve(0.3))]
    key "K_ESCAPE" action [Hide("image_viewer", transition=Dissolve(0.3))]

# Полноэкранный просмотр видео с плавным закрытием
screen video_viewer(video):
    modal True
    zorder 300
    add "#000000cc"
    add Movie(play=video, size=(config.screen_width, config.screen_height)) xalign 0.5 yalign 0.5 at scale_in
    
    # Закругленная кнопка закрытия
    button:
        xalign 0.96 yalign 0.04
        xysize (60, 60)
        background Frame(Solid("#333333"), 30, 30)
        hover_background Frame(Solid("#555555"), 30, 30)
        action [Hide("video_viewer", transition=Dissolve(0.3))]
        text "×":
            size 40
            color "#ffffff"
            hover_color "#ff4444"
            xalign 0.5
            yalign 0.5
    
    key "mousedown_1" action [Hide("video_viewer", transition=Dissolve(0.3))]
    key "K_ESCAPE" action [Hide("video_viewer", transition=Dissolve(0.3))]

# Экран для иконки play с анимацией и закруглениями
screen play_icon():
    fixed:
        xsize 80 ysize 80
        xalign 0.5 yalign 0.5
        # Закругленный фон для кнопки play
        add Frame(Solid("#00000080"), 40, 40) xalign 0.5 yalign 0.5 xysize (80, 80)
        
        add ConditionSwitch(
            "renpy.loadable('gui/play_button.png')", "gui/play_button.png",
            "True", Text("▶", size=36, color="#ffffff", bold=True)
        ) xalign 0.5 yalign 0.5 at play_icon_transform

# Экран для показа мыслей с плавным закрытием
screen thought_queue(thoughts, index):
    zorder 500
    modal True
    if index < len(thoughts):
        $ current_thought = thoughts[index]
        frame:
            background Frame(Solid("#000000aa"), 25, 25)
            xalign 0.5
            yalign 0.85
            xmaximum 0.8
            xpadding 40
            ypadding 25
            at thought_appear
            text current_thought:
                size 32
                color "#ffffff"
                bold True
                italic True
                text_align 0.5
                xalign 0.5
        timer 7 action [Hide("thought_queue", transition=Dissolve(0.3)), Show("thought_queue", thoughts=thoughts, index=index+1)]
        key "mousedown_1" action [Hide("thought_queue", transition=Dissolve(0.3)), Show("thought_queue", thoughts=thoughts, index=index+1)]
        key "K_RETURN" action [Hide("thought_queue", transition=Dissolve(0.3)), Show("thought_queue", thoughts=thoughts, index=index+1)]
        key "K_SPACE" action [Hide("thought_queue", transition=Dissolve(0.3)), Show("thought_queue", thoughts=thoughts, index=index+1)]
        key "K_ESCAPE" action [Hide("thought_queue", transition=Dissolve(0.3))]
    else:
        timer 0.01 action [Hide("thought_queue", transition=Dissolve(0.3))]

# Чат — ВСЕ ЭЛЕМЕНТЫ ЗАКРУГЛЕНЫ С ПЛАВНЫМ ЗАКРЫТИЕМ
screen phone_chat(contact_id):
    $ theme = get_phone_theme()
    $ contact = theme["contacts"][contact_id]
    $ theme["contacts"][contact_id]["unread"] = 0

    modal True zorder 200
    fixed:
        at phone_appear
        xsize 490 ysize 990
        xpos 50 ypos (config.screen_height - 990) // 2
        use phone_frame

        timer 0.1 repeat True action If(
            expecting_thought and not renpy.get_screen("video_viewer") and not renpy.get_screen("image_viewer"),
            [SetVariable("expecting_thought", False), Function(show_hero_thought, pending_thought)]
        )

        # Основной фон чата с закругленными углами
        frame xpos 20 ypos 40 xsize 450 ysize 910 background Frame(Solid(theme["bg_color"]), 25, 25):
            vbox xfill True spacing 0:

                # Заголовок с закругленными углами
                frame background Frame(Solid(theme["header_color"]), 25, 25, 0, 0) xfill True ysize 70:
                    hbox spacing 15 xalign 0.5 yalign 0.5:
                        # Круглый аватар
                        add contact["avatar"]:
                            at circular_avatar
                        
                        vbox spacing 2:
                            text contact["name"] size 24 bold True color "#ffffff"
                            text "Online" size 16 color "#e3f2fd"
                        
                        # Закругленная кнопка закрытия
                        button:
                            background Frame(Solid("#ffffff20"), 22, 22)
                            hover_background Frame(Solid("#ffffff40"), 22, 22)
                            xysize (45, 45)
                            action [Return(), With(Dissolve(0.3))]
                            text "×":
                                size 40
                                color "#ffffff"
                                hover_color "#ff4444"
                                xalign 0.5
                                yalign 0.5

                # Область сообщений
                viewport yinitial 0.0 mousewheel True draggable True xfill True ysize 790:
                    vbox spacing 15 xfill True yalign 1.0:
                        null height 15

                        for msg in contact["chat_history"]:

                            if msg["sender"] == "me":
                                hbox xalign 1.0 spacing 8 xmaximum 450:
                                    null width 40

                                    # Текст в закругленном пузыре
                                    if msg.get("text"):
                                        frame background Frame(Solid(theme["bubble_me"]), 20, 20) xpadding 16 ypadding 12:
                                            text msg["text"] color "#ffffff" size 20 bold True

                                    # Медиа в закругленном контейнере
                                    if msg.get("media"):
                                        if msg.get("is_video"):
                                            $ preview_image = msg["media"]
                                            $ img_width, img_height = renpy.image_size(preview_image)
                                            $ max_width = 320
                                            $ scale_factor = min(1.0, max_width / img_width)
                                            $ display_width = int(img_width * scale_factor)
                                            $ display_height = int(img_height * scale_factor)
                                            
                                            frame background Frame(Solid(theme["bubble_me"]), 20, 20) xpadding 0 ypadding 0:
                                                button action [
                                                    SetVariable("expecting_thought", True),
                                                    SetVariable("pending_thought", msg.get("thought_after")),
                                                    Show("video_viewer", video=msg["video_file"])
                                                ] background None:
                                                    fixed:
                                                        xysize (display_width, display_height)
                                                        add preview_image size (display_width, display_height)
                                                        add Solid("#00000060") size (display_width, display_height)
                                                        use play_icon
                                        else:
                                            $ preview_image = msg["media"]
                                            $ img_width, img_height = renpy.image_size(preview_image)
                                            $ max_width = 320
                                            $ scale_factor = min(1.0, max_width / img_width)
                                            $ display_width = int(img_width * scale_factor)
                                            $ display_height = int(img_height * scale_factor)
                                            
                                            frame background Frame(Solid(theme["bubble_me"]), 20, 20) xpadding 0 ypadding 0:
                                                button action [
                                                    SetVariable("expecting_thought", True),
                                                    SetVariable("pending_thought", msg.get("thought_after")),
                                                    Show("image_viewer", img=msg["media"])
                                                ] background None:
                                                    fixed:
                                                        xysize (display_width, display_height)
                                                        add preview_image size (display_width, display_height)

                            else:
                                hbox xalign 0.0 spacing 8 xmaximum 450:
                                    # Круглый маленький аватар
                                    add contact["small_avatar"]:
                                        at circular_small_avatar
                                    
                                    null width 10

                                    # Текст от собеседника в закругленном пузыре
                                    if msg.get("text"):
                                        frame background Frame(Solid("#e5e5ea"), 20, 20) xpadding 16 ypadding 12:
                                            text msg["text"] color "#000000" size 20

                                    # Медиа от собеседника в закругленном контейнере
                                    if msg.get("media"):
                                        if msg.get("is_video"):
                                            $ preview_image = msg["media"]
                                            $ img_width, img_height = renpy.image_size(preview_image)
                                            $ max_width = 320
                                            $ scale_factor = min(1.0, max_width / img_width)
                                            $ display_width = int(img_width * scale_factor)
                                            $ display_height = int(img_height * scale_factor)
                                            
                                            frame background Frame(Solid("#e5e5ea"), 20, 20) xpadding 0 ypadding 0:
                                                button action [
                                                    SetVariable("expecting_thought", True),
                                                    SetVariable("pending_thought", msg.get("thought_after")),
                                                    Show("video_viewer", video=msg["video_file"])
                                                ] background None:
                                                    fixed:
                                                        xysize (display_width, display_height)
                                                        add preview_image size (display_width, display_height)
                                                        add Solid("#00000060") size (display_width, display_height)
                                                        use play_icon
                                        else:
                                            $ preview_image = msg["media"]
                                            $ img_width, img_height = renpy.image_size(preview_image)
                                            $ max_width = 320
                                            $ scale_factor = min(1.0, max_width / img_width)
                                            $ display_width = int(img_width * scale_factor)
                                            $ display_height = int(img_height * scale_factor)
                                            
                                            frame background Frame(Solid("#e5e5ea"), 20, 20) xpadding 0 ypadding 0:
                                                button action [
                                                    SetVariable("expecting_thought", True),
                                                    SetVariable("pending_thought", msg.get("thought_after")),
                                                    Show("image_viewer", img=msg["media"])
                                                ] background None:
                                                    fixed:
                                                        xysize (display_width, display_height)
                                                        add preview_image size (display_width, display_height)

                        null height 20

                # Поле ввода с закругленными углами
                frame background Frame(Solid("#ffffff20"), 0, 0, 25, 25) xfill True ysize 40:
                    text "Напишите сообщение…" color "#ffffff" size 18 xalign 0.5 yalign 0.5

# Главный экран телефона с закругленными элементами и плавным закрытием
screen phone_main():
    $ theme = get_phone_theme()
    
    modal True
    zorder 200
    
    fixed:
        at phone_appear
        xsize 490 ysize 990
        xpos 50 ypos (config.screen_height - 990) // 2
        use phone_frame
        
        # Основной контент с закругленными углами
        frame xpos 20 ypos 40 xsize 450 ysize 910 background Frame(Solid(theme["bg_color"]), 25, 25):
            vbox xfill True spacing 0:
                
                # Заголовок с закругленными верхними углами
                frame background Frame(Solid(theme["header_color"]), 25, 25, 0, 0) xfill True ysize 80:
                    text theme["name"] + " Phone" size 28 bold True color "#ffffff" xalign 0.5 yalign 0.5
                
                # Список контактов
                viewport mousewheel True draggable True xfill True ysize 742:
                    vbox spacing 0 xfill True:
                        for i, contact in enumerate(theme["contacts"]):
                            button:
                                background None
                                xfill True
                                ysize 100
                                action [Return(i), With(Dissolve(0.3))]
                                
                                hbox spacing 15 xalign 0.0 yalign 0.5:
                                    # Круглый аватар в списке контактов
                                    add contact["avatar"]:
                                        crop_relative True
                                        crop (0, 0, 1.0, 1.0)
                                        xysize (70, 70)
                                        xpos 20
                                    
                                    vbox spacing 4 yalign 0.5:
                                        hbox:
                                            text contact["name"] size 24 color "#000000" bold True
                                            if contact["unread"] > 0:
                                                # Закругленный бейдж уведомлений
                                                add Frame(Solid("#ff4444"), 12, 12) xsize 24 ysize 24 xalign 1.0 yalign 0.0
                                                text str(contact["unread"]) size 18 color "#ffffff" bold True xalign 1.0 yalign 0.0
                                        
                                        text contact["last_msg"] size 20 color "#666666" xpos 20
                                    
                                    null width 50
                                    
                                    vbox spacing 2 yalign 0.5 xalign 1.0:
                                        text contact["last_time"] size 18 color "#666666"

# Метки с плавными переходами
label phone():
    show screen phone_main
    $ selected = ui.interact()
    hide screen phone_main with phone_disappear
    if selected is not None:
        call screen phone_chat(selected)
    return

label phone_direct(contact_id):
    call screen phone_chat(contact_id)
    return