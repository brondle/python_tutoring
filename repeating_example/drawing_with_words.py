from random import randint, random, choice

ee = "E E Cummings, often styled as e e cummings, as he is attributed in many of his published works, was an American poet, painter, essayist, author, and playwright. He wrote approximately 2,900 poems, two autobiographical novels, four plays, and several essays. He is often regarded as one of the most important American poets of the 20th century. Cummings is associated with modernist free-form poetry. Much of his work has idiosyncratic syntax and uses lower case spellings for poetic expression."
ee_list = ee.split()

alan = "Cumming began his theatre career in his native Scotland, performing in seasons with the Royal Lyceum Edinburgh, Dundee Rep, The Tron Glasgow and tours with Borderline, Theatre Workshop, and Glasgow Citizens' TAG. He played Slupianek in the Traverse Theatre, Edinburgh's 1988 production of Conquest of the South Pole, which later transferred to the Royal Court in London and earned him an Olivier Award nomination as Most Promising Newcomer. He went on to perform plays with the Bristol Old Vic and the Royal Shakespeare Company and played Valere in La Bete at the Lyric, Hammersmith, London. In 1991 he played The Madman in the 1990 Royal National Theatre production of Accidental Death of an Anarchist by Dario Fo, for which he won the Laurence Olivier Award for Best Comedy Performance.[17][18][19] He also adapted the play with director Tim Supple. In 1993 he received great critical acclaim and the TMA Best Actor award for playing title role in the 1993 English Touring Theatre's Hamlet (playing opposite his then-wife, Hilary Lyon, in the role of Ophelia).He played the role of The Master of Ceremonies in Sam Mendes's 1993 revival of the musical Cabaret in London's West End opposite Jane Horrocks as Sally Bowles. He received an Olivier Award nomination for Best Actor in a Musical. He reprised the role in 1998 for the Mendes-Rob Marshall Broadway revival, this time opposite Natasha Richardson as Sally Bowles. He won a Tony Award, Drama Desk Award, and Outer Critics Circle Award for his performance."
al_list = alan.split()

em =' '
dir = 1
for i in range(30):
    # m = i*2
    if i < 11:

        # print('this_dir is ', this_dir, 'i is ', i)
        print(em*i,'not the end' )
    elif i < 21:
        z = i%10
        op = -1*(z+z)
        this_dir = i+op #is there a smarter way to do this?
        if z == 0:
            this_dir = 0
            # print('this direction is ', this_dir, 'i is ', i, 'z is ', z, 'op is ', op)
            print('not the end')
        else:
            # print('this direction is ', this_dir, 'i is ', i, 'z is ', z, 'op is ', op)
            print(em * this_dir, 'not the end')
#what would be a better way of handling this that could deal with different scenarios
#how to address the two empty space jump in the last line?



