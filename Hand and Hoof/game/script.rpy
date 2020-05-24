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


#Background images
image shell_office = "shell_office_png.png"

#Stats
define money = 3000
define mon_made = 0 #money you make through the course of the game
define char = 1 #charisma: more likely to recieve a positive interaction from NPCs
define bond = 1 #bond: how much your horse trusts you; bonus to your horsemanship skills; can be gained through riding and/or taking care of your horse
define horship = 1 #horsemanship: better equestrian skills; you understand your horse more
define stab_care = False #stable care: a stablehand takes care of your horse every morning and evening, leaving you with more time for other activities
define new_follow = horship * char #amount of followers you gain from social media posts
define tot_follow = 0 #amount of followers you have total
define income = 10 * tot_follow #once you hit 40 followers on social media, you gain daily income

#Facts List
define rand_post = renpy.random.choice(["Curry combing is most effective when you brush your horse's coat in circles opposite of the direction of the horse's hair.", "Ragwort is a tall plants with bright yellow flowers. This plant will fatally poison the livers of horses who eat them so make sure to remove them from the range of any of your equine friends."])

#Tasks List
define r1 = "Need someone to take video while I train."
define l1 = "Going out on a trail ride. Need a buddy to ride with me for safety reasons."
define k1 = "Have you seen my leadrope? It’s made of polyester and it’s the color pink."
define task_list = [r1, l1, k1]

# The game starts here.

label start:
label pre_chap1:
    #asking player for name
    #pfn = player first name
    #pmn = player middle name
    #pln = player last name

    menu:
        "Choose a bonus."

        "Charisma":
            $ char = 3
        
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

label chap1:
    # Chapter 1: 
    scene shell_office
    
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
            $ stab_care = True
            $ money -= 1000

        "No":
            $stab_care = False
    
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
    
    menu: 
        "Attempt jumping that cross rail?"

        "Yes":
            if horship < 3:
                $ jump_success = renpy.random.ranint(1,100)
                if $ jump_success < 11:
                    $ jump_successful = True
                    jump successful_jump
                else:
                    $ jump_successful = False
                    jump unsucc_jump
            else:
                $ jump_successful = True
                jump successful_jump
        "No":
            jump no_jump
    
    label no_jump:
        n "{i}You continue your trotting and cantering exercises, often steering off from the rail when necessary to avoid crashing into the other rider.{/i}"
        n "{i}After a while, you see the other rider slow down then stop.{/i}"
        jump raki_exit

    label successful_jump:
        $ horship += 2
        n "{i}You direct [hn] head on in the direction of the cross rail.{/i}"
        n "{i}Look directly ahead of you and lift yourself off of the saddle ahead of time, you remember.{/i}"
        n "{i}Once you two arrive right at the cross rails, you can feel [hn] lift [hpf] front legs.{/i}"
        n "{i}Fortunately, the amount of leaning forward in your saddle is sufficient to keep you balanced.{/i}"
        n "{i}You scale back on your lean a little bit as your horse's hooves reach the ground again and canter onward.{/i}"
        n "{i}You steer [hn] away from the other jumps and ask [hof] to slow down to a trot.{/i}"
        jump raki_react

    label unsucc_jump:
        $ horship += 1
        n "{i}You direct [hn] head on in the direction of the cross rail.{/i}"
        n "{i}You look right at the jump itself, even as [hn] draws nearer and nearer to it.{/i}"
        n "{i}You continue absorbing the motion of the canter in your seat as well.{/i}"
        n "{i}Only right when [hn] is lifting [hpf] hooves off of the ground do you lean forward.{/i}"
        n "{i}The landing feels a bit jarring and you lean more towards the front than necessary.{/i}"
        n "{i}Next thing you know, your feet slip out of their stirrups, the laws of physics prodding your form sideways.{/i}"
        n "{i}You grab a bit of [hn]'s mane in vain, letting go of it as soon as most of your body slips onto one side.{/i}"
        n "{i}Ultimately, you fall onto the arena padding, your horse slowing to a trot then walk and circling back to you.{/i}"

    label raki_react:
        if jump_successful  == True:
            n "{i}You notice that the other rider is at a standstill.{/i}"
            n "{i}Undoubtedly, he is looking right at you with his piercing gaze.{/i}"
            n "{i}However, his lips are curving into a small smile.{/i}"
            n "{i}Whether this smile is genuine congrats of your little victory or a mockery of how amusingly unimpressive your attempt was is undiscernable.{/i}"
            raki "{i}Impressive.{/i}"
            menu: 
                "{i}With a response like that, it's even harder to tell.{/i}"

                "Was that supposed to be sarcastic?":
                    n "{i}The other rider looks a bit taken aback by your response.{/i}"
                    n "{i}Uh oh. Perhaps he meant to be sincere after all.{/i}"
                    n "{i}His lips curl into something like a frown.{/i}"
                    if char == 3:
                        player "Wait! I'm sorry. I take that back!"
                        player "Thanks. I don't think it's that impressive though."
                        raki "No worries. You are not the first person to mix up my ironic statements with my genuine ones after all."
                        n "{i}You swear that for a second, you can see a sad gleam in his eyes.{/i}"
                        n "{i}Before you can confirm, he smiles and intensifies his gaze again, clearing it of the emotions on it from seconds ago.{/i}"
                        jump raki_exit
                    else:
                        jump raki_exit

                "Thanks.":
                    $ char += 1
                    player "{i}It was only a cross rail though.{/i}"
                    player "{i}I'm sure you could do much better than me.{/i}"
                    n "{i}A blank stare washes over his face for a moment.{/i}"
                    n "{i}Then all too quickly, his expression erupts into a languid countenance.{/i}"
                    raki "{i}Bold of you to assume I know how to jump.{/i}"
                    jump raki_exit

        if jump_successful == False:
            n "{i}You stand up and grab [hn]'s reins.{/i}"
            n "{i}Fortunately, there happens to be a mounting block nearby so you lead your horse over to it.{/i}"
            raki "{i}*laughs*{/i} Oh my goodness. Did you even learn how to jump?"
            n "{i}You look back at the source of the voice to find the other rider's once scarily composed facial expression loosened into a nearly complete smirk.{/i}"
            menu: 
                "{i}How do you respond to his reaction?{/i}"

                "Hey, that's rude!":
                    raki "My apologies then."
                    jump raki_exit
                
                "Well, I got to mess up sometimes to be on the path to success.":
                    $ char += 1
                    raki "“I suppose that’s true, but you don’t want that to happen to you too often. {i}*laughs*{/i}"
                    player "Hopefully it won't."
                    n "{i}The other rider doesn't say anything. He only smiles in good-humour.{/i}"

    label raki_exit: 
        n "{i}Then with a subtle swipe of his heels, his horse walks in the direction of the gate.{/i}"
        n "{i}Once he arrives there, he finds another rider standing outside already opening it.{/i}"
        n "{i}She lets herself in and the other one out.{/i}"
        n "{i}She looks in your direction and you recognize her as Kaia!{/i}"
        n "{i}Kaia approaches you with a gentle but grand smile on her face.{/i}"
        kaia "So have you gotten to meet Raki?"
        player "Is he the guy who was just in here with me?"
        kaia "He is."
        kaia "Hopefully he didn't give you too much trouble."
        kaia "He's not the most sociable person in the world, but he's a very nice one once you get to know him."
        kaia "Also if you can spare time to help out our staff and riders, check out the bulletin board to see what tasks need to be done."
        kaia "They will always reward you with something in return."
        player "I see."
        kaia "Anyway, Jolyne here has been waiting all day for this ride. {i}*stroke's her horse's mane*{/i}"
        kaia "So, I'll see you later?"
        player "Yeah. I was just about to head out."
        player "See ya!"
        kaia "Bye!"
        n "{i}You head towards the gate to open it and let yourself out.{/i}"
        n "{i}You and [hn] take an easy walk to [hpf] stall.{/i}"
        n "{i}After untacking your horse, you give [hof] a few affectionate strokes on the neck.{/i}"
        if stab_care == True:
            n "{i}Then you head home.{/i}"
        else:
            $ bond += 1
            n "{i}Then you spend some time making sure [hn] has [hpf] feed and water prepared.{/i}"
            n "{i}Afterwards, you head home.{/i}"
        n "{i}You arrive at the doorstep of your humble abode.{/i}"
        menu:
            "What will you do?"

            "Read {i}The Art of Charm{/i}":
                n "{i}You pick up this book and sit down to read it.{/i}"
                if stab_care == True:
                   $ char += 2
                else:
                   $ char += 1

            "Read {i}The Rider's Guide to Everything Equine{/i}":
                n "{i}You pick up this book and sit down to read it.{/i}"
                if stab_care == True:
                   $ horship += 2
                else:
                   $ horship += 1

            "Blog about the equine world.":
                n "{i}You head to your laptop, log onto YouBlog, and start writing away.{/i}"
                n "{i}Once you are down writing, the post reads as follows:{/i}"
                player "{i}[rand_post]{/i}"
                if stab_care == True: 
                    player "{i}For more information on this topic. Click on the 'Read more' button!{/i}"
                    $ new_follow = 2 * new_follow
                player "{i}I hope you enjoyed reading this!{/i}"
                $ tot_follow = new_follow
                n "{i}In the coming minutes after you post your entry, you get the notfication that your profile has gained [new_follow] followers, which makes for a total of [tot_follow] followers!{/i}"
        n "{i}The sky had been dark for some time now and you feel your tiredness creep onto you.{/i}"
        n "{i}It is time to go to bed and start a new day.{/i}"

label chap2:
    label morning:
        n "{i}The sun rises and its rays permeate throughout your room.{/i}"
        n "{i}You get up and prepare yourself for the new day ahead.{/i}"
        menu:
            "What will you do?"

            "Read {i}The Art of Charm{/i}":
                n "{i}You pick up this book and sit down to read it.{/i}"
                if stab_care == True:
                    $ char += 2
                else:
                    $ char += 1

            "Read {i}The Rider's Guide to Everything Equine{/i}":
                n "{i}You pick up this book and sit down to read it.{/i}"
                if stab_care == True:
                    $ horship += 2
                else:
                    $ horship += 1

            "Blog about the equine world.":
                n "{i}You head to your laptop, log onto YouBlog, and start writing away.{/i}"
                n "{i}Once you are down writing, the post reads as follows:{/i}"
                player "{i}[rand_post]{/i}"
                if stab_care == True: 
                    player "{i}For more information on this topic. Click on the 'Read more' button!{/i}"
                    $ new_follow = 2 * new_follow
                player "{i}I hope you enjoyed reading this!{/i}"
                $ tot_follow = new_follow
                n "{i}In the coming minutes after you post your entry, you get the notfication that your profile has gained [new_follow] followers, which makes for a total of [tot_follow] followers!{/i}"
        n "{i}It is about time to see [hn] so you head on over to Green Rain Ranch.{/i}"
        label at_ranch: 
            n "{i}You arrive at the ranch. [hn] greets you with a pleasant nicker.{/i}"    
            if stab_care == False: 
                $ bond += 1
                n "{i}You feed and groom your horse, making [hof] feel very happy!{/i}"
            menu: 
                "What will you do?"

                "Go for a ride":
                    $ bond += 1
                    n "{i}You groom and tack up [hn].{/i}"
                
                "Go into the office":
                    n "{i}You walk across the parking lot and into the office.{/i}"
                    n "{i}You turn around to see the bulletin board with various notes pinned to it.{/i}"
                    menu: 
                        "Which task will you accept?"

                        "[r1]":
                            raki "{i}[r1]{/i}"

                        "[l1]":
                            lune "{i}[l1]{/i}"
                        
                        "[k1]":
                            kaia "{i}[k1]{/i}"


return
