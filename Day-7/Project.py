import random

# Welcome Message
print('Welcome To The Hangman Game!')

# Initialize the no. of lives
lives = 6


# Initialize the stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Initializing the letter list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Generating a random word
word = ''
word_list = []
for i in range(6):
    random_number = random.randint(0, len(letters)-1)
    word_list.append(letters[random_number])

for i in range(6):
    word += word_list[i]
print(word)

# Iteration
hidden_list = [True] * 6
flag = True
another_flag = True

while lives != 0:
    another_word_list = []
    another_word = ''
    for i in range(6):
        another_word_list.append(word_list[i])

    for i in range(len(hidden_list)):
        if hidden_list[i]:
            another_word_list[i] = '_'

    for i in range(6):
        another_word += another_word_list[i]

    print(f'The word is: {another_word}')
    guessed_letter = input('Guess a letter: ')
    for i in range(len(word)):
        if hidden_list[i] is True and guessed_letter == word[i]:
            hidden_list[i] = False
            flag = True
            break
        else:
            flag = False

    if not flag:
        lives -= 1

    print(stages[lives])
    print(f'--------------------({lives}/6) Lives Left--------------------')

    if lives == 0:
        print('Game Over! You Lose!')
        break

    for i in range(len(hidden_list)):
        if not hidden_list[i]:
            another_flag = False
        else:
            another_flag = True
            break

    if not another_flag:
        print('Game Over! You Win!')
        break
