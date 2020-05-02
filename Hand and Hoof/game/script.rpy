#Hand and Hoof 
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

#Characters
define n= Character("")
define player = Character("[pn]")
define dev = Character("Developer")
define shell = Character("Shelley")
define horse = Character ("[hn]")
define lune = Character("Lune")
define raki = Character("Raki")
define kaia = Character("Kaia")
define mere = Character("Meredith")

#Pronouns
#sfc = subject form with capital at beginning (She, He, They)
#sfl = subject form in all lowercase (she, he, they)
#pf = possessive form (her, his, their)
#pfc = possessive form with capital at beginning (Her, His, Their)
#verb (is, are)
#of = object form (her, him, them)
#add an 'h' in front of every pronoun-form to refer to the horse

#Name lists
define jojo_names = ["Jotaro", "Kakyoin", "Kakyouin", "Jojo", "Josuke", "Jousuke", "Koichi", "Kouichi", "Okuyasu", "Jolyne", "Jonathan", "Joseph", "Dio", "Giorno", "Yasuho", "Joshu", "Joshuu", "Jobin", "Joubin", "Narancia,", "Fugo", "Abbachio", "Bucciarati", "Pannacotta", "Mista", "Guido", "Trish"]

#Character images


#Stats
define money = 3000
define char = 1 #charisma: more likely to recieve a positive interaction from NPCs
define art = 1 #artistic ability: higher quality drawings/paintings/photos and more flexibility for expressing yourself 
define horship = 1 #horsemanship: better equestrian skills; you understand your horse more
define stab_care = False #stable care: a stablehand takes care of your horse every morning and evening, leaving you with more time for other activities
define ar_pri = art * 3

# The game starts here.

label start:

    #asking player for name
    #pfn = player first name
    #pmn = player middle name
    #pln = player last name

    menu:
        "Choose a bonus."

        "Charisma":
            $ char = 3
        
        "Artistic ability":
            $ art = 3
        
        "Horsemanship": 
            $ horship = 3

        "Money":
            $ money = 5000

    $ pn = renpy.input("What is your name?")
    if pn == "":
        $ pn = "Blair"

    if pn in jojo_names:
        dev "Oho! I see what you did there!"

    menu:
        "What are your pronouns?"

        "They/them":
            $ sfc = "They"
            $ sfl = "they"
            $ verb = "are"
            $ pf = "their"
            $ of = "them"
        "She/her":
            $ sfc = "She"
            $ sfl = "she"
            $ verb = "is"
            $ pf = "her"
            $ of = "her"
        "He/him":
            $ sfc = "He"
            $ sfl = "he"
            $ verb = "is"
            $ pf = "his"
            $ of = "him"

    # Chapter 1: 
    
    shell "Hi there! I haven't seen you here before. Are you new to this town?"
    player "Yup!"
    shell "Well, you're going to love it here - especially if you're a horse person! My name is Shelley by the way."
    player "Pleased to meet you! I'm [pn]."
    shell "Are you here to buy a horse?"
    player "Yes I am!"
    shell "Then you're at the right place!"
    shell "Come now, I'll show you all the beauties that are ready to be adopted!"
    n "{i}Shelley takes you on a short walk out of the office and through the stables, guiding you to the section with horses for sale.{/i}"
    n "{i}In a short notice she stops in her tracks and points to two stalls, each with a horse in them.{/i}"
    shell "The selections this time around are very limited and I'm sorry for that."
    shell "Fortunately, the horses we do have on sale are well-behaved and well-trained in the commands of a rider."
    shell "These horses are twins! They're names are Rosie and Dante but you are free to change the name of whichever one you choose."

    menu:
        shell "Which horse do you want to adopt?"

        "Rosie":
            $ hsfc = "She"
            $ hsfl = "she"
            $ hverb = "is"
            $ hpf = "her"
            $ hpfc = "Her"
            $ hof = "her"

            shell "All right!"
            shell "Why don't you take [hof] on a test ride and see what you think?"
            n "{i}Shelley prepares Rosie's tack and you mount [hof].{/i}"
            n "{i}She then points you to a riding ring nearby and goes over to open the gate for you.{/i}"
            n "{i}You spend quite a bit of time riding around in the ring with Rosie.{/i}"
            n "{i}[hpfc] trot is a little bouncy but it's nothing you can't handle. [hpfc] canter feels amazing!{/i}"
            n "{i}After your test ride is over, you ride out of the gate and dismount.{/i}"
            n "{i}You hold onto one rein as you stand next to Shelley.{/i}"
            shell "I'll get all the papers ready and I just have a few questions for you."
            n "{i}She heads back to the office and comes back with some papers.{/i}"
            shell "First of all, are you aware that it is within our legal ability to seize your horse if you do not take care of her?"
            player "Yes."
            shell "Will you be keeping your horse on your own property or are you planning to board her somewhere?"
            player "Boarding. I have already chosen a place for her."
            
            menu: 
                shell "Excellent! Now for one final question. Do you wish to change her name?"

                "Yes.":
                    $ hn = renpy.input("What will you name her?")

                    if hn == "":
                        $ hn = "Lucilia"

                    if hn in jojo_names:
                        dev "Niicceee!"
                
                "No.":
                    $ hn = "Rosie"
            
        "Dante":
            $ hsfc = "He"
            $ hsfl = "he"
            $ hverb = "is"
            $ hpf = "his"
            $ hof = "him"

            shell "All right!"
            shell "Why don't you take [hof] on a test ride and see what you think?"
            n "{i}Shelley prepares Dante's tack and you mount [hof].{/i}"
            n "{i}She then points you to a riding ring nearby and goes over to open the gate for you.{/i}"
            n "{i}You spend quite a bit of time riding around in the ring with Dante.{/i}"
            n "{i}[hpfc] trot is a little bouncy but it's nothing you can't handle. [hpfc] canter feels amazing!{/i}"
            n "{i}After your test ride is over, you ride out of the gate and dismount.{/i}"
            n "{i}You hold onto one rein as you stand next to Shelley.{/i}"
            shell "I'll get all the papers ready and I just have a few questions for you."
            n "{i}She heads back to the office and comes back with some papers on a clipboard and a pen.{/i}"
            shell "First of all, are you aware that it is within our legal ability to seize your horse if you do not take care of him?"
            player "Yes."
            shell "Will you be keeping your horse on your own property or are you planning to board him somewhere?"
            player "Boarding. I have already chosen a place for him."

            menu: 
                shell "Excellent! Now for one final question. Do you wish to change his name?"

                "Yes.":
                    $ hn = renpy.input("What will you name him?")

                    if hn == "":
                        $ hn = "Merlin"

                    if hn in jojo_names:
                        dev "Nice!"
                
                "No.":
                    $ hn = "Dante"

    shell "All right! Let me write all of this down."
    n "{i}With her pen, Shelley transcribes what you just said on the papers she brought.{/i}"
    n "{i}She hands over the clipboard to you. The first paper you see is completely blank, save for Shelley's signature at the bottom.{/i}"
    shell "You just need to fill this out and you're all good to go!"
    n "{i}You write down your name and everything else the document requires. Once you finish, you try hand it back to Shelley.{/i}"
    n "{i}She takes it, but opens up the clip and peels the paper you just wrote on, revealing a yellow version of the exact same paper.{/i}"
    n "{i}It even came with all of your writing and her signature. Wow, how convenient!{/i}"
    n "{i}She hands the first version over to you.{/i}"
    shell "Here. This is for you to keep!"
    n "{i}After you two settle all the legal matters, Shelley takes [hn] out of [hpf] stall and walks [hof] to a trailer. Afterwards, she leads you to the truck attached to it.{/i}"
    n "{i}She opens the door to the passenger side for you.{/i}"
    shell "Why don't you hop on in?"
    n "{i}You climb in and sit down while Shelley walks around to the other side and climbs in herself.{/i}"
    n "{i}Shelley powers on her truck and starts backing up.{/i}"
    shell "To Green Rain Ranch we go!"
    n "{i}You and Shelley are on the road for about 10 minutes.{/i}"
    n "{i}Then you spot a welcome sign on the right side of the road and Shelley turns the vehicle into the road where it stands.{/i}"
    n "{i}The two of you head down that road for another couple of minutes.{/i}"
    n "{i}You see the vast grassy hills with some horses on them, stalls and barns, and riding rings out of the window.{/i}"
    n "{i}Soon enough, the truck parks and the main office building is in your view.{/i}"
    n "{i}You climb out and walk into the office.{/i}"
    n "{i}A young woman is sitting behind the desk with a cheerful expression on her face.{/i}"
    kaia "Hello! Are you the new boarder, [pn]? I'm Kaia by the way."
    player "Yes, I am! It's nice to finally meet you."
    kaia "The pleasure is all mine! Did you bring your horse?"
    player "I did and [hsfl] is waiting in the parking lot as we speak."
    kaia "Perfect! I'll meet you in the parking lot and I can show you [hsfl] new stall!"
    n "{i}You walk out of the door just as Kaia gets up and strides over to the trailer, where Shelley is opening it and putting a halter on [hn].{/i}"
    horse "{i}*whinny*{/i}"
    shell "That's a good horse!"
    shell "Ah! [pn], there you are!"
    shell "Your horse is ready to see [hpf] new stall!"
    n "{i}She hands the lead rope to you with a gentle smile.{/i}"
    n "{i}She goes inside the trailer and comes back out with a tack trunk.{/i}"
    shell "Here."
    n "{i}Shelley hands you the trunk.{/i}"
    player "Thanks!"
    shell "I gotta head back so I'll see you around, [pn]!"
    player "Bye, Shelley!"
    kaia "Shall I show you where [hn] is going to live?"
    player "Please lead the way!"
    n "{i}As Shelley hops back into her truck and starts it, Kaia motions you to follow her.{/i}"
    n "{i}She points to an empty stall on the other side of the parking lot as the two of you walk there.{/i}"
    n "{i}Once you arrive at the stall, she opens the stall door for you and you lead [hn] in there.{/i}"
    n "{i}You remove [hpf] halter and give [hof] a gentle stroke on the neck before leaving the stall.{/i}"
    n "{i}As you and Kaia watch your horse happilly explore [hpf] new home with [hpf] springy trot,{/i}"
    n "{i}you hear footsteps and the sound of rolling wheels along the dirt path next to the stables.{/i}"
    n "{i}The two of you look away to see a young woman pulling a wheelbarrow full of soiled bedding and mucking tools.{/i}"
    kaia "Oh hi, Lune!"
    lune "Hey, Kaia! How's it going?"
    kaia "It's all right. Oh, by the way, Lune. This is [pn], the new boarder! [pn], this is Lune, only one of our most hardworking and excellent stablehands!"
    lune "Oh jeez Kaia, you flatter me too much!"
    lune "Anyway, hi [pn]! I take care of the horses around here. Well the horses for the ones that pay an additional fee to their boarding cost."
    player "How much is the cost?"
    lune "A flat fee of 1000 dollars. It a little expensive I know."
    player '{i}A "little" expensive.{/i}'
    lune "But that covers the cost of everything from mucking stalls to grooming to feeding!"
    lune "Plus that money helps us preserve the beauty of this land and repair and upgrade our facilities when needed!"

    menu:
        "Arrange stable care?"

        "Yes":
            player "I'd like to arrange stable care for [hn], please."
            kaia "Oh perfect, we can make that happen!"
            n "{i}You pull out a check and a pen and scribbe the details you need.{/i}"
            n "{i}You hand it to Kaia, who inspects it before nodding of approval.{/i}"
            kaia "All set! Starting now, we will take care of your [hn] for you!"

        "No":
    
    lune "Anyway, I got to go! There are many more horses who need my services."
    lune "I'll see you around, [pn]?"
    player "Yeah. See you, Lune!"
    kaia "Bye Lune!"
    lune "Bye Kaia! See you later, [pn]!"
    n "{i}Wheelbarrow in her grip, she strolls past the two of you.{/i}"
    kaia "Anyway, I got to go myself. If you got any questions, feel free to reach out to me!"
    kaia "It was nice meeting you, [pn]!"
    player "It was nice meeting you, too! See you later, Kaia!"
    n "{i}Kaia waves at you and she walks back across the parking lot to the office.{/i}"
    n "{i}You turn to face the stall to see [hn] standing right in front of you.{/i}"
    n "{i}You gentely stroke [hpf] head and poke [hof] on the snout.{/i}"
    n "{i}In response, [hn] perks [hpf] ears up and forward and moves shoves [hpf] muzzle in your hand.{/i}"
    player "Hey! {i}*laughs*{/i}"
    n "{i}Suddenly aware of the weight of the trunk you carry in your other hand, an idea pops in your head.{/i}"
    player "Hey, [hn]. Let's go on another ride!"
    n "{i}You place the trunk on the ground and open up the lid.{/i}"
    n "{i}Inside there is [hpf] saddle, saddlepad, bridle, and various grooming supplies.{/i}"
    player "Wow, Shelley has been real generous hasn't she?"
    n "{i}You put [hn] in [hpf] halter and start tacking [hof] up.{/i}"
    n "{i}Once [hsfl] is all tacked up, you lead [hof] to the nearest mounting block in the parking lot and get on [hpf] back.{/i}"
    n "{i}You and [hn] walk at a slow and steady pace past the main office building.{/i}"
    n "{i}You spot a large riding arena some distance away and continue your march towards it.{/i}"
    n "{i}Upon closer inspection, you realize that the arena is empty save for a few jumping obstacles and one rider with a horse pacing along at a quick march.{/i}"
    n "{i}You open the gate to let yourselves in and [hn] starts pacing as well.{/i}"
    n "{i}After walking a few laps around the arena, you press your heels into [hn]'s sides, asking for a trot.{/i}"
    n "{i}Just as your horse takes the first few steps of a trot, the other rider turns around and passes right behind you at a trot much brisker than [hn]'s.{/i}"
    raki "..."
    player "{i}Whoa, scary!{/i}"
    n "{i}Even though the other rider is opposite from you in the arena at this point, you cannot shake the feeling that his gaze is still on you.{/i}"
    n "{i}Perhaps he is trying to silently intimidate you into leaving the arena or maybe he's just uncomfortably curious about the newcomer.{/i}"
    n "{i}Regardless, you have a right to be here as much as he does so you and [hn] trot on, winding up to canter.{/i}"
    n "{i}As you canter along the rail, getting off of it when you need to pass the other rider, your eyes keep darting back and forth to a cross rail jump in the middle of the arena.{/i}"
    '''
    menu: 
        "Attempt jumping that cross rail?"

        "Yes":
    '''
    
label successful_jump:
    n "{i}You direct [hn] head on in the direction of the cross rail.{/i}"



    return
