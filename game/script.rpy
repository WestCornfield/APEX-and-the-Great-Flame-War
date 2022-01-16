# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image outsideBuilding = "bg/Onsen_Building.png"
image outsideRoom = "bg/Apartment_Exterior.png"
image insideRoom = "bg/Futon_Room.png"
image Digital_World = "bg/Digital_World.jpeg"

image caedus = "characters/Jim_Caedus.png"
image archyle = "characters/Drew_Archyle.png"
image omega = "characters/Robert_Main.png"
image ollie = "characters/Oliver_Main.png"

define n = Character("Narrator", color="#000000")
define j = Character("Jim Caedus", color="#00BFFF")
define r = Character("Robert Main", color="#FFA500")
define d = Character("Drew Archyle", color="#708B8F")
define o = Character("Oliver Main", color="#FF0000")

define audio.main = "main_theme.mp3"
define audio.battle = "battle_theme.mp3"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music main

    scene outsideBuilding

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    n "Our Story begins at the Senior Living Facility Where APEX resides..."

    scene outsideRoom

    n "APEX! One of the greatest factions in XWF History!"

    n "However! They now face their greatest challenge of all!"

    n "Internet Trolls!"

    scene insideRoom

    show caedus

    # These display lines of dialogue.

    j "Dagnabbit, Dang ol' Trolls!"

    hide caedus

    show archyle

    d "JIM! BROTHER!"

    d "I JUST GOT ROBERT TO TAKE A NAP!"

    d "YOU KNOW HE NEEDS EIGHTEEN HOURS OF SLEEP THESE DAYS!"

    d "OTHERWISE HE GETS ALL CRANKY!"

    hide archyle

    show omega

    r "Zzzzzzzzzzzzzzzz"

    r "The Hunter Hunts, Hunting for the Hunt in a..."

    r "Zzzzzzzzzzzzzzzz"

    hide omega

    show archyle

    d "AWWW HE'S CUTTING A PROMO IN HIS SLEEP!"

    d "AND IT SOUNDS LIKE HIS BEST ONE IN WEEKS!"

    hide archyle

    show ollie

    o "And I'm Ollie!"

    hide ollie

    show caedus

    j "Dang ol', we ain't gah no dagnab time for napping!"

    j "Talkinbout, dang ol', APEX's got them dang ol' buzzards circlin'..."

    j "Dang ol', lookin' for signs 'a weakness, knowwutImean?"

    hide caedus

    show archyle

    d "YOU ALWAYS KNEW JUST WHAT TO SAY TO WHIP THIS CREW INTO SHAPE, JIM!"

    hide archyle

    show omega

    r "The dreaming dreamer dreams, but dreams dream their own dreams"

    r "Dreaming a dream where dreams may dream to dream"

    hide omega

    show archyle

    d "YOU SAID IT, MAIN! YOU STILL GOT IT!"

    hide archyle

    show ollie

    o "And I'm Ollie!"

    hide ollie

    show caedus

    j "Then, it's dang ol' settled, man."

    j "Talkingbout, we're done being flamed 'n ambushed 'n trolled by the damn..."

    j "Dang ol' peanut gallery."

    j "We're takin' th' dang ol' fight to th' only place where fights like 'is get settled..."

    hide caedus

    show archyle

    d "OF COURSE! THE RING!"

    hide archyle

    show caedus

    j "Nah, not the dang ol' ring! Why'd we settle anythin' in the ring, Drew?"

    hide caedus

    show archyle

    d "I JUST MEANT..."

    hide archyle

    show caedus

    j "Think with your dang ol' head, Drew!"

    hide caedus

    show omega

    r "***@RobertTHEOMEGA1 has blocked you on Twitter***"

    hide omega

    show ollie

    o "And I'm Ollie!"

    hide ollie

    show caedus

    j "That's right! We're takin' 'is fight..."

    j "To the dang ol' internet, knowwutImean!"

    # This ends the game.

    return
