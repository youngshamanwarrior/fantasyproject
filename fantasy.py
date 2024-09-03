#simulation work in numpy

import numpy as np

# Define projections - these are to be improved upon using API's 
team_1 = {
    "Josh Allen": 25.4, "Travis Etienne Jr": 15.6, "Jerome Ford": 9.0,
    "Puka Nacua": 14.0, "Malik Nabers": 12.5, "Dalton Kincaid": 8.5,
    "Jaxon Smith-Njigba": 10.0, "Eagles D": 7.0, "Jake Moody": 8.0,
    "Zamir White": 3.0, "Joshua Palmer": 4.0, "Jordan Addison": 11.5,
    "Ty Chandler": 3.5, "Gabe Davis": 9.5, "Jamaal Williams": 6.0,
    "Jordan Mason": 2.0
}

team_2 = {
    "Jordan Love": 18.0, "Josh Jacobs": 17.0, "David Montgomery": 13.0,
    "Ja'Marr Chase": 20.0, "Marvin Harrison Jr": 12.0, "Trey Mcbride": 7.5,
    "DeVonta Smith": 15.0, "Bears D": 5.5, "Dustin Hopkins": 7.5,
    "Jayden Reed": 5.0, "Chase Brown": 2.5, "Khalil Shakir": 3.5,
    "Chuba Hubbard": 6.5, "Darnell Mooney": 7.5, "Jaleel McLaughlin": 2.0,
    "Dontayvion Wicks": 1.5
}


def simulate_game(projections):
    return sum(np.random.normal(loc=score, scale=score * 0.15) for score in projections.values())


# Run simulations
team_1_wins = 0
team_2_wins = 0
n_simulations = 10000

for _ in range(n_simulations):
    team_1_score = simulate_game(team_1)
    team_2_score = simulate_game(team_2)

    if team_1_score > team_2_score:
        team_1_wins += 1
    else:
        team_2_wins += 1

print(f"Team 1 wins: {team_1_wins} times")
print(f"Team 2 wins: {team_2_wins} times")
