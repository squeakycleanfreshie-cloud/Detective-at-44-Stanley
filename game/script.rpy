#Characters - Important
define n = Character("Narrator")
define mc = Character("Jean Paul")
define officer = Character("Officer Benjamin Chateaurouxette")
#Characters - Suspects
#Case 1
define hugo = Character("Hugo Bernard")
define manon = Character("Manon Dubois")
define cammile = Character("Cammile Russau")
define jullien = Character("Jullien Moreau")

image hugo = "images/hugo.png"
image manon = "images/manon.png"
image cammile = "images/cammile.png"
image jullien = "images/jullien.png"

default hugo_asked = set()
default manon_asked = set()
default cammile_asked = set()
default jullien_asked = set()

define config.main_menu_music = "audio/music.mp3"

label start:

    play music "audio/music.mp3" loop
    
    n "Septemer 2nd 1945, the day the second world war ended and the day the world thought it would see peace"
    n "But that was not the case, especially in the small city of Saintclairemont where crime has reached a record high"
    n "And that is where you come in"
    n  "A private investigator known through out France for never failing to solve a case"
    n "Detective Jean Paul"
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

    officer "Bonjour, vous devez être le nouveau détective Mr. Jean Paul, enchanté. Je suis l'officier Benjamin"

    mc "I'm sorry I don't speak French"

    officer "Oh my apologies, My name is Officer Benjamin Chateaurouxette, it will be a pleasure working with you"

    mc "Likewise. Now that formalities are done is there any protocol I'm expected to follow? "

    officer "Thank you for asking, It works a bit different here compared to other places. Le criminal are very intellegent and cunning"
    officer "They can manipulate you into believing that they are right and because a random amount of suspects come in with each case it begins very hard to identify"
    officer "You will have to look through the case file and then question them all to hear their side of the story"
    officer "Be vigilant as only one is right and the rest are criminals, one wrong guess and you're head will be cut off faster than the line at the baguette store when I arrive"

    mc "That is very useful information. I will remember that"
    mc "Are there any new cases for me to take?"

    officer "You're one eager man Jean. Check on the counter for a file named Case One "

    "You approach the counter and see to files"

    menu:
        "What will you pick"
        "Case 1":
            jump case_1
        "Bonus: Officer Benjamin's Baguette Report":
            jump extra_1


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
    officer "Pourquoi????!"

    mc "What did I just read, let me focus on the actual case now"
    jump case_1

label case_1:
    show text "The Poisoning of Pierre Dubois" with dissolve
    pause(2.0)
    hide text with dissolve
    pause(1.0)

    n "Pierre is a man who lives on Rue d'eglise, a street near the Stanley building"
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
    "This would mean none of his wealth go to Manon if she murdered him..."
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

    hide text with dissolve

    $ questioned = set()
    jump suspect_lineup_label

label suspect_lineup_label:
    call screen suspect_lineup


label interrogate_hugo:
    $ questioned.add("hugo")
    if len(hugo_asked) == 0:
        n "You question Hugo."
        n "Hugo wears glasses, and has sweaty forehead"
        mc "Hello Mr.Bernard, how are you today?"
        hugo "I’m ok, thank you. How about you?"
        mc "I’m fine. I have brought you here today to ask a few questions."
        hugo "Okay, fine."
    jump hugo_menu

label hugo_menu:
    if len(hugo_asked) >= 3:
        jump suspect_lineup_label

    $ hugo_asked_left = 3 - len(hugo_asked)

    menu:
        "Pick a question to ask Hugo. ([hugo_asked_left] left)":
            pass

        "Did you notice that Mr Dubois was gone from later than normal on the date of his death?" if "q1" not in hugo_asked:
            $ hugo_asked.add("q1")
            mc "Did you notice that Mr Dubois was gone from later than normal on the date of his death?"
            hugo "Yes. He left at 12:00, I heard him talking to other co-workers, saying he was tired and needed a rest, just him and a glass of wine."

        "Did Mr Dubois normally leave from work early?" if "q2" not in hugo_asked:
            $ hugo_asked.add("q2")
            mc "Did Mr Dubois normally leave from work early?"
            hugo "Yes. I don't beleive that he worked very hard, from my experience as being his colleuge."
            mc "And how long have you known him?"
            hugo "I have been working at Gabriel Enterprise for 3 years now, just when I met Pierre."

        "Did you an Mr Dubois get along well?" if "q3" not in hugo_asked:
            $ hugo_asked.add("q3")
            mc "Did you an Mr Dubois get along well?"
            hugo "If you would like my honest oppinion, well. No not really. Pierre was just very stubborn, and he wouldn't listen to any of my ideas."
            n "Hugo looks away for a moment."

        "Where were you between 3pm and 4pm that day?" if "q4" not in hugo_asked:
            $ hugo_asked.add("q4")
            mc "Where were you between 3pm and 4pm that day?"
            jullien "I was at the vineyard. I had work to finish there, and I did not leave until later that afternoon."
            hugo "I was in the office. Working."
            mc "Can anybody vouch for you?"
            hugo "I beleive in this case, no. There was a staff lunch party that I didn't attend."
            mc "Why not?"
            hugo "I don't like those sort of things. Talking to people who are less inteligent than me bores me."

    jump hugo_menu


label interrogate_manon:
    $ questioned.add("manon")
    if len(manon_asked) == 0:
        n "You question Manon."
    jump manon_menu

label interrogate_manon:
    $ questioned.add("manon")
    hide hugo
    hide cammile
    hide jullien
    if len(manon_asked) == 0:
        show mc at char_left, talker
        show manon at char_right, listener
        n "You question Manon."
        n "Manon has tired eyes, and holds herself very still, hands folded in her lap"
        mc "Hello Mrs. Dubois, thank you for coming in. I know this is difficult."
        show manon at char_right, talker
        show mc at char_left, listener
        manon "Of course. Anything to help find who did this to him."
        show mc at char_left, talker
        show manon at char_right, listener
        mc "I appreciate that. I just have a few questions."
        show manon at char_right, talker
        show mc at char_left, listener
        manon "Go ahead."
    else:
        show mc at char_left, listener
        show manon at char_right, listener
    jump manon_menu

label manon_menu:
    if len(manon_asked) >= 5:
        jump suspect_lineup_label

    $ manon_asked_left = 7 - len(manon_asked)

    menu:
        "Pick a question to ask Manon. ([manon_asked_left] left)":
            pass

        "Where were you between 3pm and 4pm before you left to walk the dog?" if "q1" not in manon_asked:
            $ manon_asked.add("q1")
            show mc at char_left, talker
            show manon at char_right, listener
            mc "Where were you between 3pm and 4pm before you left to walk the dog?"
            show manon at char_right, talker
            show mc at char_left, listener
            manon "I was home, tidying up. Pierre wasn't back from work yet."

        "What time did you actually leave to walk the dog?" if "q2" not in manon_asked:
            $ manon_asked.add("q2")
            show mc at char_left, talker
            show manon at char_right, listener
            mc "What time did you actually leave to walk the dog?"
            show manon at char_right, talker
            show mc at char_left, listener
            manon "Around 3:10, like I told the officer. He gets restless around then, needs his walk."

        "Did Pierre have any prescriptions or medications in the house?" if "q3" not in manon_asked:
            $ manon_asked.add("q3")
            show mc at char_left, talker
            show manon at char_right, listener
            mc "Did Pierre have any prescriptions or medications in the house?"
            show manon at char_right, talker
            show mc at char_left, listener
            manon "No, nothing like that. He was healthy. Careful about that sort of thing, actually."

        "Whose eye drops were in the bathroom? Did you know Hugo well?" if "q4" not in manon_asked:
            $ manon_asked.add("q4")
            show mc at char_left, talker
            show manon at char_right, listener
            mc "Whose eye drops were in the bathroom? Did you know Hugo well?"
            show manon at char_right, talker
            show mc at char_left, listener
            manon "Those must be Hugo's. He stayed with us once, months ago, before things went sour between him and Pierre."
            manon "I don't know him well beyond a few dinners. Pierre handled that friendship, not me."

        "What did Pierre say about him? Was Pierre acting normal that morning before he left for work?" if "q5" not in manon_asked:
            $ manon_asked.add("q5")
            show mc at char_left, talker
            show manon at char_right, listener
            mc "What did Pierre say about him? Was Pierre acting normal that morning before he left for work?"
            show manon at char_right, talker
            show mc at char_left, listener
            manon "Pierre never had a kind word for Hugo lately. Said he couldn't trust him with the business anymore."
            manon "That morning was normal though. Coffee, complaints about work, the usual."

        "Why no prenup or marriage after this long together?" if "q6" not in manon_asked:
            $ manon_asked.add("q6")
            show mc at char_left, talker
            show manon at char_right, listener
            mc "Why no prenup or marriage after this long together?"
            show manon at char_right, talker
            show mc at char_left, listener
            manon "We just never got around to it. Pierre always said there was no rush, that it didn't change how he felt."
            manon "I never pushed. I suppose now I wish I had."

        "Who else had access to the house that day?" if "q7" not in manon_asked:
            $ manon_asked.add("q7")
            show mc at char_left, talker
            show manon at char_right, listener
            mc "Who else had access to the house that day?"
            show manon at char_right, talker
            show mc at char_left, listener
            manon "Just the two of us, really. Cammile has a spare key for emergencies, next door."
            manon "And Julien visits sometimes, though I don't think he has his own key."

    jump manon_menu


label interrogate_cammile:
    $ questioned.add("cammile")
    if len(cammile_asked) == 0:
        n "You question Cammile."
    jump cammile_menu

label cammile_menu:
    if len(cammile_asked) >= 3:
        jump suspect_lineup_label

    $ cammile_asked_left = 3 - len(cammile_asked)

    menu:
        "Pick a question to ask Cammile. ([cammile_asked_left] left)":
            pass

        "You said you were home all day — did you see Pierre come back before 4:14pm?" if "q1" not in cammile_asked:
            $ cammile_asked.add("q1")
            mc "You said you were home all day — did you see Pierre come back before 4:14pm?"
            cammile "No. I did not see him come back. I heard a car around 3:20, but I cannot say who it belonged to."

        "Did you see anyone else visit the house that afternoon?" if "q2" not in cammile_asked:
            $ cammile_asked.add("q2")
            mc "Did you see anyone else visit the house that afternoon?"
            cammile "I saw someone walking towards the Dubois house around 3:25pm. It looked like a man wearing a dark jacket, but I did not see his face."

        "How far is your place from theirs — could you hear or see the front door?" if "q3" not in cammile_asked:
            $ cammile_asked.add("q3")
            mc "How far is your place from theirs — could you hear or see the front door?"
            cammile "We are close enough for me to hear things outside. I can also see part of their front path from my window."

        "Did your complaints about the dog ever turn into direct conflict with Pierre or just Manon?" if "q4" not in cammile_asked:
            $ cammile_asked.add("q4")
            mc "Did your complaints about the dog ever turn into direct conflict with Pierre or just Manon?"
            cammile "I'm reasonable enough to sense that they can't really do anything about a pesky disobediant dog"

        "Do you have any medical background, or access to medication like eye drops/heart drugs?" if "q5" not in cammile_asked:
            $ cammile_asked.add("q5")
            mc "Do you have any medical background, or access to medication like eye drops/heart drugs?"
            cammile "I wanted to be a Docter as a kid but I was born in the wrong city"

    jump cammile_menu


label interrogate_jullien:
    $ questioned.add("jullien")
    if len(jullien_asked) == 0:
        n "You question Jullien."
    jump jullien_menu

label jullien_menu:
    if len(jullien_asked) >= 3:
        jump suspect_lineup_label

    $ jullien_asked_left = 3 - len(jullien_asked)

    menu:
        "Pick a question to ask Jullien. ([jullien_asked_left] left)":
            pass

        "Where were you between 3pm and 4pm that day?" if "q1" not in jullien_asked:
            $ jullien_asked.add("q1")
            mc "Where were you between 3pm and 4pm that day?"
            jullien "I was working in my Vineyard."

        "Have you spoken to Pierre recently about the will or the vineyard?" if "q2" not in jullien_asked:
            $ jullien_asked.add("q2")
            mc "Have you spoken to Pierre recently about the will or the vineyard?"
            jullien "Yes, we spoke about it. I was angry that I could not sell the vineyard, but I never threatened him."

        "Do you blame Pierre for how the inheritance was split?" if "q3" not in jullien_asked:
            $ jullien_asked.add("q3")
            mc "Do you blame Pierre for how the inheritance was split?"
            jullien "I blamed our father more than Pierre. The will was his decision. Pierre did not write it."

        "Did you visit the house that day, or know Pierre's schedule?" if "q4" not in jullien_asked:
            $ jullien_asked.add("q4")
            mc "Did you visit the house that day, or know Pierre's schedule?"
            jullien "No. I did not visit the house. I knew he worked until around noon sometimes, but I did not know when he would return home."

        "Do you have access to any of Pierre's medications, or Manon's?" if "q5" not in jullien_asked:
            $ jullien_asked.add("q5")
            mc "Do you have access to any of Pierre's medications, or Manon's?"
            jullien "No. I have never had access to their medication, and I have never needed it."

    jump jullien_menu


label accusation_screen_label:
    n "You have questioned every suspect."
    n "Now you must decide who murdered Pierre Dubois."

    menu:
        "Who do you accuse?"
        "Hugo Bernard":
            jump accuse_hugo
        "Manon Dubois":
            jump accuse_manon
        "Cammile Russau":
            jump accuse_cammile
        "Jullien Moreau":
            jump accuse_jullien


label accuse_hugo:
    n "You accuse Hugo Bernard of murdering Pierre Dubois."
    mc "The evidence points towards Hugo."
    mc "He knew Pierre, had access to the house, and his eye drops were found in the bathroom."
    mc "Cammile also saw a man going towards the house around 3:25pm."
    mc "Most importantly, Hugo claimed he was in the office between 3pm and 4pm with nobody able to confirm it."
    mc "The atropine came from eye drops, and Hugo had access to them."
    n "The evidence is enough."
    n "Hugo Bernard was the murderer."
    hugo "Wait... How did you figure it out?"
    mc "You knew Pierre's schedule, you had a key to the house, and you had access to the drug that killed him."
    mc "You thought nobody would connect the eye drops to you."
    hugo "..."
    n "Hugo had no answer."
    n "Case #01 Solved."

    show text "Case Solved" with dissolve
    pause(2.0)
    hide text

    return


label accuse_manon:
    n "You accuse Manon Dubois of murdering Pierre Dubois."
    n "But the evidence does not support the accusation."
    mc "Something is wrong with this conclusion."
    n "You failed to identify the murderer."
    n "Case #01 Unsolved."

    show text "Case UnSolved" with dissolve
    pause(2.0)
    hide text

    return


label accuse_cammile:
    n "You accuse Cammile Russau of murdering Pierre Dubois."
    n "But the evidence does not support the accusation."
    mc "She had a reason to dislike the dog, but that does not explain the atropine."
    n "You failed to identify the murderer."
    n "Case #01 Unsolved."

    show text "Case UnSolved" with dissolve
    pause(2.0)
    hide text

    return


label accuse_jullien:
    n "You accuse Jullien Moreau of murdering Pierre Dubois."
    n "But the evidence does not support the accusation."
    mc "He had a motive involving the vineyard, but no access to the drug or the house."
    n "You failed to identify the murderer."
    n "Case #01 Unsolved."

    show text "Case UnSolved" with dissolve
    pause(2.0)
    hide text
    
    return
