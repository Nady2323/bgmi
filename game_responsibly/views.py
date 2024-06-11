from django.shortcuts import render



video_games = [
    {
        "id":1,
        "title": "The Witcher 3: Wild Hunt", 
        "genre": "Action RPG", 
        "platform": "PC, PS4, Xbox One",
        "description": '''The Witcher 3: Wild Hunt[b] is a 2015 action role-playing game developed and published by CD Projekt. It is the sequel to the 2011 game The Witcher 2: Assassins of Kings and the third game in The Witcher video game series, played in an open world with a third-person perspective. The games follow the Witcher series of fantasy novels written by Andrzej Sapkowski.

The game takes place in a fictional fantasy world based on Slavic mythology. Players control Geralt of Rivia, a monster slayer for hire known as a Witcher, and search for his adopted daughter, who is on the run from the otherworldly Wild Hunt. Players battle the game's many dangers with weapons and magic, interact with non-player characters, and complete quests to acquire experience points and gold, which are used to increase Geralt's abilities and purchase equipment. The game's story has three possible endings, determined by the player's choices at key points in the narrative.

Development began in 2011 and lasted for three and a half years. Central and Northern European cultures formed the basis of the game's world. The game was developed using the REDengine 3, which enabled CD Projekt to create a complex story without compromising its open world. The music was primarily composed by Marcin Przybyłowicz and performed by the Brandenburg State Orchestra.

The Witcher 3: Wild Hunt was released for PlayStation 4, Windows, and Xbox One in May 2015, with a Nintendo Switch version released in October 2019, and PlayStation 5 and Xbox Series X/S versions titled The Witcher 3: Wild Hunt - Complete Edition which was released in December 2022. The game received critical acclaim, with praise for its gameplay, narrative, world design, combat, and visuals, although it received minor criticism due to technical issues. It holds more than 200 game of the year awards and has been cited as one of the greatest video games ever made. Two expansions were also released to critical acclaim: Hearts of Stone and Blood and Wine. A Game of the Year edition was released in August 2016, with the base game, expansions and all downloadable content included. The game has sold over 50 million units as of March 2023, making it one of the best-selling video games of all time.''',
        },
    {
        "id":2,
        "title": "Legend of Zelda: Breath of the Wild", 
        "genre": "Action-adventure", 
        "platform": "Nintendo Switch",
        "description": ''' The Legend of Zelda: Breath of the Wild[b] is a 2017 action-adventure game developed and published by Nintendo for the Nintendo Switch and Wii U. Set at the end of the Zelda timeline, the player controls an amnesiac Link as he sets out to save Princess Zelda and prevent Calamity Ganon from destroying the world. Players explore the open world of Hyrule while they collect items and complete objectives such as puzzles or side quests. Breath of the Wild's world is unstructured and encourages exploration and experimentation; the story can be completed in a nonlinear fashion.

Development lasted five years, commencing immediately after the release of The Legend of Zelda: Skyward Sword in 2011. Led by director Hidemaro Fujibayashi and producer Eiji Aonuma, Nintendo sought to rethink Zelda's conventions and introduced elements such as detailed chemistry and physics engines. The designers drew inspiration from Shadow of the Colossus (2005) and The Elder Scrolls V: Skyrim (2011). Monolith Soft, known for their work on the open-world Xenoblade Chronicles series, assisted in designing landscapes and topography.

Breath of the Wild was first planned for release in 2015 as a Wii U exclusive. It was eventually released on March 3, 2017, as a launch game for the Switch and the final Nintendo game for the Wii U. It received acclaim and won numerous Game of the Year accolades. Critics praised its open-ended gameplay, open-world design, and attention to detail, though some criticized its technical performance. It is the best-selling Zelda game and one of the best-selling video games of all time, with 33.31 million copies sold by 2023.

Breath of the Wild is considered one of the greatest video games of all time. Journalists described it as a landmark in open-world design for its emphasis on experimentation, physics-based sandbox, and emergent gameplay. Numerous developers cited Breath of the Wild as inspiration, and it is a popular point of comparison among open-world games. A spin-off, Hyrule Warriors: Age of Calamity, was released in 2020 while a sequel, The Legend of Zelda: Tears of the Kingdom, was released in 2023.'''
        },
    {
        "id":3,
        "title": "Red Dead Redemption 2", 
        "genre": "Action-adventure", 
        "platform": "PS4, Xbox One",
        "description":'''Red Dead Redemption is a 2010 action-adventure game developed by Rockstar San Diego and published by Rockstar Games. A successor to 2004's Red Dead Revolver, it is the second game in the Red Dead series. Red Dead Redemption is set during the decline of the American frontier in the year 1911. It follows John Marston, a former outlaw who, after his wife and son are taken hostage by the government in ransom for his services as a hired gun, sets out to bring three members of his former gang to justice. The narrative explores themes of the cycle of violence, masculinity, redemption, and the American Dream.

The game is played from a third-person perspective. The player can freely roam in its interactive open world, a fictionalized version of the Western United States and Northern Mexico, primarily by horseback, and on foot. Gunfights emphasize a gunslinger gameplay mechanic called "Dead Eye" that allows players to mark multiple shooting targets on enemies in slow motion. The game uses a morality system by which the player's actions in the game affect their character's levels of honor, fame, and how other characters respond to the player. An online multiplayer mode is included with the original release, allowing up to 16 players to engage in both cooperative and competitive gameplay in a recreation of the single-player setting.

The game's development lasted over five years, and it became one of the most expensive video games ever made. Rockstar improved its proprietary game engine to increase its technological capabilities. The development team conducted extensive research, including field trips to Washington, D.C. and analyzing classic Western films, to achieve realism for the game. The team hired professional actors to perform the body movements through motion capture. Red Dead Redemption features an original score composed by Bill Elm and Woody Jackson. The game's development received controversy following accusations of unethical working practices. The working hours and managerial style of the studio was met with public complaints from staff members.

Red Dead Redemption was released for the PlayStation 3 and Xbox 360 in May 2010, and for Nintendo Switch and PlayStation 4 in August 2023. It received critical acclaim for its visuals, music, performances, gameplay, and narrative. It won several year-end accolades, including Game of the Year awards from several gaming publications, and is considered by critics as one of the best video games ever made. It had shipped around 23 million copies by 2021, making it one of the best-selling video games. After the game's release, several downloadable content additions were released; Undead Nightmare, later released as a standalone game, added a new single-player campaign in which Marston searches for a cure for an infectious zombie plague. A prequel, Red Dead Redemption 2, was released in October 2018.''',
        },
    {
        "id":4,
        "title": "Overwatch", 
        "genre": "First-person shooter", 
        "platform": "PC, PS4, Xbox One",
        "description":'''Overwatch (retroactively referred to as Overwatch 1[b]) was a 2016 team-based multiplayer first-person shooter game by Blizzard Entertainment. The game was first released for PlayStation 4, Windows, and Xbox One in May 2016 and Nintendo Switch in October 2019. Cross-platform play was supported across all platforms.

Described as a "hero shooter", Overwatch assigned players into two teams of six, with each player selecting from a large roster of characters, known as "heroes", with unique abilities. Teams worked to complete map-specific objectives within a limited period of time. Blizzard added new characters, maps, and game modes post-release, all free of charge, with the only additional cost to players being optional loot boxes to purchase cosmetic items.

Overwatch is Blizzard's fourth major franchise and came about following the 2014 cancellation of a massively multiplayer online role-playing game, Titan. A portion of the Titan team were inspired by the success of team-based first-person shooters like Team Fortress 2 and the popularity of multiplayer online battle arena games, creating a hero-based shooter which emphasized teamwork. Some elements of Overwatch borrow concepts from the canceled Titan project.

Overwatch was unveiled at the 2014 BlizzCon event and was in a closed beta from late 2015 through early 2016. An open beta before release drew in nearly 10 million players. Overwatch received universal acclaim from critics, who praised the game for its accessibility, the diverse appeal of its hero characters, its cartoonish art style, and enjoyable gameplay. Blizzard reported over US$1 billion in revenue during the first year of its release and had more than 50 million players after three years. Overwatch is considered to be among the greatest video games ever made, receiving numerous game of the year awards and other accolades. The game was a popular esport, with Blizzard funding and producing the global Overwatch League.

A sequel, Overwatch 2, was announced in 2019 and entered beta in 2022. The game is free to play, with all cosmetic items from Overwatch carried over while introducing new heroes, maps, and gamemodes. On October 3, 2022, the Overwatch servers were shut down in preparation for the release of Overwatch 2 the next day.''',
        },
    {
        "id":5,
        "title": "Fortnite", 
        "genre": "Battle Royale", 
        "platform": "PC, PS4, Xbox One, iOS, Android",
        "description":''' Fortnite is an online video game and game platform developed by Epic Games and released in 2017. It is available in six distinct game mode versions that otherwise share the same general gameplay and game engine: Fortnite Battle Royale, a free-to-play battle royale game in which up to 100 players fight to be the last person standing; Fortnite: Save the World, a cooperative hybrid tower defense-shooter and survival game in which up to four players fight off zombie-like creatures and defend objects with traps and fortifications they can build; and Fortnite Creative, in which players are given complete freedom to create worlds and battle arenas, Lego Fortnite, an open world survival game, Rocket Racing, a racing game, and Fortnite Festival, a rhythm game.

Save the World and Battle Royale were released in 2017 as early access titles, while Creative was released on December 6, 2018. While the Save the World and Creative versions have been successful for Epic Games, Fortnite Battle Royale in particular became an overwhelming success and a cultural phenomenon, drawing more than 125 million players in less than a year, earning hundreds of millions of dollars per month. Fortnite as a whole generated $9 billion in gross revenue up until December 2019, and it has been listed among the greatest games of all time.

Save the World is available for macOS,[c] PlayStation 4, Windows, and Xbox One, while Battle Royale and Creative were released for all those platforms as well as Android and iOS devices[c] and Nintendo Switch. The game also launched with the release of the ninth-generation PlayStation 5 and Xbox Series X/S consoles. Furthermore, Lego Fortnite, Rocket Racing and Fortnite Festival are available on all platforms.'''
        }
]



def game(request):
    context = {
        "game":video_games
    }
    return render(request,'game.html',context)


def details(request,id):
    data = None
    for game in video_games:
        if game['id'] == id:
            data = game
            break
    
    context = {
        "games":data
    }

    return render(request,'details.html',context)





