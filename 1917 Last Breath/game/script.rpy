# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define S = Character('Soldat', color="#0000ff")
define S1 = Character('Soldat 1', color="#0000ff")
define S2 = Character('Soldat 2', color="#0000ff")
define C = Character('Commandant', color="#0000ff")
define SA = Character('Soldat Allemand', color="#ff0000")
default povName = ""
define POV = Character ("[povName] (You)", color ="#32f5ff")
default clock = 0
default isFirstIteration = True
define lostAudition = False
define foodInventory = False
define foodIsRat = False
define hadExplosif = False

define MASK = Character('Mask', color="#ff0000")

default K_isVisite = False

#Pour la santé mentale:
default sanity = 0
default SANITY_MIN = -100
default SANITY_MAX = 100

default isFirstIterationA = True
default isFirstIterationB = True
default isFirstIterationC = True
default isFirstIterationD = True
default isFirstIterationE = True
default isFirstIterationF = True
default isFirstIterationG = True
default isFirstIterationH = True
default isFirstIterationI = True
default isFirstIterationJ = True
default isFirstIterationK = True
default isFirstIterationL = True
default isFirstIterationM = True
default isFirstIterationN = True
default isFirstIterationO = True
default isFirstIterationP = True
 
default previous = ""    

image bg AMMO = "images/ammo.png"
image bg ARTY = "images/arty.png"
image bg ARTY_SIDE = "images/artySide.png"
image bg BEDS = "images/beds.png"
image bg CMDT = "images/cmdt.png"
image bg FOOD = "images/food.png"
image bg FOOD_RATS = "images/foodRats.png"
image FRENCH = "images/french.png"
image bg FRONT = "images/front.png"
image GAZ_MASK = "images/gazMask.png"
image GERMANS = "images/germans.png"
image bg SURVIVOR = "images/survivor.png"
image bg SURVIVOR_CHILL = "images/survivorChill.png"
image bg SURVIVOR_CHILL_DEAD = "images/survivorChillDead.png"
image bg SURVIVOR_CHILL_DEAD_RATS = "images/survivorChillDeadRats.png"
image bg SURVIVOR_FIRE = "images/survivorFire.png"
image bg TRENCH_T_RIGHT_BARDED = "images/TrenchTRightBarded.png"
image bg TRENCH_L = "images/TrenchL.png"
image bg TRENCH_L_BARDED = "images/TrenchLBarded.png"
image bg TRENCH_L_BARDED_RIGHT = "images/TrenchLBardedRight.png"
image bg TRENCH_L_BARDED_RIGHT_FLIP = "images/TrenchLBardedRightFlip.png"
image bg TRENCH_L_FLIP = "images/TrenchLFlip.png"
image bg TRENCH_T = "images/TrenchT.png"
image bg TRENCH_T_LEFT = "images/TrenchTLeft.png"
image bg TRENCH_T_LEFT_BARDED = "images/TrenchTLeftBarded.png"
image bg TRENCH_T_RIGHT = "images/TrenchTRight.png"
image bg TRENCH_X = "images/TrenchX.png"
image bg TRENCH_X_FLIP = "images/TrenchXFliped.png"
image bg TRENCH_Y = "images/TrenchY.png"



label start:
# Le jeu commence ici

    "Vous vous réveillez brusquement."
    "Vous avez du mal à vous souvenir de ces derniers moments."
    "Mais certains vous reviennent en mémoire."

    # cutscene du passé
    "Vous discutiez tranquillement avec vos camarades."
    "Vos frères d'armes."
    

    # arrivé d'un perso pour donner l'occasion au joueur de donner son nom
    "..."
    "..."
    "Vous voyez le commandant s'approcher de vous."
    C "Soldat, quel est votre mission ?"
    $ txtVar = ""
    $ missionEntrer = renpy.input(txtVar, length=150)
    
    if missionEntrer == "":
        C "Votre objectif de vie est d'être un incompétant à ce que je vois..."
        C "Jamais vu un soldat aussi inutile!"
        C "Soyez au moins aussi utile qu'une larve et présentez vous soldat!"
        $ povName = renpy.input("Quel est votre nom?")
        $ povName = povName.strip()
        C "Votre nom est tout aussi insignifiant que votre objectif de vie..."
        C "Vous serez une simple larve soldat dans mes rangs!"
        $ povName = "soldat"

    if len(missionEntrer) >= 50:
        C "Votre mission est bien trop longue pour que je puisse la retenir"
        C "Vous êtes belle et bien aussi insignifiant qu'une mouche sur mon uniforme"
        C "..."
        C "Mais je peux faire une exeption en ayant votre nom ..."
        C "Présentez vous soldat!"
        $ povName = renpy.input("Quel est votre nom?")
        $ povName = povName.strip()
        C "Votre nom est tout aussi insignifiant que votre mission..."
        C "Vous serez une simple larve dans mes rangs soldat!"
        $ povName = "soldat"

    if len(missionEntrer) < 50 and missionEntrer != "":
        C "Ah enfin un soldat qui sait se présenter correctement!"
        C "Votre mission n'est cependant aussi utile qu'un cure-dent dans une tranchée..."
        C "..."
        C "Soldat, en vu de votre présentation, votre existence a le mérite d'exister,"
        C "Présentez-vous !"
        $ povName = renpy.input("Quel est votre nom?")
        $ povName = povName.strip()
        C "Bien, soldat [povName],"
        C "Votre nom est tout aussi insignifiant que votre mission..."
        C "Vous serez une simple larve dans mes rangs soldat!"
        $ povName = "soldat"
    jump game

label retry:
    
    jump game
label game:
    show bg TRENCH_L_FLIP
    with fade
    show GAZ_MASK at center

    "La tranchée se divise en plusieurs directions..."
    "Où allons nous ?"

    # CHOIX DROITE OU GAUCHE
menu:
    "NORD":
        jump L 
    "EST": 
        jump O
    
label A: #Arty
    scene bg ARTY 
    with fade
    show GAS_MASK
    
    define accessA_to_B = False
    if previous == "F" and isFirstIterationA:
        "Vous arrivez devant une sorte de porte"
        "Vous remarquez qu'il s'agie d'un bunker d'artillerie moyenne"
        "..."
        "Deux soldats sont à l'entrée de l'artillerie" 
        "et un à l'intérieur en train de sctruter l'horizon."
        S1 "Bonjour Soldat! Que me vaut votre visite ?"
        $isFirstIterationA = False
        jump ChoiceA1
    
    "Vous rentrer dans le poste d'artillerie."
    
    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."

    if sanity < SANITY_MIN:
        if lostAudition == False:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            S "Soldat! Est-ce que sa va ? Vous m'entendez ?"
            "Vous observez alors sans comprendre votre commandant:"
            C "Ressaisissez-vous soldat! Les Bochs sont là!"
            "À ces mots," 
            "vous vous rendez compte que des soldats commencent à
            prendre d'assaut l'artillerie."
            "Pris de panique, vous vous saisissez de votre arme..."
            "..."
            "Un coup de feu retentit ..."
            "..."
            C "Est-ce que sa va soldat?!"
            "..."
            "À ces mots, vous prenez conscience de votre erreur ..."
            "Une balle vous a transpercé le ventre de part en part,"
            "Vous saignez abondamment ..."
            "..."
            jump ENDING05
        if lostAudition == True:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            S "..."
            "Vous observez alors sans comprendre votre commandant:"
            C "..."
            "À ces mots, que vous devinez sur les lèvres de votre commandant," 
            "vous vous rendez compte que des soldats commencent à
            prendre d'assaut l'artillerie."
            "Pris de panique, vous vous saisissez de votre arme..."
            "..."
            "Un coup de feu retentit ..."
            "..."
            C "..."
            "..."
            "À ces mots que vous semblez avoir deviné," 
            "vous prenez conscience de votre erreur ..."
            "Une balle vous a transpercé le ventre de part en part,"
            "Vous saignez abondamment ..."
            "..."
            jump ENDING05
    if sanity > SANITY_MAX:
        if lostAudition == False:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition == True:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les sensations de vos pas retentissent fortement autour de vous."
            "..."
            "Dû à la perte de votre audition, l'attention à votre environnement s'est détériorée..."
            "..."
            "(sensation d'une détonation)"
            "..."
            jump ENDING04

    $ previous = "A"
    $ clock += 1
menu:
    "NORD":
        jump B
    "SUD":
        jump F

label ChoiceA1:
    MC "Je souhaiterais passer pour accéder à la réserve de munitions,"
    if not K_isVisite:
        MC "Mon nombre de munition descent dangeureusement ..."
    if K_isVisite:
        MC "Mon nombre de munition est bien bas," 
        MC "et il me faut des explosifs pour accéder au poste de commandement..."
    S2 "On ne peut pas vous laissez passer pour ça,"
    S2 "notre nombre de munitions est bien trop bas pour pouvoir vous en passer comme cela,"
    S2 "..."
    S2 "Enfin sans avoir quelque chose en échange"
    if foodInventory == True:
        MC "J'ai de la nourriture en stock si vous souhaitez"
        S1 "..."
        S2 "Pourquoi pas ..."
        $accessA_to_B = True
    if foodInventory == False:
        MC "Je n'ai pas grand chose à échanger actuellement..."
        S1 "Si vous trouvez de la nourriture, on devrait pouvoir trouver un compromis"
        S2 "Revenez nous voir quand ce sera bon ..."
        "Vous retournez sur vos pas."
        jump previous
    
    "Vous pouvez vous rendre à la réserve de munition."
    "Souhaitez vous-y aller ?"
menu:
    "Oui":
        jump B
    "Non":
        jump A



label B: #Ammo
    scene bg AMMO
    with fade
    show GAS_MASK

    "Vous arrivez dans la réserve de munitions."
    

    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == False:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."
    
    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == False:
            "Vous entendez au loin un coup de feu au loin ..."
            "..."

    if sanity < SANITY_MIN:
        if lostAudition == False:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            S "Soldat! Est-ce que sa va ? Vous m'entendez ?"
            "Vous observez alors sans comprendre votre commandant:"
            C "Ressaisissez-vous soldat! Les Bochs sont là!"
            "À ces mots," 
            "vous vous rendez compte que des soldats commencent à
            prendre d'assaut l'artillerie."
            "Pris de panique, vous vous saisissez d'un explosif à coté..."
            menu:
                "Détoner l'explosif":
                    "Armé, vous jeté l'explosif dans la direction de la sortie de la pièce,"
                    "éspérant toucher le plus d'ennemi possible ..."
                    "..."
                    "Lorsque l'explosif détonna,"
                    "Le souffle propulsat bon nombre de débris dans votre direction ..."
                    "Sectionnant votre jugulaire et plusieurs artères ..."
                    "..."
                    jump ENDING06
                "Ne rien faire":
                    "Vous décidez de ne pas jeter l'explosif"
                    "Cependant la menace que représente votre misérable existance,"
                    "a incité un soldat allié à proximité à vous fusillé..."
                    jump ENDING01
        if lostAudition == True:
            "Alors que votre état mental était au plus bas,"
            "et votre audition aussi affuté qu'un tron d'arbre,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            S "..."
            "Vous observez alors sans comprendre votre commandant:"
            C "..."
            "À ces mots, que vous semblez reconnaître..." 
            "Vous vous rendez compte que des bochs commencent à
            prendre d'assaut l'artillerie."
            "Pris de panique, vous vous saisissez d'un explosif à coté..."
            menu:
                "Détoner l'explosif":
                    "Armé, vous jeté l'explosif dans la direction de la sortie de la pièce,"
                    "éspérant toucher le plus d'ennemi possible ..."
                    "..."
                    "Lorsque l'explosif détonna,"
                    "Le souffle propulsat bon nombre de débris dans votre direction ..."
                    "Sectionnant votre jugulaire et plusieurs artères ..."
                    "..."
                    jump ENDING06
                "Ne rien faire":
                    "Vous décidez de ne pas jeter l'explosif"
                    "Cependant la menace que représente votre misérable existance,"
                    "a incité un soldat allié à proximité à vous fusillé..."
                    jump ENDING01
        
    if sanity > SANITY_MAX:
        if lostAudition == False:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition == True:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "Vous vous enfoncez toujours plus profondément dans les tranchées."
            "..."
            "Pris d'une envie soudaine d'être le héros,"
            "Vous choisissez de regarder en dehors des tranchées pour pouvoir abbatre l'ennemie"
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04

    "Prenez-vous des explosif / munitions ?"
    $ previous = "B"
    $ clock += 1
menu:
    "Oui":
        $ hadExplosif = True
        "Vous avez pris des explosifs."
    "Non":
        "Vous ne prenez pas d'explosifs."
    
"Où souhaitez vous allez ?"

menu:
    "SUD":
        jump A
    "EST":
        jump D



label C: #Garde-Mangé
    scene bg FOOD
    with fade
    show GAS_MASK
    
    
    $ previous = "C"
    define canTakeFood = True
    if clock >= 15 and clock <= 22 and sanity <= SANITY_MAX and sanity >= SANITY_MIN + 40 and isFirstIterationE:
        scene bg FOOD_RATS
        with fade
        show GAS_MASK

        "Les rats ont commencé à prendre part aux festivités..."
        "..."
        $ canTakeFood = False

    if clock >= 15 and clock <= 22 and sanity <= SANITY_MAX and sanity >= SANITY_MIN + 40 and not isFirstIterationE:
        "Les rats sont toujours là..."
        "..."
        scene bg FOOD_RATS
        with fade
        show GAS_MASK

        $canTakeFood = False

    if canTakeFood == True and foodInventory == False and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        
        jump takeFoodLabel

    if canTakeFood == True and foodInventory == True and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Il semblerait que vous ayez déjà en votre position de la nourriture..."
        $clock += 1
        "Vous avez perdu du temps."



    if clock >= 15 and clock <= 22 and sanity <= -60 and sanity >= SANITY_MIN :
        "Il semblerait que des soldats ait laissé trainé de la nourriture par terre ..."

    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == False:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == False:
            "Vous entendez au loin un coup de feu au loin ..."
            "..."
    if clock >= 23 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Alors que vous êtes dans le garde-mangé,"
        "Un bruit couplé aux rats grouillant autour de vous se fait entendre..."
        "..."
        "Un simple bruit de métal tappant régulièrement contre la porte intallé à la hâte ..."
        "..."
        if lostAudition == False:
            SA "Nun, nun, mein liebes kleines Französchen," 
            SA "das sich so gerne den Ratten zur Schau stellt!" 
            SA "Man erkennt hier deutlich das schlichte Gemüt des kleinen Gockels," 
            SA "der Sie nun einmal sind..." 
            SA "Erlauben Sie mir, Ihnen dabei behilflich zu sein," 
            SA "zu den Ihren zurückzukehren..."
            "..."
            "Sans pouvoir riposter, une détonation se fait entendre..."
            "..."
        if lostAudition == True:
            SA "..."
            SA "..."
            SA "..."
            SA "..."
            SA "..."
            SA "..."
            SA "..."
            SA "..."
            "Sans pouvoir riposter, une détonation se fait entendre..."
            SA "..."
        jump ENDING01

    if sanity < SANITY_MIN:
        "Alors que votre état mental était au plus bas,"
        "un sentiment de mal-être vous envahi petit à petit."
        "..."
        "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
        "Le réel de l'iréel..."
        "..."
        "Vous perdez complètement la raison ..."
        "..."
        if lostAudition == False:
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
        if lostAudition == True:
            "..."
            "..."
            "..."
            "Vous ressentez une détonation ..."
        "..."
        jump ENDING03
    if sanity > SANITY_MAX:
        if lostAudition == False:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition == True:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "Vous choisissez telle un héros de sortir la tête des tranchées..."
            "..."
            "(sensation d'une détonation)"
            "..."
            jump ENDING04


$ clock += 1
menu:
    "EST":
        jump F

label takeFoodLabel:
    "Il semblerait que votre inventaire n'ait pas de nourriture,"
    "souhaitez-vous en prendre ?"

menu:
    "Oui":
        if sanity <= -60:
            $foodIsRat = True
        $foodInventory = True
        jump previous
    "Non":
        jump previous

label D: 
    scene bg TRENCH_X_FLIPPED
    with fade
    show GAS_MASK
    $ previous = "D"

    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == False:
            "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
            "Votre audition est assourdie pendant quelques secondes ..."
            if sanity < -60:
                "Vous commencez à faire une petite crise de panique ..."
                $ sanity -= 10
                "Votre santé mentale est encore plus basse ..."
    
    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == False:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."
        

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == False:
            "Vous entendez au loin un coup de feu au loin ..."
            "..."

    if clock >= 23 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        
        if lostAudition == False:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais d'autres bruits commencent à surgir au loin ..."
            "Vous entendez des bruits d'armes à feu,"
            "ainsi que des cris de soldats au loin."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            "Vous entendez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
        if lostAudition == True:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu..."
            "Tout semble trop calme..."
            "..."
            SA "..."
        "..."
        "Un Boch apparait alors dans votre champ de vision,"
        "arme à la main, prêt à vous abattre ..."
        "..."
        if lostAudition == False:
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
        if lostAudition == True:
            "..."
            "..."
            "Vous ressentez une détonation..."
        "..."
        jump ENDING01

    if sanity < SANITY_MIN:
        "Alors que votre état mental était au plus bas,"
        "un sentiment de mal-être vous envahi petit à petit."
        "..."
        "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
        "Le réel de l'iréel..."
        "..."
        "Vous perdez complètement la raison ..."
        "..."
        if lostAudition == False:
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
        if lostAudition == True:
            "..."
            "..."
            "..."
            "Vous ressentez une détonation ..."
        "..."
        jump ENDING03
    if sanity > SANITY_MAX:
        if lostAudition == False:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition == True:
            "Telle le héros que vous voulez devenir,"
            "une idée brillante vous viens à l'esprit:"
            MC "(Allons jeter un oeil en dehors des tranchées pour aider au combat)"
            "..."
            "Vous regardez en dehors des tranchées."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
    

$ clock += 1
menu:
    "NORD":
        jump E
    "SUD":
        jump H
    "OUEST":
        jump B
    "EST":
        jump I


label E: 
    scene bg TRENCH_L_FLIP
    with fade
    show FRENCH
    show GAS_MASK
    $ previous = "E"

    if clock >= 8 and clock <= 22 and sanity <= SANITY_MAX and sanity >= SANITY_MIN + 40 and isFirstIterationE:
        "Les rats ont commencé à prendre part aux festivités..."
        "..."
    if clock >= 8 and clock <= 22 and sanity <= SANITY_MAX and sanity >= SANITY_MIN + 40 and not isFirstIterationE:
        "Les rats sont toujours là..."
        "..."

    if clock >= 8 and clock <= 22 and sanity <= -60 and sanity >= SANITY_MIN :
        "Il semblerait que des soldats ait laissé trainé de la nourriture par terre ..."
        
        
    
    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous sentez de violante secousses" 
        "surevenu suite à l'explosion d'obus non loin de vous ..."
        "..."
        "Les rats sont agités"
        "..."
        "Votre audition est assourdie pendant quelques heures ..."
        $ clock += 5
        "Vous perdez l'audition"
        $ lostAudition = True

    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == False:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."
        

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == False:
            "Vous entendez au loin un coup de feu au loin ..."
            "..."
        
    if clock >= 23 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == False:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais d'autres bruits commencent à surgir au loin ..."
            "Vous entendez des bruits d'armes à feu,"
            "ainsi que des cris de soldats au loin."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            "Vous entendez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
            "..."
            "Un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING01
        if lostAudition == True:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais l'agitation dans les tranchées se fait de plus en plus présente..."
            "..."
            "C'est alors que très proche de vous, un soldat allié tombe à côté de vous,"
            "..."
            "criblé de balles..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
            "..."
            jump ENDING01

    if sanity < SANITY_MIN:
        
        "Alors que votre état mental était au plus bas,"
        "un sentiment de mal-être vous envahi petit à petit."
        "..."
        "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
        "Le réel de l'iréel..."
        "..."
        "Vous perdez complètement la raison ..."
        "..."
        if lostAudition== False:
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
        if lostAudition== True:
            SA "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
        "..."
        jump ENDING03
    if sanity > SANITY_MAX:
        if lostAudition == False:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition == True:
            "Telle le héros que vous voulez devenir,"
            "une idée brillante vous viens à l'esprit:"
            MC "(Allons jeter un oeil en dehors des tranchées pour aider au combat)"
            "..."
            "Vous regardez en dehors des tranchées."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04


$ clock += 1 
menu:
    "SUD":
        jump D



label F:
    $ previous = "F"
    
    if clock == 6 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez un violant bruit d'explosion d'obus non loin de vous ..."
        "Votre audition est assourdie pendant quelques heures ..."
        $ clock += 2
        "Vous avez perdu l'audition."
        $ lostAudition = True
    
    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous sentez de violante secousses" 
        "survenu suite à l'explosion d'obus non loin de vous ..."
        if lostAudition == False:
            "Votre audition est assourdie pendant quelques heures ..."
        $ clock += 5

    if clock == 15 and sanity <= -60 and sanity >= -100:
        if lostAudition == False:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."
        if lostAudition == True:
            "Vous remarquez autour de vous une certaine agitation des troupes..."
    
    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."
    if clock >= 22 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == True:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais problème arrivent..."
            "..."
            "Vous voyez alors un soldat devant vous tomber au combat,"
            "Un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
            "..."
            jump ENDING01
        if lostAudition == False:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais problème arrivent..."
            "..."
            "Vous voyez alors un soldat devant vous tomber au combat,"
            "un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "Hier"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING01

    if sanity < SANITY_MIN:
        "Alors que votre état mental était au plus bas,"
        "un sentiment de mal-être vous envahi petit à petit."
        "..."
        "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
        "Le réel de l'iréel..."
        "..."
        "Vous perdez complètement la raison ..."
        "..."
        if lostAudition == False:
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
        if lostAudition == True:
            SA "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
        "..."
        jump ENDING03
    if sanity > SANITY_MAX:
        if lostAudition == False:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition == True:
            "Alors que l'un des soldats à côté de vous se prépare à attaquer en dehors des tranchées,"
            "L'idée de devenir un héros à ces yeux deviens clair..."
            MC "Attend, laisse moi faire..."
            "..."
            "(ressentie d'une détonnation)"
            "..."
            jump ENDING04
    

$ clock += 1  
menu:
    "NORD":
        jump G
    "SUD":
        jump C
    "OUEST":
        jump A
    "EST":
        jump J



label G:
    $ previous = "G"

    if clock == 6 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez un violant bruit d'explosion d'obus non loin de vous ..."
        "Votre audition est assourdie pendant quelques minutes ..."
        $ clock += 5
        "Vous avez perdu l'audition."
        $ lostAudition = True

    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == False:
            "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
            "Votre audition est assourdie pendant quelques secondes ..."
            if sanity < -60:
                "Vous commencez à faire une petite crise de panique ..."
                $ sanity -= 10
                "Votre santé mentale est encore plus basse ..."
    
    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == False:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."
    
    if clock >= 23 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if lostAudition == False:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais d'autres bruits commencent à surgir au loin ..."
            "Vous entendez des bruits d'armes à feu,"
            "ainsi que des cris de soldats au loin."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            "Vous entendez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
            "..."
            "Un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING01
        if lostAudition == True:
            "Les bombardements survenue ans la zone se sont progressivement arrêtés,"
            "..."
            "Mais pas votre absurdité..."
            "..."
            "Vous avez choisie de levé la tête des tranchées..."
            "(Sensation de détonation)"

    if sanity < SANITY_MIN:
        if lostAudition == False:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING03
        if lostAudition == True:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            SA "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
            "..."
            jump ENDING03
    if sanity > SANITY_MAX:
        if not lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition:
            "Telle le héros que vous voulez devenir,"
            "une idée brillante vous viens à l'esprit:"
            MC "(Allons jeter un oeil en dehors des tranchées pour aider au combat)"
            "..."
            "Vous regardez en dehors des tranchées."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
    

$ clock += 1  
menu:
    "NORD":
        jump H
    "SUD":
        jump F
    "EST":
        jump K


label H:
    $ previous = "H"

    if clock == 6 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez un violant bruit d'explosion d'obus non loin de vous ..."
        "Votre audition est assourdie pendant quelques minutes ..."
        $ clock += 5
        "Vous avez perdu l'audition."
        $ lostAudition = True

    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
            "Votre audition est assourdie pendant quelques secondes ..."
            if sanity < -60:
                "Vous commencez à faire une petite crise de panique ..."
                $ sanity -= 10
                "Votre santé mentale est encore plus basse ..."
    
    if clock == 8 and sanity >= 60 and sanity <= 100:
        if not lostAudition:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."
    
    if clock == 12 and sanity > -60 and sanity < 60:
        if not lostAudition:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez au loin un coup de feu au loin ..."
            "..."

    if clock >= 23 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais d'autres bruits commencent à surgir au loin ..."
            "Vous entendez des bruits d'armes à feu,"
            "ainsi que des cris de soldats au loin."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            "Vous entendez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
            "..."
            "Un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING01
        if lostAudition:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais d'autres sensations commencent à surgir au loin ..."
            "Vous voyez des soldats au loin se battre..."
            "..."
            SA "..."
            "Vous voyez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
            "..."
            "Un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
            "..."
            jump ENDING01

    if sanity < SANITY_MIN:
        "Alors que votre état mental était au plus bas,"
        "un sentiment de mal-être vous envahi petit à petit."
        "..."
        "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
        "Le réel de l'iréel..."
        "..."
        "Vous perdez complètement la raison ..."
        "..."
        if not lostAudition:
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
        if lostAudition:
            SA "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
        "..."
        jump ENDING03
    if sanity > SANITY_MAX:
        if not lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition:
                "Alors que vous foncez déterminer à travert les tranchées,"
                "une idée brillante vous vient à l'esprit:"
                MC "(Sortons la tête des tranchées pour observer l'ennemie)"
                "..."
                "(bruit d'une détonation)"
                "..."
                jump ENDING04
    

$ clock += 1
menu:
    "NORD":
        jump I
    "SUD":
        jump G
    "OUEST":
        jump D

label I: 
    $ previous = "I"
    if clock ==10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez siffler de plus en plus forte un objet dans le ciel ..."
        "Le tonnerre gronde et l'humanité vous foudroie de toute sa puissance."
        "Vous voyez alors,"
        "un obus arriver sur vous..."
        "à une vitesse dont nulle personne ne pourrait en réchapper."
        "Vous êtes frappé de plein fouet par l'explosion ..."
        "..."
        "Vous êtes mort."
        jump ENDING02
    
    if clock >= 11 and clock < 15 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Les bombardements viennes tout justes de s'arrêter..."
        "La zone n'est cependant plus accessible dû aux nombreux débrit dans la zone."
        "Vous revenez en arrière."
        $ clock += 1
        jump previous
        

    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."
    
    if clock >= 15 and clock <= 21 and sanity <= SANITY_MAX and sanity >= SANITY_MIN + 40 and isFirstIterationE:
        "Les rats ont commencé à prendre part aux festivités..."
        "..."
    if clock >= 15 and clock <= 21 and sanity <= SANITY_MAX and sanity >= SANITY_MIN + 40 and not isFirstIterationE:
        "Les rats sont toujours là..."
        "..."

    if clock >= 15 and clock <= 21 and sanity <= -60 and sanity >= SANITY_MIN :
        "Il semblerait que des soldats ait laissé trainé de la nourriture par terre ..."
        

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez au loin un coup de feu au loin ..."
            "..."
    
    if clock >= 22 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais d'autres bruits commencent à surgir au loin ..."
            "Vous entendez des bruits d'armes à feu,"
            "ainsi que des cris de soldats au loin."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            "Vous entendez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
            "..."
            "Un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING01
        if lostAudition:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais d'autres sensations commencent à surgir au loin ..."
            "Vous voyez des soldats au loin se battre..."
            "..."
            SA "..."
            "Vous voyez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
            "..."
            "Un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
            "..."
            jump ENDING01

    if sanity < SANITY_MIN:
        if not lostAudition:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING03
        if lostAudition:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            SA "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
            "..."
            jump ENDING03
    if sanity > SANITY_MAX:
        if not lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "une idée merveilleuse et segronu vous viens à l'esprit:"
            MC "(Sortons la tête des tranchées pour observer l'ennemie...)"
            "..."
            "Vous observez alors qu'un soldat au loin se fait fusiller."
            "..."
            "Vous voyez également un canon à très courte porté..."
            "de votre tête."
            SA "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04


$ clock += 1
menu:
    "NORD":
        jump M
    "SUD":
        jump H
    "OUEST":
        jump D
    "EST":
        jump L

label J: 
    $ previous = "J"

    if clock == 6 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
            "Votre audition est assourdie pendant quelques secondes ..."
            if sanity < -60:
                "Vous commencez à faire une petite crise de panique ..."
                $ sanity -= 10
                "Votre santé mentale est encore plus basse ..."
    
    if clock == 8 and sanity >= 60 and sanity <= 100:
        if not lostAudition:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."
    
    if clock == 12 and sanity > -60 and sanity < 60:
        if not lostAudition:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez au loin un coup de feu au loin ..."
            "..."

    if clock >= 21 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais d'autres bruits commencent à surgir au loin ..."
            "Vous entendez des bruits d'armes à feu,"
            "ainsi que des cris de soldats au loin."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            "Vous entendez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
            "..."
            "Un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING01
        if lostAudition:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais d'autres sensations commencent à surgir au loin ..."
            "Vous voyez des soldats au loin se battre..."
            "..."
            SA "..."
            "Vous voyez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
            "..."
            "Un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
            "..."
            jump ENDING01

    if sanity < SANITY_MIN:
        "Alors que votre état mental était au plus bas,"
        "un sentiment de mal-être vous envahi petit à petit."
        "..."
        "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
        "Le réel de l'iréel..."
        "..."
        "Vous perdez complètement la raison ..."
        "..."
        if not lostAudition:
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
        if lostAudition:
            SA "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
        "..."
        jump ENDING03
    if sanity > SANITY_MAX:
        if not lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition:
            "Que ce passerait-il si par le plus grand des hazards,"
            "l'humanité faisait appel à son plus grand des héros,"
            "pour regarder où se trouve l'ennemie par dessus les tranchées ?"
            "..."
            "Cette idée aussi merveilleuse soit-elle, mis en place par votre personne,"
            "n'a pas eu l'effet esconté..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
    

$ clock += 1
menu:
    "NORD":
        jump K
    "OUEST":
        jump F
    "EST":
        jump N

label K: 
    $ previous = "K"
    $ K_isVisite = True
    #le test pour savoir si on a un explosif sert à savoir si l'on peux rentrer.
    if not hadExplosif:
        "N'ayant pas d'explosif sous la main," 
        "vous remarquez que l'accès au poste de commandement est bloqué."
        MC "(Il faudrait que j'aille chercher des explosif à l'ouest)"
        if clock >= 22 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
            "Cependant, chaque chose en son temps,"
            "..."
            "Car en effet,"
            "Vous n'êtes pas seul sur la deventure du poste."
            if not lostAudition:
                SA "Keine Bewegung!"
            if lostAudition:
                SA "..."
            "..."
            jump ENDING01
        jump previous

    "Vous entrez dans le centre de commandement."
    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez au loin dehors un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."

    if clock == 15 and sanity <= -60 and sanity >= -100:
        if not lostAudition:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez au loin un coup de feu au loin ..."
            "..."

    if clock >= 22 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Alors que vous vous trouvez dans le centre de commandement,"
            "votre arme posée à l'entrée de la petite pièce,"
            "pour vous permettre de rétablir tant bien que mal les communications,"
            "entouré des cadavres de dizaines de soldats,"
            "des coups de feu et des cris se font entendre au loin ..."
            "..."
            "Puis,"
            "Sans avoir eu le temps de réagir,"
            "Un bruit métalique retentit contre la porte de fortune installée à la hâte ..."
            SA "Na, na, man muss sich wohl eingestehen"
            SA "in jenem guten Französisch, das mir nicht eigen ist," 
            SA "und um es mit Ihren eigenen Worten zu sagen:" 

            "Vous vous rendez compte que l'allemand qui parle est proche de vous ..."
            "et que de plus,"
            "votre arme n'est pas avec vous..."


            SA "La voix du plus fort est à celui qui le prévoit le mieux." 

            "Votre arme se situe proche de l'entrée,"
            "proche de l'officier allemand..."

            SA "das ist ein Kinderreim, den meine Brüder und ich oft aufsagten," 
            SA "als wir noch klein waren. Sie erinnern mich an meinen Bruder..." 
            SA "bevor ich seinen Tagen ein Ende setzte..."

            MC "Att..."

            "Avant même d'avoir pu commencer votre phrase,"
            "Une détonation s'est fait entendre ..."

            jump ENDING01
        
        if lostAudition:
            "Alors que vous vous trouvez dans le centre de commandement,"
            "votre arme posée à l'entrée de la petite pièce,"
            "pour vous permettre de rétablir tant bien que mal les communications,"
            "entouré des cadavres de dizaines de soldats,"
            "des coups de feu et des cris se font entendre au loin ..."
            "..."
            "Puis,"
            "Sans avoir eu le temps de réagir,"
            "Un bruit métalique retentit contre la porte de fortune installée à la hâte ..."
            SA "Na, na, man muss sich wohl eingestehen"
            SA "in jenem guten Französisch, das mir nicht eigen ist," 
            SA "und um es mit Ihren eigenen Worten zu sagen:" 

            "Vous vous rendez compte que l'allemand qui parle est proche de vous ..."
            "et que de plus,"
            "votre arme n'est pas avec vous..."


            SA "La voix du plus fort est à celui qui le prévoit le mieux." 

            "Votre arme se situe proche de l'entrée,"
            "proche de l'officier allemand..."

            SA "das ist ein Kinderreim, den meine Brüder und ich oft aufsagten," 
            SA "als wir noch klein waren. Sie erinnern mich an meinen Bruder..." 
            SA "bevor ich seinen Tagen ein Ende setzte..."

            MC "Att..."

            "Avant même d'avoir pu commencer votre phrase,"
            "Une détonation s'est fait entendre ..."

            jump ENDING01


    if sanity < SANITY_MIN:
        if not lostAudition:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            S "Die Feldgraue sind da! Die Feldgraue sind da!"
            S "Hier!"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING03
        if lostAudition:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            S "..."
            S "..."
            "..."
            "Vous ressentez une détonation ..."
            "..."
            jump ENDING03
    if sanity > SANITY_MAX:
        if not lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition:
            "Que ce passerait-il si par le plus grand des hazards,"
            "l'humanité faisait appel à son plus grand des héros,"
            "pour regarder où se trouve l'ennemie par dessus les tranchées ?"
            "..."
            "Cette idée aussi merveilleuse soit-elle, mis en place par votre personne,"
            "n'a pas eu l'effet esconté..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04


$ clock += 1
menu:
    "SUD":
        jump J
    "OUEST":
        jump G

label L: 
    $ previous = "L"
    if clock == 4 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez au loin le bruit d'une mitrailleuse lourde ..."
        
    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
            "Votre audition est assourdie pendant quelques secondes ..."
            if sanity < -60:
                "Vous commencez à faire une petite crise de panique ..."
                $ sanity -= 10
                "Votre santé mentale est encore plus basse ..."

    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez au loin un coup de feu au loin ..."
            "..."

    if clock >= 21 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais d'autres bruits commencent à surgir au loin ..."
            "Vous entendez des bruits d'armes à feu,"
            "ainsi que des cris de soldats au loin."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            "Vous entendez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
            "..."
            "Un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING01
        if lostAudition:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais d'autres sensations commencent à surgir au loin ..."
            "Vous voyez des soldats au loin se battre..."
            "..."
            SA "..."
            "Vous voyez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
            "..."
            "Un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
            "..."
            jump ENDING01


    if sanity < SANITY_MIN:
        if not lostAudition:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING03
        if lostAudition:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            SA "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
            "..."
            jump ENDING03
    if sanity > SANITY_MAX:
        if not lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition:
            "Que ce passerait-il si par le plus grand des hazards,"
            "l'humanité faisait appel à son plus grand des héros,"
            "pour regarder où se trouve l'ennemie par dessus les tranchées ?"
            "..."
            "Cette idée aussi merveilleuse soit-elle, mis en place par votre personne,"
            "n'a pas eu l'effet esconté..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
            

$ clock += 1
menu:
    "SUD":
        jump O
    "OUEST":
        jump I
    "EST":
        jump P


label M:
    $ previous = "M"

    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
            "Votre audition est assourdie pendant quelques secondes ..."
            if sanity < -60:
                "Vous commencez à faire une petite crise de panique ..."
                $ sanity -= 10
                "Votre santé mentale est encore plus basse ..."
    
    if clock == 8 and sanity >= 60 and sanity <= 100:
        if not lostAudition:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."
    
    if clock == 12 and sanity > -60 and sanity < 60:
        if not lostAudition:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."
    
    if clock == 15 and sanity <= -60 and sanity >= -100:
        if not lostAudition:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez au loin un coup de feu au loin ..."
            "..."
    if clock >= 23 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais d'autres bruits commencent à surgir au loin ..."
            "Vous entendez des bruits d'armes à feu,"
            "ainsi que des cris de soldats au loin."
            "..."
            "Dans l'endroit clos où vous vous situez actuellement,"
            "armé seulement de votre baïonnette,"
            "les bruits d'armes à feu et de cris se font de plus en plus proches ..."
            "..."
            S "Vite! Vite! Ils arrivent!"
            "Vous voyez alors le soldat ayant clamé cela se faire fusillé devant vous."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            "..."
            "Un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING01
        if not lostAudition:
            "Les bombardements d'obus à proximité se sont arrêtés depuis peu,"
            "mais d'autres ennuie arrivent au loin."
            "..."
            "Dans l'endroit clos où vous vous situez actuellement,"
            "armé seulement de votre baïonnette,"
            "les bruits d'armes à feu et de cris se font de plus en plus proches ..."
            "..."
            S "..."
            "Vous voyez alors le soldat ayant clamé cela se faire fusillé devant vous."
            SA "..."
            "..."
            "Un Boch apparait alors dans votre champ de vision,"
            "arme à la main, prêt à vous abattre ..."
            "..."
            SA "..."
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING01

    
    if sanity < SANITY_MIN:
        if not lostAudition:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING03
        if lostAudition:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            SA "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
            "..."
            jump ENDING03
    if sanity > SANITY_MAX:
        if not lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition:
            "Que ce passerait-il si par le plus grand des hazards,"
            "l'humanité faisait appel à son plus grand des héros,"
            "pour regarder où se trouve l'ennemie par dessus les tranchées ?"
            "..."
            "Cette idée aussi merveilleuse soit-elle, mis en place par votre personne,"
            "n'a pas eu l'effet esconté..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04


$ clock += 1
menu:
    "SUD":
        jump I

label N:

    $ previous = "N" 
    if (clock == 6 or clock == 10) and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez siffler de plus en plus forte un objet dans le ciel ..."
            "Le tonnerre gronde et l'humanité vous foudroie de toute sa puissance."
            "Vous voyez alors,"
        if lostAudition:
            "Alors que vous n'entendiez plus grand chose," 
            "vous voyez alors quelque chose dans le ciel,"
        "un obus arriver sur vous..."
        "à une vitesse dont nulle personne ne pourrait en réchapper."
        "Vous êtes frappé de plein fouet par l'explosion ..."
        "..."
        "Vous êtes mort."
        jump ENDING02
    if clock >= 7 and clock != 10 and clock < 20 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Les bombardements viennes tout justes de s'arrêter..."
        "La zone n'est cependant plus accessible dû aux nombreux débrit dans la zone."
        "Vous revenez en arrière."
        $ clock +=  1
        jump previous
        
    if clock >= 20 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Les bombardements d'obus se sont arrêtés depuis peu,"
        if not lostAudition:
            "mais d'autres bruits commencent à surgir au loin ..."
            "Vous entendez des bruits d'armes à feu,"
            "ainsi que des cris de soldats au loin."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            "Vous entendez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
        if lostAudition:
            "mais d'autres problèmes surgissent au loin."
            "Vous appercevez d'autres soldats au loin tomber au combat..."
            "..."
            SA "..."
            "Vous voyez les soldats français," 
            "se faire déchirer par les balles ennemies ..."
        "..."
        "Un Boch apparait alors dans votre champ de vision,"
        "arme à la main, prêt à vous abattre ..."
        "..."
        if not lostAudition:
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
        if lostAudition:
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
        "..."
        jump ENDING01
    if sanity < SANITY_MIN:
        "Alors que votre état mental était au plus bas,"
        "un sentiment de mal-être vous envahi petit à petit."
        "..."
        "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
        "Le réel de l'iréel..."
        "..."
        "Vous perdez complètement la raison ..."
        "..."
        if not lostAudition:
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
        if lostAudition:
            SA "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
        "..."
        jump ENDING03
    if sanity > SANITY_MAX:
        if not lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "une idée merveilleuse vous viens alors à l'esprit,"
            "puisque rien ne peux vous tuer dans ce monde,"
            "il vous suffirait de vous montrer sur votre 31," 
            "pour que l'ennemie se montre par lui-même..."
            "..."
            jump ENDING04




$ clock += 1   
menu:
    "NORD":
        jump O
    "OUEST":
        jump J

label O: 
    $ previous = "O"
    
    if clock == 6 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
            "Votre audition est assourdie pendant quelques secondes ..."
            if sanity < -60:
                "Vous commencez à faire une petite crise de panique ..."
                $ sanity -= 10
                "Votre santé mentale est encore plus basse ..."

    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez au loin un bruit de sifflet ..."
            "..."
            "Les allemand arrivent."
            "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        if not lostAudition:
            "Vous entendez au loin un coup de feu au loin ..."
            "..."

    if clock >= 20 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Les bombardements d'obus se sont arrêtés depuis peu,"
        if not lostAudition:
            "mais d'autres bruits commencent à surgir au loin ..."
            "Vous entendez des bruits d'armes à feu,"
            "ainsi que des cris de soldats au loin."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            "Vous entendez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
        if lostAudition:
            "mais d'autres problèmes surgissent au loin."
            "Vous appercevez d'autres soldats au loin tomber au combat..."
            "..."
            SA "..."
            "Vous voyez les soldats français," 
            "se faire déchirer par les balles ennemies ..."
        "..."
        "Un Boch apparait alors dans votre champ de vision,"
        "arme à la main, prêt à vous abattre ..."
        "..."
        if not lostAudition:
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
        if lostAudition:
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
        "..."
        jump ENDING01
    if sanity < SANITY_MIN:
        "Alors que votre état mental était au plus bas,"
        "un sentiment de mal-être vous envahi petit à petit."
        "..."
        "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
        "Le réel de l'iréel..."
        "..."
        "Vous perdez complètement la raison ..."
        "..."
        if not lostAudition:
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
        if lostAudition:
            SA "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
        "..."
        jump ENDING03
    if sanity > SANITY_MAX:
        if not lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "une idée merveilleuse vous viens alors à l'esprit,"
            "puisque rien ne peux vous tuer dans ce monde,"
            "il vous suffirait de vous montrer sur votre 31," 
            "pour que l'ennemie se montre par lui-même..."
            "..."
            jump ENDING04


$ clock += 1
menu:
    "NORD":
        jump P
      
    "SUD": 
        jump N
    "OUEST":
        jump L
         

label P:
    
"Vous arrivez à une intersection de la tranché de première ligne."

if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
    if not lostAudition:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
    if not lostAudition:
        "Vous entendez un coup de feu proche de vous ..."
        "..."

if clock >= 20 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Les bombardements d'obus se sont arrêtés depuis peu,"
        if not lostAudition:
            "mais d'autres bruits commencent à surgir au loin ..."
            "Vous entendez des bruits d'armes à feu,"
            "ainsi que des cris de soldats au loin."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            "Vous entendez les corps de soldats français," 
            "se faire déchirer par les balles ennemies ..."
        if lostAudition:
            "mais d'autres problèmes surgissent au loin."
            "Vous appercevez d'autres soldats au loin tomber au combat..."
            "..."
            SA "..."
            "Vous voyez les soldats français," 
            "se faire déchirer par les balles ennemies ..."
        "..."
        "Un Boch apparait alors dans votre champ de vision,"
        "arme à la main, prêt à vous abattre ..."
        "..."
        if not lostAudition:
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
        if lostAudition:
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
        "..."
        jump ENDING01
# CHOIX
if sanity <= SANITY_MAX and sanity >= SANITY_MIN:
    "Vous vous approchez et vous voyez un soldat."
    "Ce soldat fonce brusquement sur vous et criant"
    if not lostAudition:
        S "QU'ATTENDEZ VOUS POUR TIREZ ?"
        S "LES ALLEMANDS SONT LÀ, ILS ARRIVENT!!!"
        if clock < 12:
            "Vous le regardez surpris, vous ne pensiez pas que les allemands attaquerait déjà"
        if clock >= 12:
            "Le bruit de sifflet aurait-il été faux ?"
    if lostAudition:
        S "... ?"
        S "... !!!"
        if clock < 12:
            "Vous le regardez surpris, vous ne comprennez pas ce qui a été dit"
            "Le soldat vous regarde dubitatif"
    # CHOIX REGARDER/TIRER/NE RIEN FAIRE
menu : 
    "...":
        jump P_1
    "Regarder l'ennemi venir":
        jump P_2
    "Tirer avec le soldat":
        jump P_3
label P_1:
    if not lostAudition:
        S "Tu ne tires pas ?"
        S "Très bien... Tu es un déserteur en quelque sorte..."
        S "Ne m'oblige pas à te tuer..."
        S "Les ordres sont pourtant claire..."
        S "Tout deserteur doit être abattue immédiatement!"
        jump ENDING01
    if lostAudition:
        S "... ?"
        S "..."
        S "..."
        S "..."
        S "..."
        "Sans que vous puissiez réagir,"
        jump ENDING01

label P_2:
    "Vous monter très toucement l'echelle."
    "Au moindre bruit, les allemands pourrait être alerté."
    "Un seul bruit et votre vie oté, servant de repas au rat."
    if sanity > SANITY_MAX:
        if not lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "une idée merveilleuse vous viens alors à l'esprit,"
            "puisque rien ne peux vous tuer dans ce monde,"
            "il vous suffirait de vous montrer sur votre 31," 
            "pour que l'ennemie se montre par lui-même..."
            "..."
            jump ENDING04
    if sanity < SANITY_MIN:
        if not lostAudition:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
            "..."
            jump ENDING03
        if lostAudition:
            "Alors que votre état mental était au plus bas,"
            "un sentiment de mal-être vous envahi petit à petit."
            "..."
            "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
            "Le réel de l'iréel..."
            "..."
            "Vous perdez complètement la raison ..."
            "..."
            SA "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
            "..."
            jump ENDING03
    "Heureusent, vous avez réussi à vous faire discret."
    scene bg FRONT
    with fade
    show GAZ_MASK
    "Mais malheureusement,"
    "Vous ne voyez aucun soldat à l'horizon."
    "Seulement les fortifications au loin,"
    "Votre nouvel ami semble faire une paranoia."
    scene bg SURVIVOR
    with fade
    show GAZ_MASK
    "Un phénomène courant dans les tranchers,"
    "Des crises de nerds déclenchable à cause d'un haut taux d'horreur."
    "Ce qui peut provoquer des hallucinations"
    "Vous lui faite donc par de son hallucination"
    "Mais ne veux malheureusement rien entendre et commence à ouvrir le feu"
    $ clock += 1   

    
    jump P00
label P_3: 
    "Vous répondez positivement à l'appel!"
    if not lostAudition:
        S "AH! Voilà un bon soldat !"
    if lostAudition:
        S "..."
    scene bg FRONT
    with fade
    show GAZ_MASK
    "Vous vous mettez donc en positions et tiré donc sans relache,"
    "Ni en regardant réellement sur quoi ou sur qui vous tirez,"
    "Il se trouve qu'il n'y a personne"
    "Cependant..."
    "À cause vos coups, vous avez attirez l'attention des Allemands."
    "Vous entendez donc une cadences rapide de balles sifflé à coté de vos orreils,"
    "Malheureusement, votre nouvel ami se fait déchiré par les balles de la mitrailleuse."
    "Vous avez eu beaucoup de chance..."
    "Mais ce n'est pas le cas de ce soldat."
    "Sa tête s'est littéralement fait arraché,"
    "Son visage devenue un gruyère,"
    "Vous en trembler encore de peur"
    "Si vous cotoyer trop souvent les morts, vous risquez de predre rapidement foi."
    $ clock += 1
    

    if sanity < SANITY_MIN:
        "Alors que votre état mental était au plus bas,"
        "un sentiment de mal-être vous envahi petit à petit."
        "..."
        "Vous n'arrivez plus à disserner ce qui est vrai de ce qui ne l'est pas..."
        "Le réel de l'iréel..."
        "..."
        "Vous perdez complètement la raison ..."
        if not lostAudition:
            "..."
            SA "Die Feldgraue sind da! Die Feldgraue sind da!"
            SA "Hier!"
            "..."
            "Vous entendez une détonation ..."
        if not lostAudition:
            "..."
            SA "..."
            SA "..."
            "..."
            "Vous ressentez une détonation ..."
        "..."
        jump ENDING03
    if sanity > SANITY_MAX:
        if not lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "les bruit de vos pas retentiissent fortement autour de vous."
            "..."
            "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
            "vous amène à ne plus faire attention à votre environnement..."
            "..."
            "(bruit d'une détonation)"
            "..."
            jump ENDING04
        if lostAudition:
            "Alors que vous foncez déterminer à travert les tranchées,"
            "une idée merveilleuse vous viens alors à l'esprit,"
            "puisque rien ne peux vous tuer dans ce monde,"
            "il vous suffirait de vous montrer sur votre 31," 
            "pour que l'ennemie se montre par lui-même..."
            "..."
            jump ENDING04
    jump P00

label P00:
    $ previous = "P"
    $ clock += 1
menu:
    "SUD":
        jump O
    "OUEST":
        jump L

label ENDING01:
    "Vous avez été abattu par balle..."
    jump retry

label ENDING02:
    "Vous avez été tué par l'explosion d'un obus..."
    jump retry

label ENDING03:
    "Vous avez perdu la raison..."
    jump rety

label ENDING04:
    "Vous n'avez pas vu l'ennemi en fasse de vous..."
    "Vous avez été abattu par l'ennemi..."
    jump retry
label ENDING05:
    "Vous avez été transpersé par des balles,"
    "ennemie, ou alliée..."
    "Qui sais?"
    "..."
    jump retry
label ENDING06:
    "Vous vous êtes vidé de votre sang,"
    "dû à votre stupidité..."
    "..."
    "Avez-vous un QI négatif ?"
    "..."
    jump retry
return