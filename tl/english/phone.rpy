# game/tl/english/phone.rpy
# Full English translation for the phone system
# Translation completed: 2025-11-30

translate english python:

    phone_themes = {
        "sara": {
            "name": "Sara",
            "bg_color": "#ffc0cb",
            "header_color": "#ff4081",
            "bubble_me": "#ff4081",
            "contacts": [
                {"name": "Konnor💗", "gender": "male",
                 "avatar": "gui/avatars/Connor.png", "small_avatar": "gui/avatars/Connor.png",
                 "chat_history": [
                     {"sender": "her", "text": "Hey babe! How’s the drive?", "media": None},
                     {"sender": "her", "text": "You guys there yet?", "media": None},
                     {"sender": "me",   "text": "Hey! Not yet. Stopped at a café.", "media": None},
                     {"sender": "me",   "text": "Mom went to order food. I’m alone in the car… thinking what to do..🫦", "media": None},
                     {"sender": "me",   "text": "Maybe send me that video from last weekend? The one you filmed?😏", "media": None},
                     {"sender": "her", "text": "You mean that nighttime video we can’t show Mom😈?", "media": None},
                     {"sender": "her", "text": "Fine, but I want something in return. Send me your tits🍒?", "media": None},
                     {"sender": "me",   "text": "Caroline’s boobs not enough for you anymore? Ugh… fine, perv.", "media": None},
                     {"sender": "me",   "text": "Enjoy😋", "media": None},
                     {"sender": "me",   "text": None, "media": "images/273.webp",
                      "thought_after": [
                          "What the hell is this video? And why is she just sending her brother nudes like he’s her boyfriend?",
                          "She’s supposed to have that rich fiancé… right?",
                      ]},
                     {"sender": "her", "text": "Thanks, I miss them so much, sis💞!", "media": None},
                     {"sender": "her", "text": "Here’s the video as promised. And remember — shhh🤫", "media": None},
                     {"sender": "her", "text": None,
                      "media": "videos/anim1.png",
                      "is_video": True,
                      "video_file": "videos/anim1.webm",
                      "thought_after": [
                          "What the fuck is going on in this family…?!",
                          "She jerked off her brother so he could cum on their mom’s face?!",
                          "Damn… that’s actually a brilliant idea. This Connor guy isn’t such an idiot after all. Maybe I should ask him how he did it…",
                          "Alright… gotta forward this to myself real quick…"
                      ]},
                     {"sender": "me",   "text": "Thanks! Now I’ve got something to keep me busy😜", "media": None},
                     {"sender": "me",   "text": "By the way, you didn’t forget to clean her face afterward, did you😳?", "media": None},
                     {"sender": "her", "text": "Uhh… I thought you were gonna do that🤔", "media": None},
                     {"sender": "me",   "text": "What?! I told you to do it!😰", "media": None},
                     {"sender": "her", "text": "Relax, I’m kidding😊", "media": None},
                     {"sender": "me",   "text": "You’re gonna get it when we get home for jokes like that!😡", "media": None},
                     {"sender": "her", "text": "Love you too😘", "media": None},
                 ], "unread": 0, "last_msg": "😘", "last_time": "14:32"},

                {"name": "Dad", "gender": "male",
                 "avatar": "gui/avatars/Dad.png", "small_avatar": "gui/avatars/Dad.png",
                 "chat_history": [
                     {"sender": "her", "text": None, "media": "images/274.webp"},
                     {"sender": "her", "text": "Look what you do to me… I want you inside me right now", "media": None},
                     {"sender": "me",   "text": "DAD! WHAT THE FUCK IS THIS?!😰", "media": None},
                     {"sender": "her", "text": "Oh my God!", "media": None},
                     {"sender": "her", "text": "Sorry Sarah, wrong chat…😟", "media": None},
                     {"sender": "me",   "text": "Happens…😏", "media": None},
                     {"sender": "me",   "text": "So you found yourself a new girlfriend? Happy for you.", "media": None},
                     {"sender": "her", "text": "Well… not exactly.", "media": None},
                     {"sender": "her", "text": "Maybe we can meet up sometime? Grab coffee, talk?", "media": None},
                     {"sender": "her", "text": "I miss you guys so much…🥹", "media": None},
                     {"sender": "me",   "text": "Sorry, but Mom doesn’t allow us to see or talk to you.", "media": None},
                     {"sender": "her", "text": "I know… I just really want to hug you sometimes.", "media": None},
                     {"sender": "me",   "text": "Gotta go, Dad. Talk later. Bye!", "media": None},
                     {"sender": "her", "text": "Bye, sweetheart. Love you ❤️", "media": None},
                 ], "unread": 0, "last_msg": "Bye, sweetheart. Love you ❤️", "last_time": "14:32"},

                {"name": "Lily", "gender": "female",
                 "avatar": "gui/avatars/Lily.png", "small_avatar": "gui/avatars/Lily.png",
                 "chat_history": [
                     {"sender": "her", "text": "Hey Sarah!", "media": None},
                     {"sender": "her", "text": "How’s pregnant life treating you?🍉 Been quiet lately.", "media": None},
                     {"sender": "me",   "text": "Heeey Lily ❤️", "media": None},
                     {"sender": "me",   "text": "Sorry, been super busy.", "media": None},
                     {"sender": "her", "text": "No worries! How’s the baby? Kicking yet?⚽", "media": None},
                     {"sender": "me",   "text": "Kicking like crazy! Wouldn’t let me sleep last night…😭", "media": None},
                     {"sender": "her", "text": "Takes after his daddy!😂", "media": None},
                     {"sender": "her", "text": "Speaking of — how is he? What’s he up to?", "media": None},
                     {"sender": "me",   "text": "He’s… a little busy right now😛", "media": None},
                     {"sender": "me",   "text": None, "media": "images/275.webp"},
                     {"sender": "her", "text": "Damn, not sure who I’m more jealous of lol😈🫦", "media": None},
                     {"sender": "her", "text": "Alright, I see you’re busy — enjoy!😘", "media": None},
                     {"sender": "me",   "text": "Thanks, talk later😜!", "media": None},
                 ], "unread": 0, "last_msg": "Thanks, talk later😜!", "last_time": "14:32"},
            ]
        },

        "you": {
            "name": "You",
            "bg_color": "#e3f2fd",
            "header_color": "#0277bd",
            "bubble_me": "#0277bd",
            "contacts": [
                {"name": "Sara", "gender": "female",
                 "avatar": "images/avatar_sara.png", "small_avatar": "images/avatar_sara_small.png",
                 "chat_history": [
                     {"sender": "her", "text": "Hey babe", "media": None},
                     {"sender": "me",  "text": "Hey Sarah", "media": None},
                     {"sender": "her", "text": None, "media": "images/sara_photo1.jpg"},
                 ], "unread": 3, "last_msg": "photo", "last_time": "14:32"},
            ]
        }
    }

    # Перевод текстов в интерфейсе телефона
    phone_input_placeholder = "Type a message…"

translate english strings:
    old "Напишите сообщение…"
    new "Type a message…"

    old "Online"
    new "Online"