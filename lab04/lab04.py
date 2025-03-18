import random

def roll_die():
    return random.randint(1,6)

def roll_multiple_dice(num_dice):
    rolls = [roll_die() for _ in range(num_dice)]
    print('Rolled dice: ', rolls) 
    return sum(rolls)

def get_round_result(player_total, computer_total):
    global round_result
    if player_total > computer_total: 
        round_result = 'Win'
    elif computer_total > player_total: 
        round_result = 'Loss'
    else: 
        round_result = 'Draw'

def shop(score):
    while True: 
        print('\nMenu')
        print(f'1. Add +5 points (Cost: 5 points)')
        print(f'2. Add +15 points (Cost: 10 points)')
        print(f'3. Exit Shop')
        user_choice = int(input('Select a menu option: '))
        if user_choice == 1 and score >=5: 
            score += 5 
            print('Updated score: ', score)
        elif user_choice == 2 and score >=10:
            score += 15
            print('Updated Score: ', score)
        elif user_choice == 3: 
            break
        else: 
            print('Not enough points or invalid choice')
    return score

def display_statistics(rounds, wins, draws, losses, score, round_numbers, player_totals, computer_totals, results):
    print('Total Rounds PLayed: ', rounds)
    print('Wins: ', wins, 'Draws: ', draws, 'Losses: ', losses)
    print('Final Score: ', score)
    for i in range(rounds):
        print(f'Round {round_numbers[i]}: Player {player_totals[i]} vs Computer Totals: {computer_totals[i]} -> {results[i]}')

random.seed(15)
score = 0
rounds = 0
wins = 0
draws = 0
losses = 0
round_numbers = []
player_totals = []
computer_totals = []
results = []
round_result = ''

while True: 
    rounds += 1

    print('\nRound', rounds)
    player_total = roll_multiple_dice(2)
    computer_total =  roll_multiple_dice(2)
    print('Player rolled: ', player_total, 'Computer rolled: ', computer_total)
    get_round_result(player_total, computer_total)
    print('Round result: ', round_result)

    if round_result == 'Win':
        wins += 1
        score += 20 
    elif round_result == 'Draw':
        draws += 1
        score += 10 
    elif round_result == 'Loss':
        losses += 1
        score += 0
    
    print('Updated score after round: ', score)

    round_numbers.append(rounds)
    player_totals.append(player_total)
    computer_totals.append(computer_total)
    results.append(round_result)
    
    visit_shop = str(input("To visit the shop input yes: ")).lower()
    if visit_shop == 'yes':
        old_score = score 
        score = shop(score)

    print(f'Result: {round_result}. Current Score: {score}')
    if str(input('Play another round (yes/no): ')).lower() != 'yes':
        break

display_statistics(rounds, wins, draws, losses, score, round_numbers, player_totals, computer_totals, results)
