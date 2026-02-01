# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define S = Character('Soldat', color="#0000ff")
define C = Character('Commandant', color="#0000ff")
define SA = Character('Soldat Allemand', color="#ff0000")
default povName = ""
define POV = Character ("[povName]")
default clock = 0
default isFirstIteration = True
define lostAudition = False

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


label start:
# Le jeu commence ici
    if isFirstIteration: 
    
        "Vous vous réveillez brusquement."
        "Vous avez du mal à vous souvenir de ces derniers moments."
        "Mais certains vous reviennent en mémoire."

        # cutscene du passé
        "Vous discutez tranquillement avec vos camarades."
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
            C "Vous serez une simple larve soldat dans mes rangs!"
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
            C "Vous serez une simple larve soldat dans mes rangs!"
            $ povName = "soldat"

        $isFirstIteration = False
        jump game
    if ! isFirstIteration:
        "Vous vous réveillez brusquement."
        "Vous avez du mal à vous souvenir de ces derniers moments."
        "Mais certains vous reviennent en mémoire."

        # cutscene du passé
        "Vous discutez tranquillement avec vos camarades."
        "Vos frères d'armes. "
        
        "..."
        "..."
        
        $ povName = "slodat"
        "..."
        "Vous voyez le commandant s'approcher de vous"
        C "Soldat, quel est votre mission ?"
        $ txtVar = ""
        $ missionEntrer = renpy.input(txtVar, length=150)
        if missionEntrer == "":
            C "Votre objectif de vie est d'être un incompétant à ce que je vois..."
            C "Jamais vu un soldat aussi inutile!"
            C "Soyez au moins aussi utile qu'une larve..."
            C "Pour la peine, vous serez une simple larve dans mes rangs soldat!"

        else:
            C "Votre mission me semble aussi inutile que votre avenir, mais peu importe..."
            C "Pour la peine, vous serez une simple larve dans mes rangs soldat!"
            
        jump game
label game:


    "La tranchée se divise en plusieurs directions..."
    "Où allons nous ?"

    # CHOIX DROITE OU GAUCHE
menu:
    "NORD":
        jump L 
    "EST": 
        jump O
    
label A: #Arty
    $ previous = "A"
    #if previous == 
    #   "Vous arrivez devant une sorte de porte"
    #    "Vous remarquez qu'il s'argie d'un bunker d'artillerie moyenne"
    #    ""
    
    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."

    if sanity < SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04

    $ clock += 1
menu:
    "NORD":
        jump B
    "SUD":
        jump F


label B: #Ammo

    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."
    
    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."

    if sanity < SANITY_MIN:
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
        " ..."
        "..."
        C "Est-ce que sa va soldat?!"
        "..."
        "À ces mots, vous prenez conscience de votre erreur ..."
        "Une balle vous a transpercé le ventre de part en part,"
        "Vous saignez abondamment ..."
        "..."
        jump ENDING05
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04

$ previous = "B"
$ clock += 1
menu:
    "SUD":
        jump A
    "EST":
        jump D



label C: #Garde-Mangé

    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."
    if clock >= 23 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Alors que vous êtes dans le garde-mangé,"
        "Un bruit couplé aux rats grouillant autour de vous se fait entendre..."
        "..."
        "Un simple bruit de métal tappant régulièrement contre la porte intallé à la hâte ..."
        "..."
        SA "Nun, nun, mein liebes kleines Französchen," 
        SA "das sich so gerne den Ratten zur Schau stellt!" 
        SA "Man erkennt hier deutlich das schlichte Gemüt des kleinen Gockels," 
        SA "der Sie nun einmal sind..." 
        SA "Erlauben Sie mir, Ihnen dabei behilflich zu sein," 
        SA "zu den Ihren zurückzukehren..."
        "..."
        SA "Sans pouvoir riposter, une détonation se fait entendre..."
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
        SA "Die Feldgraue sind da! Die Feldgraue sind da!"
        SA "Hier!"
        "..."
        "Vous entendez une détonation ..."
        "..."
        jump ENDING03
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04

$ previous = "C"
$ clock += 1
menu:
    "EST":
        jump F


label D: 

    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
        "Votre audition est assourdie pendant quelques secondes ..."
        if sanity < -60:
            "Vous commencez à faire une petite crise de panique ..."
            $ sanity -= 10
            "Votre santé mentale est encore plus basse ..."
    
    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."

    if clock >= 23 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
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

    if sanity < SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04
    
$ previous = "D"
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

    if isFirstIterationE == True:
        "Vous arrivez dans un lieu rempli d'histoire," 
        "les dernières traces du bunker ayant permis de 
        survivre sommairement aux attaques ayant surgi dans la zone" 
        "ont laissé place à un amas de débris jonchant le sol et les murs sommaires autour de vous."

        "Un homme est actuellement assis au au fond de l'impasse formé par les différents débris,"

        "son regard semble vide, mais avec une légère lueur d'espoir …"

        "Certains cadavres vous regardent encore… vous vous adressez à l'individu:"

    
    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous sentez de violante secousses" 
        "surevenu suite à l'explosion d'obus non loin de vous ..."
        "Votre audition est assourdie pendant quelques heures ..."
        $ clock += 5
        "Vous perdez l'audition"
        $ lostAudition = True

    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."
        
    if clock >= 23 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
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

    if sanity < SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04

$ previous = "E"
$ clock += 1 
menu:
    "SUD":
        jump D



label F:

    
    if clock == 6 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez un violant bruit d'explosion d'obus non loin de vous ..."
        "Votre audition est assourdie pendant quelques heures ..."
        $ clock += 2
        "Vous avez perdu l'audition."
        $ lostAudition = True
    
    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous sentez de violante secousses" 
        "surevenu suite à l'explosion d'obus non loin de vous ..."
        "Votre audition est assourdie pendant quelques heures ..."
        $ clock += 5

    if clock == 15 and sanity <= -60 and sanity >= -100:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."
    
    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."
    if clock >= 22 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
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

    if sanity < SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04
    
$ previous = "F"
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

    if clock == 6 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez un violant bruit d'explosion d'obus non loin de vous ..."
        "Votre audition est assourdie pendant quelques minutes ..."
        $ clock += 5
        "Vous avez perdu l'audition."
        $ lostAudition = True

    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
        "Votre audition est assourdie pendant quelques secondes ..."
        if sanity < -60:
            "Vous commencez à faire une petite crise de panique ..."
            $ sanity -= 10
            "Votre santé mentale est encore plus basse ..."
    
    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."
    
    if clock >= 23 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
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

    if sanity < SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04
    
$ previous = "G"
$ clock += 1  
menu:
    "NORD":
        jump H
    "SUD":
        jump F
    "EST":
        jump K


label H:

    if clock == 6 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez un violant bruit d'explosion d'obus non loin de vous ..."
        "Votre audition est assourdie pendant quelques minutes ..."
        $ clock += 5
        "Vous avez perdu l'audition."
        $ lostAudition = True

    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
        "Votre audition est assourdie pendant quelques secondes ..."
        if sanity < -60:
            "Vous commencez à faire une petite crise de panique ..."
            $ sanity -= 10
            "Votre santé mentale est encore plus basse ..."
    
    if clock == 8 and sanity >= 60 and sanity <= 100:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."
    
    if clock == 12 and sanity > -60 and sanity < 60:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."

    if clock >= 23 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
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

    if sanity < SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04
    
$ previous = "H"
$ clock += 1
menu:
    "NORD":
        jump I
    "SUD":
        jump G
    "OUEST":
        jump D

label I: 

    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."
    
    if clock >= 22 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
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

    if sanity < SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04

$ previous = "I"
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

    if clock == 6 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
        "Votre audition est assourdie pendant quelques secondes ..."
        if sanity < -60:
            "Vous commencez à faire une petite crise de panique ..."
            $ sanity -= 10
            "Votre santé mentale est encore plus basse ..."
    
    if clock == 8 and sanity >= 60 and sanity <= 100:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."
    
    if clock == 12 and sanity > -60 and sanity < 60:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."

    if clock >= 21 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
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

    if sanity < SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04
    
$ previous = "J"
$ clock += 1
menu:
    "NORD":
        jump K
    "OUEST":
        jump F
    "EST":
        jump N

label K: 
    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 15 and sanity <= -60 and sanity >= -100:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."

    if clock >= 22 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04

$ previous = "K"
$ clock += 1
menu:
    "SUD":
        jump J
    "OUEST":
        jump G

label L: 

    if clock == 4 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin le bruit d'une mitrailleuse lourde ..."
        
    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
        "Votre audition est assourdie pendant quelques secondes ..."
        if sanity < -60:
            "Vous commencez à faire une petite crise de panique ..."
            $ sanity -= 10
            "Votre santé mentale est encore plus basse ..."

    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."

    if clock >= 21 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
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

    if sanity < SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04
            
$ previous = "L"
$ clock += 1
menu:
    "NORD":
        jump P
    "SUD":
        jump O
    "OUEST":
        jump I

label M:

    if clock == 10 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
        "Votre audition est assourdie pendant quelques secondes ..."
        if sanity < -60:
            "Vous commencez à faire une petite crise de panique ..."
            $ sanity -= 10
            "Votre santé mentale est encore plus basse ..."
    
    if clock == 8 and sanity >= 60 and sanity <= 100:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."
    
    if clock == 12 and sanity > -60 and sanity < 60:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."
    
    if clock == 15 and sanity <= -60 and sanity >= -100:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."
    if clock >= 23 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
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

    
    if sanity < SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04

$ previous = "M"
$ clock += 1
menu:
    "SUD":
        jump I

label N:
    if clock >= 6 and clock < 20 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez siffler de plus en plus forte un objet dans le ciel ..."
        "Le tonnerre gronde et l'humanité vous foudroie de toute sa puissance."
        "Vous voyez alors,"
        "un obus arriver sur vous..."
        "à une vitesse dont nulle personne ne pourrait en réchapper."
        "Vous êtes frappé de plein fouet par l'explosion ..."
        "..."
        "Vous êtes mort."
        jump ENDING02
    if clock >= 20 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Les bombardements d'obus se sont arrêtés depuis peu,"
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
    if sanity < SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04


$ previous = "N" 
$ clock += 1   
menu:
    "NORD":
        jump O
    "OUEST":
        jump J

label O: 
    
    if clock == 6 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez brusquement le bruit d'un obus exploser non loin de vous ..."
        "Votre audition est assourdie pendant quelques secondes ..."
        if sanity < -60:
            "Vous commencez à faire une petite crise de panique ..."
            $ sanity -= 10
            "Votre santé mentale est encore plus basse ..."

    if clock == 12 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

    if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez au loin un coup de feu au loin ..."
        "..."

    if clock >= 20 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
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

    if sanity < SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04

$ previous = "O"
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
        "Vous entendez au loin un bruit de sifflet ..."
        "..."
        "Les allemand arrivent."
        "..."

if clock == 18 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
        "Vous entendez un coup de feu proche de vous ..."
        "..."

if clock >= 20 and clock <= 25 and sanity <= SANITY_MAX and sanity >= SANITY_MIN:
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
# CHOIX
if sanity <= SANITY_MAX and sanity >= SANITY_MIN:
    "Vous vous approchez et vous voyez un soldat."
    "Ce soldat fonce brusquement sur vous et criant"
    S "QU'ATTENDEZ VOUS POUR TIREZ ?"
    S "LES ALLEMANDS SONT LÀ, ILS ARRIVENT!!!"
    if clock < 12:
        "Vous le regardez surpris, vous ne pensiez pas que les allemands attaquerait déjà"
    if clock >= 12:
        "Le bruit de sifflet aurait-il été faux ?"
    # CHOIX REGARDER/TIRER/NE RIEN FAIRE
menu : 
    "...":
        jump P_1
    "Regarder l'ennemi venir":
        jump P_2
    "Tirer avec le soldat":
        jump P_3
label P_1:
    S "Tu ne tires pas ?"
    S "Très bien... Tu es un déserteur en quelque sorte..."
    S "Ne m'oblige pas à te tuer..."
    S "Les ordres sont pourtant claire..."
    S "Tout deserteur doit être abattue immédiatement!"
    jump ENDING01

label P_2:
    "Vous monter très toucement l'echelle."
    "Au moindre bruit, les allemands pourrait être alerté."
    "Un seul bruit et votre vie oté, servant de repas au rat."
    # PARANOIA PEUT FOIRER ?
    "Heureusent, vous avez réussi à vous faire discret."
    "Mais malheureusement,"
    "Vous ne voyez aucun soldat à l'horizon."
    "Seulement les fortifications au loin,"
    "Votre nouvel ami semble faire une paranoia."
    "Un phénomène courant dans les tranchers,"
    "Des crises de nerds déclenchable à cause d'un haut taux d'horreur."
    "Ce qui peut provoquer des hallucinations"
    "Vous lui faite donc par de son hallucination"
    "Mais ne veux malheureusement rien entendre et commence à ouvrir le feu"
    $ clock += 1
    

    if sanity < SANITY_MIN:
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
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04
    jump P00
label P_3: 
    "Vous répondez positivement à l'appel!"
    S "AH! Voilà un bon soldat !"
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
        "..."
        S "Die Feldgraue sind da! Die Feldgraue sind da!"
        S "Hier!"
        "..."
        "Vous entendez une détonation ..."
        "..."
        jump ENDING03
    if sanity > SANITY_MAX:
        "Alors que vous foncez déterminer à travert les tranchées,"
        "les bruit de vos pas retentiissent fortement autour de vous."
        "..."
        "Le bruit de la boue mélé au bruit de divers coup de feu au loin,"
        "vous amène à ne plus faire attention à votre environnement..."
        "..."
        "(bruit d'une détonation)"
        "..."
        jump ENDING04
    jump P00

label P00:
$ clock += 1
menu:
    "SUD":
        jump O
    "OUEST":
        jump L

label ENDING01:
    "Vous avez été abattu par balle..."

label ENDING02:
    "Vous avez été tué par l'explosion d'un obus..."

label ENDING03:
    "Vous avez perdu la raison, la mort ou chichi..."

label ENDING04:
    "Vous n'avez pas vu l'ennemi en fasse de vous..."
    "Vous avez été abattu par l'ennemi..."
label ENDING05:
    "Vous avez été transpersé par des balles,"
    "ennemie, ou alliée..."
    "Qui sais?"
    "..."
label ENDING06:
    "Vous vous êtes vidé de votre sang,"
    "dû à votre stupidité..."
    "..."
    "Avez-vous un QI négatif ?"
    "..."
return