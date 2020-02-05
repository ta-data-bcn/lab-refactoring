{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Disney Hangman F.V."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Greeting the player!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What is your name? jo\n",
      "Welcome to Disney Hangman jo!. Ready to play?!\n"
     ]
    }
   ],
   "source": [
    "name = input(\"What is your name? \")\n",
    "\n",
    "print(\"Welcome to Disney Hangman \" + name + \"!. Ready to play?!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2.Importing an external text file containing all the Disney Classics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Academy Award Review of Walt Disney Cartoons', 'Snow White and the Seven Dwarfs', 'Pinocchio', 'Fantasia', 'The Reluctant Dragon', 'Dumbo', 'Bambi', 'Saludos Amigos', 'Victory Through Air Power', 'The Three Caballeros', 'Make Mine Music', 'Song of the South', 'Fun and Fancy Free', 'Melody Time', 'So Dear to My Heart', 'The Adventures of Ichabod and Mr. Toad', 'Cinderella', 'Alice in Wonderland', 'Peter Pan', 'Lady and the Tramp', 'Sleeping Beauty', 'One Hundred and One Dalmatians', 'The Sword in the Stone', 'The Jungle Book', 'The Aristocats', 'Robin Hood', 'The Many Adventures of Winnie the Pooh', 'The Rescuers', 'The Fox and the Hound', 'The Black Cauldron', 'The Great Mouse Detective', 'Who Framed Roger Rabbit', 'Oliver & Company', 'The Little Mermaid', 'DuckTales the Movie: Treasure of the Lost Lamp', 'The Rescuers Down Under', 'Beauty and the Beast', 'Aladdin', 'The Nightmare Before Christmas', 'The Lion King', 'A Goofy Movie', 'Pocahontas', 'Toy Story', 'James and the Giant Peach', 'The Hunchback of Notre Dame', 'Hercules', 'Mulan', \"A Bug's Life\", 'Tarzan', 'Toy Story 2', 'Fantasia 2000', 'The Tigger Movie', 'Dinosaur', \"The Emperor's New Groove\", \"Recess: School's Out\", 'Atlantis: The Lost Empire', 'Monsters, Inc.', 'Return to Never Land', 'Lilo & Stitch', 'Spirited Away', 'Treasure Planet', 'The Jungle Book 2', \"Piglet's Big Movie\", 'Finding Nemo', 'Brother Bear', \"Teacher's Pet\", 'Home on the Range', 'The Incredibles', \"Pooh's Heffalump Movie\", \"Howl's Moving Castle\", 'Valiant', 'Chicken Little', 'Bambi II', 'The Wild', 'Cars', 'Meet the Robinsons', 'Ratatouille', 'Enchanted', 'WALL-E', 'Tinker Bell', 'Roadside Romeo', 'Bolt', 'Up', 'Ponyo', 'Tinker Bell and the Lost Treasure', 'A Christmas Carol', 'The Princess and the Frog', 'Toy Story 3', 'Tales from Earthsea', 'Tangled', 'Gnomeo & Juliet', 'Mars Needs Moms', 'Cars 2', 'Winnie the Pooh', 'The Secret World of Arrietty', 'Arjun: The Warrior Prince', 'Brave', 'Secret of the Wings', 'Frankenweenie', 'Wreck-It Ralph', 'Monsters University', 'Planes', 'Frozen', 'The Pirate Fairy', 'The Wind Rises', 'Planes: Fire & Rescue', 'Big Hero 6', 'Strange Magic', 'Tinker Bell and the Legend of the NeverBeast', 'Inside Out', 'The Good Dinosaur', 'Zootopia', 'Finding Dory', 'Moana', 'Cars 3', 'Coco', 'Incredibles 2', 'Ralph Breaks the Internet', 'Toy Story 4', 'The Lion King', 'Frozen II', 'Spies in Disguise']\n"
     ]
    }
   ],
   "source": [
    "with open('../Project_Files/disney_movies_list.txt') as f:\n",
    "    linelist = f.readlines()\n",
    "    \n",
    "disney_classics=[]\n",
    "for i in linelist:\n",
    "    disney_classics.append(i.rstrip(\"\\n\"))\n",
    "    \n",
    "print(disney_classics)    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3.1. Puzzlegiver (aka the machine) selects a random word amongst the established list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DINOSAUR\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "chosen_movie = random.choice(disney_classics).upper()\n",
    "\n",
    "print(chosen_movie)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3.2. The random selection of the chosen movie can also be done via a funtion with the below programme. For the sake if keeping consistency, we have left the action in the above format."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import random\n",
    "\n",
    "#def machine_chosen_movie ():\n",
    "    #return random.choice(disney_classics).upper()\n",
    "\n",
    "# REMOVE!eventually remove the name since it´s a secret word!\n",
    "#print(chosen_movie)\n",
    "\n",
    "#machine_chosen_movie()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4.Puzzlegiver confirms the word has been selected and gives you the length of the word."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The movie title contains 8 characters. The movie is formed of 1 word(s).\n",
      "_ _ _ _ _ _ _ _ \n"
     ]
    }
   ],
   "source": [
    "print(\"The movie title contains \" + str(len(chosen_movie)-(len(chosen_movie.split())-1)) + \" characters. The movie is formed of \" + str(len(chosen_movie.split())) + \" word(s).\")\n",
    "\n",
    "ch_word_length = \"\"\n",
    "\n",
    "for char in chosen_movie:\n",
    "    if char == \" \":\n",
    "        ch_word_length+= \" \"\n",
    "    else:\n",
    "        ch_word_length+= \"_ \"\n",
    "        \n",
    "print(ch_word_length)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5. Create a dictionary of the chosen movie so that each value of the text is associated with a key."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0: 'D', 1: 'I', 2: 'N', 3: 'O', 4: 'S', 5: 'A', 6: 'U', 7: 'R'}\n"
     ]
    }
   ],
   "source": [
    "chosen_movie_dict = {}\n",
    "\n",
    "index = 0\n",
    "\n",
    "for i in chosen_movie:\n",
    "    index += 1\n",
    "    chosen_movie_dict [index - 1] = i\n",
    "    \n",
    "print(chosen_movie_dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6. Create a string associated with the number of spaces and characters from the chosen movie for parallel comparison."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "________\n"
     ]
    }
   ],
   "source": [
    "empty_chosen_movie_string = \"\"\n",
    "\n",
    "for char in chosen_movie:\n",
    "    if char == \" \":\n",
    "        empty_chosen_movie_string +=\" \"\n",
    "    else:\n",
    "         empty_chosen_movie_string +=\"_\"\n",
    "    \n",
    "    \n",
    "print(empty_chosen_movie_string)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7. Create a dictionary of the \"empty\" chosen movie so that each value of the text is associated with a key, and refilled as users answers correct letters."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "empty_chosen_movie_dict= {}\n",
    "\n",
    "index_empty = 0\n",
    "\n",
    "for i in empty_chosen_movie_string:\n",
    "    index_empty += 1\n",
    "    empty_chosen_movie_dict[index_empty - 1] = i\n",
    "    \n",
    "print(empty_chosen_movie_dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Below the final programme for the game"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "failed_attempts = 0\n",
    "max_attempts = 10\n",
    "already_said_characters= []\n",
    "player_guess = \"\"\n",
    "while (failed_attempts < max_attempts) & (player_guess != chosen_movie):\n",
    "    character_chosen = input(\"Please guess a character:\").upper()\n",
    "    while character_chosen in already_said_characters:\n",
    "        print(\"Go again, you have already introduced this character\")\n",
    "        character_chosen = input(\"Please guess a character:\").upper()\n",
    "    already_said_characters.append(character_chosen)\n",
    "    match_letter=0\n",
    "    for index,letter in chosen_movie_dict.items():\n",
    "        if letter == character_chosen:\n",
    "            empty_chosen_movie_dict [index] = character_chosen\n",
    "            player_guess = ''.join(empty_chosen_movie_dict.values())\n",
    "            match_letter+=1\n",
    "    print(player_guess)\n",
    "    if match_letter==0:\n",
    "        failed_attempts+=1\n",
    "        print(\"Wrong answer. You have \" + str((max_attempts - failed_attempts)) + \" attempts left.\")\n",
    "if failed_attempts==max_attempts:\n",
    "    print(\"\"\"No Hakuna Matata for you amigo, you dead.\n",
    "                +---+\n",
    "                |   |\n",
    "               _O_  |\n",
    "                |   |\n",
    "               / \\  |\n",
    "                    |\n",
    "              =========\"\"\")\n",
    "else:\n",
    "    print(\"\"\"You won and are alive!\n",
    "         +---+\n",
    "                    |\n",
    "                    |\n",
    "               \\O/  |\n",
    "                |   |\n",
    "               | |  |\n",
    "              ========= \"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
