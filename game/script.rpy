# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image outsideBuilding = "bg/Onsen_Building.png"
image outsideRoom = "bg/Apartment_Exterior.png"
image insideRoom = "bg/Futon_Room.png"
image digitalWorld = "bg/Digital_World.jpeg"

image caedus = "characters/Jim_Caedus.png"
image archyle = "characters/Drew_Archyle.png"
image omega = "characters/Robert_Main.png"
image ollie = "characters/Oliver_Main.png"
image nickles = "characters/Charlie_Nickles.png"
image flynn = "characters/Mark_Flynn.png"
image nkwc = "characters/NKWC.png"

define narrator = Character("Narrator", color="#FFFFFF")
define jim  = Character("Jim Caedus", color="#00BFFF")
define rob = Character("Robert Main", color="#FFA500")
define drew = Character("Drew Archyle", color="#708B8F")
define oliver = Character("Oliver Main", color="#FF0000")
define charlie = Character("Charlie Nickles", color="#008000")
define flynn = Character("Mark Flynn", color="#FFA500")
define nkwc = Character("NK", color="#C3E87D")

style pokemon_who is text:
    size 22
    font "gui/fonts/PKMN RBYGSC.ttf"
    color "#000000"

style pokemon_what is text:
    size 22
    font "gui/fonts/PKMN RBYGSC.ttf"
    color "#000000"

style pokemon_window is window:
    background Frame("gui/pokemon_background.png", 25, 25)
    left_margin 50
    right_margin 50
    bottom_margin 50
    top_padding 20
    left_padding 20

style poke_namebox_window is window:
    background Frame("gui/pokemon_background.png")
    xsize 250
    ysize 50
    xpos 90
    ypos -10
    top_padding 10
    left_padding 45

define poke_narrator = Character("NARRATOR", namebox_style="poke_namebox_window", who_style="pokemon_who", what_style="pokemon_what", window_style="pokemon_window")
define poke_jim  = Character("CAEDUS", namebox_style="poke_namebox_window", who_style="pokemon_who", what_style="pokemon_what", window_style="pokemon_window")
define poke_rob = Character("OMEGA", namebox_style="poke_namebox_window", who_style="pokemon_who", what_style="pokemon_what", window_style="pokemon_window")
define poke_drew = Character("ARCHYLE", namebox_style="poke_namebox_window", who_style="pokemon_who", what_style="pokemon_what", window_style="pokemon_window")
define poke_oliver = Character("OLLIE", namebox_style="poke_namebox_window", who_style="pokemon_who", what_style="pokemon_what", window_style="pokemon_window")
define poke_charlie = Character("NICKLES", namebox_style="poke_namebox_window", who_style="pokemon_who", what_style="pokemon_what", window_style="pokemon_window")

define audio.battle = "audio/music/battle_theme.mp3"
define audio.internet = "audio/music/internet_theme.mp3"
define audio.main = "audio/music/main_theme.mp3"
define audio.spotted = "audio/music/spotted_theme.mp3"

define audio.drew_cry = "audio/sounds/Drew_Cry.mp3"
define audio.jim_cry = "audio/sounds/Jim_Cry.mp3"
define audio.main_cry = "audio/sounds/Main_Cry.mp3"
define audio.ollie_cry = "audio/sounds/Ollie_Cry.mp3"

define audio.collision = "audio/sounds/Collision.mp3"
define audio.faint = "audio/sounds/Faint.wav"
define audio.thud = "audio/sounds/Thud.mp3"

define audio.poof = "audio/sounds/Poof.wav"
define audio.toss = "audio/sounds/Toss.wav"

define audio.run = "audio/sounds/Run.wav"

define sent_main = False
define sent_drew = False
define sent_ollie = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music main

    scene outsideBuilding
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    narrator "Our Story begins at the Senior Living Facility that APEX calls home..."

    scene outsideRoom
    with dissolve

    narrator "APEX! One of the greatest factions in XWF History!"

    narrator "However! They now face their greatest challenge of all!"

    narrator "Internet Trolls!"

    scene insideRoom
    with dissolve

    show caedus

    # These display lines of dialogue.

    jim "Dagnabbit, Dang ol' Trolls!"

    hide caedus

    show archyle

    drew "JIM! BROTHER!"

    drew "I JUST GOT ROBERT TO TAKE A NAP!"

    drew "YOU KNOW HE NEEDS EIGHTEEN HOURS OF SLEEP THESE DAYS!"

    drew "OTHERWISE HE GETS ALL CRANKY!"

    hide archyle

    show omega

    rob "Zzzzzzzzzzzzzzzz"

    rob "The Hunter Hunts, Hunting for the Hunt in a..."

    rob "Zzzzzzzzzzzzzzzz"

    hide omega

    show archyle

    drew "AWWW HE'S CUTTING A PROMO IN HIS SLEEP!"

    drew "AND IT SOUNDS LIKE HIS BEST ONE IN WEEKS!"

    hide archyle

    show ollie

    oliver  "And I'm Ollie!"

    hide ollie

    show caedus

    jim "Dang ol', we ain't gah no time for dagnab napping!"

    jim "Talkinbout, dang ol', APEX's got them dang ol' buzzards circlin'..."

    jim "Dang ol', lookin' for signs 'a weakness, knowwutImean?"

    hide caedus

    show archyle

    drew "YOU ALWAYS KNEW JUST WHAT TO SAY TO WHIP THIS CREW INTO SHAPE, jim !"

    hide archyle

    show omega

    rob "The dreaming dreamer dreams, but dreams dream their own dreams..."

    rob "Dreaming a dream where dreams may dream to dream..."

    hide omega

    show archyle

    drew "YOU STILL GOT IT, MAIN!"

    hide archyle

    show ollie

    oliver  "And I'm Ollie!"

    hide ollie

    show caedus

    jim "Then, it's dang ol' settled, man."

    jim "Talkingbout, we're done being flamed 'n ambushed 'n trolled by the damn..."

    jim "Dang ol' peanut gallery."

    jim "We're takin' th' dang ol' fight to th' only place where fights like 'is get settled..."

    hide caedus

    show archyle

    drew "OF COURSE! THE RING!"

    hide archyle

    show caedus

    jim "..."

    jim "Nah, not the dang ol' ring! Why'd we settle anythin' in the ring, Drew?"

    hide caedus

    show archyle

    drew "I JUST MEANT..."

    hide archyle

    show caedus

    jim "Think with your dang ol' head, Drew!"

    jim "Why would APEX ever WRESTLE, Drew?"

    jim "We don't WRESTLE anymore!"

    jim "'Swhy I challenged Schizz to a boxing match!"

    hide caedus

    show omega

    rob "I haven't been in a wrestling ring willingly since 2018..."

    hide omega

    show ollie

    oliver  "And I'm Ollie!"

    hide ollie

    show caedus

    jim "That's right! We're takin' 'is fight..."

    jim "To the dang ol' internet, knowwutImean!"

    hide caedus

    show digitalWorld
    with pixellate

    play music internet

    show caedus

    jim "We're here! The Dang ol' Internet!"

    jim "Talkinbout 'stime t' do what MEN LIKE US do in this dangol' new-fangled digital age!"

    hide caedus

    show archyle

    drew "BUY PILLS FOR ERECTICLE DYSFUNCTION?"

    hide archyle

    show omega

    rob "DM girls, asking if they're still in high school?"

    hide omega

    show ollie

    oliver  "And I'm Ollie!"

    hide ollie

    show caedus

    jim "Dangol' NO!"

    jim "Talkinbout We defend our dang ol' honor!"

    jim "Look right chere under dang ol HASHTAG XWF..."

    hide caedus

    show nickles

    play music spotted

    narrator "A Wild Charlie Nickles appears!"

    hide nickles

    show caedus

    jim "CHARLIE NICKLES! MY DANG OL' SOCIAL MEDIA NEMESIS!"

    jim "TALKINGBOUT MY MENTAL EQUAL!"

    hide caedus

    show nickles

    charlie "lol fuk u jim"

    hide nickles

    show caedus

    jim "YOU IMPUGN M' HONOR, SIR! AND I DEMAN' SATISFACTION!"

    play music battle

    hide caedus

    $ gui.SetPreference("font", "gui/fonts/Pokemon.ttf")

    show caedus
    with pixellate

    poke_narrator "Trainer Caedus wants to battle!"

label choices:
    poke_jim "Now, Who'my gon' choose as my dang ol' second 'ginst Charlie?"

    menu:
        "Which APEX member shall battle Charlie Nickles?"

        "M'Boy, Main" if not sent_main:
            $ sent_main = True
            jump main

        "M'Boy, Drew" if not sent_drew:
            $ sent_drew = True
            jump drew

        "M'Boy, Ollie" if not sent_ollie:
            $ sent_ollie = True
            jump ollie

        "IT'S UP T' ME NOW!" if sent_main and sent_drew and sent_ollie:
            jump jim

label drew:
    poke_jim "Take 'im out, Drew!"

    hide caedus

    play sound toss
    play sound poof

    poke_narrator "Trainer Caedus sends out..."

    show archyle

    play sound drew_cry

    narrator "ARCHYLE!"

    poke_drew "IT'S AN HONOR TO FIGHT ALONGSIDE YOU, JIM! MY BROTHER!"

    hide archyle

    show nickles

    poke_charlie "lol ur gay"

    hide nickles

    show archyle

    poke_drew "WITNESS MY ATTACK AND TREMBLE, NICKLES!"

    play sound collision

    show archyle
    with vpunch

    poke_narrator "ARCHYLE headbutts his phone so hard he cracks the screen."

    play sound faint
    play sound thud

    hide archyle
    with moveoutbottom

    poke_narrator "ARCHYLE is offline!"

    show caedus

    poke_jim "GAH DAMMIT! DREW!"

    jump choices

label main:
    poke_jim "It's all you, Omega!"

    hide caedus

    play sound toss
    play sound poof

    poke_narrator "Trainer Caedus sends out..."

    show omega

    play sound main_cry

    poke_narrator "OMEGA!"

    poke_narrator "OMEGA builds steam!"

    poke_rob "The Warrior Wages War where Wars Warble."

    poke_rob "But Where War May Warm the Warrior, So Too The Warrior Warms War..."

    hide omega

    show caedus

    poke_jim "HELL YEAH! TALKINBOUT TH' HEAT! GO OFF, 'MEGA!"

    hide caedus

    show omega

    poke_narrator "OMEGA used Tweet!"

    poke_narrator "...But, it failed."

    poke_rob "...It won't let me post."

    hide omega

    show caedus

    poke_jim "Wutchu mean?"

    hide caedus

    show omega

    poke_rob "It says, 'Character Limit Exceeded'."

    hide omega

    show nickles

    poke_charlie "you fukin suk lol"

    hide nickles

    show omega

    poke_rob "***@@RobertTHEOMEGA1 has blocked you on Twitter***"

    hide omega
    with dissolve

    play sound run

    poke_narrator "OMEGA is offline!"

    show caedus

    poke_jim "GAH DAMMIT!"

    jump choices

label ollie:

    poke_jim "Go for it, Ollie!"

    hide caedus

    play sound toss
    play sound poof

    poke_narrator "Trainer Caedus sends out...!"

    show ollie

    play sound ollie_cry

    poke_narrator "OLLIE!"

    poke_oliver "And I'm Oll- *cough*!"

    poke_oliver "I'm Oll- *cough* *wheeze*!"

    poke_narrator "Ollie passed out, choking on his own spit!"

    play sound faint
    play sound thud

    hide ollie
    with moveoutbottom

    poke_narrator "Ollie is offline!"

    show nickles

    poke_charlie "lol wow"

    hide nickles

    show caedus

    poke_jim "Fer fuck's sake, Ollie!"

    jump choices

label jim:
    poke_jim "I GUESS IT'S UP T' ME NOW!"

    poke_jim "BOYS, LEND ME YOUR STRENGTH!"

    poke_drew "WE'RE WITH YOU, JIM, MY BROTHER!"

    poke_ollie "And I'm Ollie!"

    "..."

    "..."

    poke_jim "Okay, well two outta three ain' b-"

    poke_rob "Sorry, I know it's close to deadline, but yeah, me too."

    poke_jim "OKAY GREAT! WITH APEX'S FULL STRENGTH, I CAN'T LOSE!"

    poke_narrator "CAEDUS prepares a special attack!"

    poke_jim "'SOVER FER YOU!"

    poke_charlie "1v1 me m8"

    poke_jim "NOTCHU, NICKLES!"

    poke_jim "I'M TALKING TO COREY SMITH!"

    "..."

    poke_charlie "corey's afk, bruh"

    poke_jim "PERPARE TAH MEETCHUR MAKER, COREY!"

    poke_narrator "CAEDUS unleashes his attack!"

    poke_jim "TWEEEEEEEEET STOOOOOOOOOOOOOORM"

    poke_narrator "CAEDUS drops one reply!"

    poke_narrator "Two replies!"

    poke_narrator "Five replies!"

    poke_jim "TALKINBOUT EVEN FURTHER BEYOOOOOOOOOOOOOND!"

    poke_narrator "TEN REPLIES!"

    poke_narrator "TWENTY REPLIES!"

    poke_narrator "FIFTY REPLIES!"

    poke_jim "DANGOL WITNESS MY UNLIMITED POWER!"

    jump ending

    # This ends the game.

label ending:
    narrator "Meanwhile, back in the real world."

    narrator "*knock knock*"

    narrator "*door opens*"

    nkwc "Annyeonghaseyo, APEX!"

    flynn "FYI: Y'all's door is unlocked."

    flynn "If you're not more careful, someone might just slip in here and take your stu-"

    flynn "...Whoa."

    drew "*bleeding, face covered in glass shards, with a bricked phone embedded in his skull*"

    rob "ZZZZZzzzzzzzz ZZZZZZZZZZzzzzzzzzzzzz"

    ollie "*looking at the ceiling, drowning in his own saliva, like a turkey in the rain*"

    jim "Razza frazza, dangol... *furiously posting on the internet*"

    nkwc "...What happened here?"

    nkwc "Was APEX attacked Mark Flynn?"

    flynn "...No. I think this was... largely self-inflicted."

    nkwc "My word."

    flynn "..."

    nkwc "..."

    flynn "Hey, Jim?"

    jim "Razza frazza, dangol'... Talkinbout #shutyerface..."

    flynn "It looks like you left the tag belts in this fishbowl with your keys."

    flynn "...Mind if we...?"

    jim "Dangol, gonna kick yer ass in real life, ya simp..."

    flynn "I'll take that as a yes. Much obliged."

    nkwc "Gamsa haeyo, Jim Caedus!"

    nkwc "We hope one day you return to your former glory and..."

    nkwc "Um..."

    nkwc "Stop doing this."

    jim "Dangol, I'll show y'all I ain't tah be trifled with..."

    jim "*post sound effect*"

    jim "haha, got 'im"

    narrator "*door closes*"

    nkwc "This message has been brought to you by Wrestlers Against the Internet."

    flynn "The Internet."

    flynn "NOT."

    flynn "EVEN."

    flynn "ONCE."

    return
