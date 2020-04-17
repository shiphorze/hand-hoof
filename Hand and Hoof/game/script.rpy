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
#verb (is, are)
#of = object form (her, him, them)
#add an 'h' in front of every pronoun-form to refer to the horse

#Name lists
define jojo_names = ["Jotaro", "Kakyoin", "Kakyouin", "Jojo", "Josuke", "Jousuke", "Koichi", "Kouichi", "Okuyasu", "Jolyne", "Jonathan", "Joseph", "Dio", "Giorno", "Yasuho", "Joshu", "Joshuu", "Jobin", "Joubin"]

#Character images


#Inventory
define money = 400

# The game starts here.

label start:

    #asking player for name
    #pfn = player first name
    #pmn = player middle name
    #pln = player last name

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
        shell "Which horse will you adopt?"

        "Rosie":
            $ hsfc = "She"
            $ hsfl = "she"
            $ hverb = "is"
            $ hpf = "her"
            $ hof = "her"

            shell "All right!"
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
                        dev "Niicceee!"
                
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
            n "{i}I walk out of the door just as Kaia gets up and stride over to the trailer, where Shelley is opening it and putting a halter on [hn].{/i}"
            horse "{i}*whinny*{/i}"



    return
