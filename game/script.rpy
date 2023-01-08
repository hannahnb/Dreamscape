# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kris")
define d = Character("Dad", color = "#00FF00") #color changes color of character name

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg libraryv5

    "Kris was getting home from school, exploring her home's library."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "kris happy.png" to the images
    # directory.

    show kris happyv6 at left #shows Kris on the left side 
    with moveinleft #Kris appears on the scene sliding on the left side

    "Kris steps into her dad's office."

    "His desk is extremely messy, with documents and books scattered across its surface."

    "The crowded bookshelf near the back window catches her attention."

    k "\"There must be a dictionary in here somewhere.\""

    "Kris reaches up on the top of her toes and spots the dictionary. It’s out her reach."

    "Finding the ladder, she places it on the floor and attempts to grab the book again."

    k "\"AHHHHHH!\""

    scene bg libraryv5 with vpunch #camera shake as she falls

    k "\"OW!\""

    scene bg bookv9

    "A book lands on her head. Kris picks it up, puts it on a desk, and flips to the first page."

    k "\"Why would Dad have an old storybook laying around his office?\""

    "Kris thumbs the details of the pictures in the book."

    k "\"Didn’t I have this dream last night?\""
    
    d "\"Kriiiis!\""

    scene bg libraryv5

    show kris happyv6 at left

    "Kris hears her dad call from the other room."

    k "\"Coming Dad!\""
    
    "She quickly shuts the book close and leaves the library."

    show kris happyv6 
    with fade #fade screen transition

 # This ends the game.

return
