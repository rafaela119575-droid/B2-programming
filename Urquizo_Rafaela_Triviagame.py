'''

Filename: Triviagame.py
Author: Urquizo, Rafaela
Date: 09/28/26
Instructor: Burgess
'''

print('Welcome to the trivia game!')
print('In just a moment, you’ll be presented with a series of questions.')
print('Please answer each question carefully. Once you’ve completed the quiz,')
print('you\'ll receive a score reflecting how many questions you answered correctly.')

score = 0
correct_answers = 0
q1 = input('What is the oldest country in the world?\n')
if q1 == 'San Marine':
    score += 10
    correct_answers += 1
    print('Correct! You have been awarded 10 points!')
else:
    if score > 0:
        score -= 10
    print('Incorrect! You have been penalized 10 point!')
print()
q2 = input('What is the longest river in the world?\n')
if q2 == 'The Nile River':
    score += 10
    correct_answers += 1
    print('Correct! You have been awarded 10 points!')
else:
    if score > 0:
        score -= 10
    print('Incorrect! You have been penalized 10 point!')
print()
q3 = input('How many time zones does Russia have?\n')
if q3 == '11':
    score += 10
    correct_answers += 1
    print('Correct! You have been awarded 10 points!')
else:
    if score > 0:
        score -= 10
    print('Incorrect! You have been penalized 10 point!')
print()
q4 = input('How many days does it take for the Earth to complete one orbit around the Sun?\n')
if q4 == '365':
    score += 10
    correct_answers += 1
    print('Correct! You have been awarded 10 points!')
else:
    if score > 0:
        score -= 10
    print('Incorrect! You have been penalized 10 point!')
print()
q5 = input('What is the capital of France?\n')
if q5 == 'Paris':
    score += 10
    correct_answers += 1
    print('Correct! You have been awarded 10 points!')
else:
    if score > 0:
        score -= 10
    print('Incorrect! You have been penalized 10 point!')
print()
q6 = input('What food never goes bad?\n')
if q6 == 'Honey':
    score += 10
    correct_answers += 1
    print('Correct! You have been awarded 10 points!')
else:
    if score > 0:
        score -= 10
    print('Incorrect! You have been penalized 10 point!')
print()
q7 = input('What is the name of the toy cowboy in the movie Toy Story?\n')
if q7 == 'Woody':
    score += 10
    correct_answers += 1
    print('Correct! You have been awarded 10 points!')
else:
    if score > 0:
        score -= 10
    print('Incorrect! You have been penalized 10 point!')
print()
q8 = input('What is the fairy\'s name in Peter Pan?\n')
if q8 == 'Tinkerbell':
    score += 10
    correct_answers += 1
    print('Correct! You have been awarded 10 points!')
else:
    if score > 0:
        score -= 10
    print('Incorrect! You have been penalized 10 point!')
print()
q9 = input('What is the longest mountain range above sea level in the world?\n')
if q9 == 'The Andes':
    score += 10
    correct_answers += 1
    print('Correct! You have been awarded 10 points!')
else:
    if score > 0:
        score -= 10
    print('Incorrect! You have been penalized 10 point!')
print()
q10 = input('What is the name of the largest island in the world?\n')
if q10 == 'Greenland':
    score += 10
    correct_answers += 1
    print('Correct! You have been awarded 10 points!')
else:
    if score > 0:
        score -= 10
    print('Incorrect! You have been penalized 10 point!')
print()
print('Thank you for playing the Trivia Game!')
print(f'You answered {correct_answers}/10 questions correctly,')
print(f'and received a score of {score}/100!')