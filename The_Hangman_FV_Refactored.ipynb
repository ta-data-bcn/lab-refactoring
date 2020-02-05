{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The_Hangman_FV_Refactored\n",
    "\n",
    "\n",
    "Based on the old version of my Disney Hangman delivered on Week1, I reflected and I also requested my colleague Robin Langlois feedback to re-do the game and improve it.\n",
    "The key things we decide to modify to imporve the game are the following:\n",
    "\n",
    "1. FUNCTIONS. On the initial version of the game, everything was done by different steps within Jupyter Notebook. This lead to a fractured experience with the game which was not user friendly. I have redone the game via functions, and now the expreience it´s much more flawless since all the stepped functions link with each other.\n",
    "\n",
    "2. DOCSTRING. I have decided to include documentation within my functions for my use and potentially other people that might read my code. This has made the process of creating functions much more easy since I have included inputs and returns related to each function.\n",
    "\n",
    "3. READING THE DATA. Regarding the data, at the moment the function is calling a small text file including a small list of Disney Classic Movie titles. One potential improvement for the future would be to read the database from a cloud if we wanted to extend the game to bigger databases. ie. All movies, song titles, animals, etc...\n",
    "\n",
    "Find below the new version of the game. To play it, go directly to the final section."
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
   "metadata": {},
   "outputs": [],
   "source": [
    "def greeting():\n",
    "    \"\"\"\n",
    "    @input = null\n",
    "    @ return = null\n",
    "    \"\"\"\n",
    "    name = input(\"What is your name? \")\n",
    "    print(\"Welcome to Disney Hangman \" + name + \"!. Ready to play?!\")"
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
   "outputs": [],
   "source": [
    "def import_raw():\n",
    "    \"\"\"\n",
    "    @input = null\n",
    "    @ return = disney_classics\n",
    "    @todo : future iteration read from bigger database from cloud\n",
    "    \"\"\"\n",
    "    with open('/Users/anna/Desktop/Ironhack/Week_3/lab-refactoring/disney_movies_list.txt') as f:\n",
    "        linelist = f.readlines()\n",
    "\n",
    "        disney_classics=[]\n",
    "        for i in linelist:\n",
    "            disney_classics.append(i.rstrip(\"\\n\"))\n",
    "            \n",
    "        return disney_classics\n",
    "          "
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
   "outputs": [],
   "source": [
    "def random_select(x):\n",
    "    \"\"\"\n",
    "    @input = disney_classics\n",
    "    @ return = chosen_movie\n",
    "    \"\"\"\n",
    "    import random\n",
    "    chosen_movie = random.choice(x).upper()\n",
    "    \n",
    "    return chosen_movie"
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
   "outputs": [],
   "source": [
    "def movie_clues(x):\n",
    "    \"\"\"\n",
    "    @input = chosen_movie\n",
    "    @ return = null\n",
    "    \"\"\"\n",
    "    \n",
    "    print(\"The movie title contains \" + str(len(x)-(len(x.split())-1)) + \" characters. The movie is formed of \" + str(len(x.split())) + \" word(s).\")\n",
    "\n",
    "    ch_word_length = \"\"\n",
    "\n",
    "    for char in x:\n",
    "        if char == \" \":\n",
    "            ch_word_length+= \" \"\n",
    "        else:\n",
    "            ch_word_length+= \"_ \"\n",
    "\n",
    "    print(ch_word_length)"
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
   "outputs": [],
   "source": [
    "def movie_dict(x):\n",
    "    \"\"\"\n",
    "    @input = chosen_movie\n",
    "    @ return = chosen_movie_dict\n",
    "    \"\"\"\n",
    "    chosen_movie_dict = {}\n",
    "\n",
    "    index = 0\n",
    "\n",
    "    for i in x:\n",
    "        index += 1\n",
    "        chosen_movie_dict [index - 1] = i\n",
    "     \n",
    "    return chosen_movie_dict\n"
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
   "outputs": [],
   "source": [
    "def empty_string(x):\n",
    "    \"\"\"\n",
    "    @input = chosen_movie\n",
    "    @ return = empty_chosen_movie_string\n",
    "    \"\"\"\n",
    "    empty_chosen_movie_string = \"\"\n",
    "\n",
    "    for char in x:\n",
    "        if char == \" \":\n",
    "            empty_chosen_movie_string +=\" \"\n",
    "        else:\n",
    "             empty_chosen_movie_string +=\"_\"\n",
    "\n",
    "    return empty_chosen_movie_string\n"
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
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "### Here the input is the return of empty_chosen_movie_string/empty_string\n",
    "\n",
    "def empty_dict(x):\n",
    "    \"\"\"\n",
    "    @input = empty_chosen_movie_string\n",
    "    @ return = empty_chosen_movie_dict\n",
    "    \"\"\"\n",
    "    empty_chosen_movie_dict= {}\n",
    "\n",
    "    index_empty = 0\n",
    "\n",
    "    for i in x:\n",
    "        index_empty += 1\n",
    "        empty_chosen_movie_dict[index_empty - 1] = i\n",
    "        \n",
    "    return empty_chosen_movie_dict "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "8. Below the final program for the game to run"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def the_game(x,y,z):\n",
    "    \"\"\"\n",
    "    @input = chosen_movie\n",
    "             chosen_movie_dict\n",
    "             empty_chosen_movie_dict\n",
    "    @ return = null\n",
    "    \"\"\"\n",
    "    failed_attempts = 0\n",
    "    max_attempts = 10\n",
    "    already_said_characters= []\n",
    "    player_guess = \"\"\n",
    "\n",
    "    while (failed_attempts < max_attempts) & (player_guess != x):\n",
    "        character_chosen = input(\"Please guess a character:\").upper()\n",
    "        while character_chosen in already_said_characters:\n",
    "            print(\"Go again, you have already introduced this character\")\n",
    "            character_chosen = input(\"Please guess a character:\").upper()\n",
    "        already_said_characters.append(character_chosen)\n",
    "        match_letter=0\n",
    "        for index,letter in y.items():\n",
    "            if letter == character_chosen:\n",
    "                z[index] = character_chosen\n",
    "                player_guess = ''.join(z.values())\n",
    "                match_letter+=1\n",
    "        print(player_guess)\n",
    "        if match_letter==0:\n",
    "            failed_attempts+=1\n",
    "            print(\"Wrong answer. You have \" + str((max_attempts - failed_attempts)) + \" attempts left.\")\n",
    "    if failed_attempts==max_attempts:\n",
    "        print(\"\"\"No Hakuna Matata for you amigo, you dead.\n",
    "                    +---+\n",
    "                    |   |\n",
    "                   _O_  |\n",
    "                    |   |\n",
    "                   / \\  |\n",
    "                        |\n",
    "                  ========= \"\"\")\n",
    "        print(\"The answer was : \", x)\n",
    "    else:\n",
    "        print(\"\"\"You won and are alive!\n",
    "             +---+\n",
    "                        |\n",
    "                        |\n",
    "                   \\O/  |\n",
    "                    |   |\n",
    "                   | |  |\n",
    "                  ========= \"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# FINAL COMPILATION\n",
    "\n",
    "#1\n",
    "greeting()\n",
    "\n",
    "#2\n",
    "chosen_movie_v = random_select(import_raw())\n",
    "\n",
    "#3\n",
    "movie_clues(chosen_movie_v)\n",
    "\n",
    "#4\n",
    "chosen_movie_dict_v = movie_dict(chosen_movie_v)\n",
    "\n",
    "#5\n",
    "chosen_movie_dict_v=movie_dict(chosen_movie_v)\n",
    "\n",
    "#6\n",
    "empty_chosen_movie_string_v = empty_string(chosen_movie_v)\n",
    "\n",
    "#7\n",
    "empty_chosen_movie_dict_v = empty_dict(empty_chosen_movie_string_v)\n",
    "\n",
    "#8\n",
    "the_game(chosen_movie_v, chosen_movie_dict_v, empty_chosen_movie_dict_v)"
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
 "nbformat_minor": 4
}
