#Characters - Important
define n = Character("Narrator")
define mc = Character("Jan Paul")
define officer = Character("Officer Benjamin Chateaurouxette")
#Characters - Suspects
#Case 1
define hugo = Character("Hugo Bernard")
define manon = Character("Manon Dubois")
define cammile = Character("Cammile Russau")
define jullien = Character("Jullien Moreau")

label start:
    n "Septemer 2nd 1945, the day the second world war ended and the day the world thought it would see peace"
    n "But that was not the case, especially in the small city of Saintclairemont where crime has reached a record high"
    n "And that is where you come in"
    n  "A private investigator known through out France for never failing to solve a case"
    n "Detective Jan Paul"
    n "Will you be able to solve the cases here..."
    n "Or will you finally fail due to the criminals of Saintclairemont"

    show text "Detective at 44 Stanley" with dissolve
    pause(2.0)
    hide text with dissolve
    pause(1.0)

    jump opening

label opening:
    n "You arrive at 44 Stanley, the name of the building in which you will be solving your cases"
    n "Rumours have it that the name comes from Winston Stanley, a American detective who solved 44 cases before mysteriously vanishing"
    n "And since then no one has ever tried working here again..."

    "You enter the building"

    officer "Bonjour, vous devez être le nouveau détective M. Jan Paul, enchanté. Je suis l'officier Benjamin"

    mc "I'm sorry I don't speak French"

    officer "Oh my apologies, My name is Officer Benjamin Chateaurouxette, it will be a pleasure working with you"

    mc "Likewise. Now that formalities are done is there any protocol I'm expected to follow? "

    officer "Thank you for asking, It works a bit different here compared to other places. Le criminal are very intellegent and cunning"
    officer "They can manipulate you into believing that they are right and because a random amount of suspects come in with each case it begins very hard to identify"
    officer "You will have to look through the case file and then question them all to hear their side of the story"
    officer "Be vigilant as only one is right and the rest are criminals, one wrong guess and you're head will be cut off faster than the line at the baguette store when I arrive"

    mc "That is very useful information I will remember that"
    mc "Is there any new case"

    officer "You're one eager man. Check on the counter for a file named Case #01 "

    "You approach the counter and see to files"

    menu:
        "What will you pick"
        "Mr.Benjamin baguette story":
            jump extra_1
        "Case #01":
            jump case_1

label extra_1:
    officer "In America there is a popular saying amongst the young enfant"
    officer "In life the only thing you should chase is the bread and not la cherie"
    officer "And the bread I chase everyday.....Is the sweet and lovely baguette"
    officer "But today there was a big problem. My baguette were finished, it felt like finding your wife cheating on you with your best friend"
    officer "I thought to myself, C'est impossible something must be wrong and I was spot on"
    officer "Crumbs on the floor, like a really messy eater. This would definitly lead me to the cause of the issue no?"
    officer "I followed it around my house all the way to my backyard and what I saw......."
    officer "It was....."
    officer "MY BEST FRIEND EATING THEM QUICKLY WHILE SITTING ON MY CHAIR!!!"
    officer "Pourquoi"

    mc "What did I just read, let me focus on the actual case now"
    jump case_1

label case_1:
    show text "The Poisoning of Pierre Dubois" with dissolve
    pause(2.0)
    hide text with dissolve
    pause(1.0)

    n "Pierre os a ,am who lives on Rue d'eglise, a street near the Stanley building"
    n "He is 35 years of age. He was found dead at 4:14pm by his partner, who went out to walk their dog"
    n "She reports he was supposed to be at work, and left around 8:00am"
    n "She left to walk the dog around 3:10pm, so he must have returned and was murdered around that one minute window"
    n "She reports he was very hot to touch when she found him"
    n "He had a very dry mouth and noticeably dilated pupils"
    n "The toxicology report came back, and found Antropine in his system"
    n "A drug that is found in eye drops used to medicate certain things including heart issues"
    n "Mr Dubois has no prescription to the drug and neither did his partner"

    "You decide to check the case file for possible suspects"
    "There are 4 suspects who had the chance to murder him"

    show text "Hugo Benard - Business partner" with dissolve
    pause(1.0)
    "Mrs Dubois reports that Pierre and Hugo did not get along, and were always in competition with each other"
    "He reports he was on his afternoon lunch break"
    hide text with dissolve

    show text "Manon Dubois - Partner" with dissolve
    pause(1.0)
    "Pierre and Manon do not have a prenup, nor are they married"
    "This would mean non of his wealth go to Manon if she murdered him..."
    hide text with dissolve

    show text "Cammile Russau - Neighbour" with dissolve
    pause(1.0)
    "Constant complaints of the Dubois dog barking, constantly called over complaints"
    "Even went as far as to call animal control on the dog. She was home all day"
    hide text with dissolve

    show text "Jullien Moreau - Younger Brother" with dissolve
    pause(1.0)
    "After Pierres's father died the two brothers were given something in the will"
    "Pierre got the house in which he resided in and Julien got the vineyard"
    "Forcing Julien to work there as the terms did not allow him to sell the vineyard"


