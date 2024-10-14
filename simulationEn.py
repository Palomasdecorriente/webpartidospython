import random

class Team:
    def __init__(self, name, skill, average_goals_per_game):
        self.name = name
        self.skill = skill
        self.average_goals_per_game = average_goals_per_game

    def calculate_win_probability(self, other_team):
        # Calculates the home team's win probability
        win_probability = self.skill / (self.skill + other_team.skill)
        return win_probability

    def calculate_goals(self, win_probability):
        # Calculates the number of goals for the team
        goals = round(self.average_goals_per_game * win_probability)
        return goals

def calculate_result(home_team, away_team):
    # Calculates the win probability for the home team
    home_win_probability = home_team.calculate_win_probability(away_team)

    # Calculates the win probability for the away team
    away_win_probability = away_team.calculate_win_probability(home_team)

    # Calculates the number of goals for the home team
    home_goals = home_team.calculate_goals(home_win_probability)

    # Calculates the number of goals for the away team
    away_goals = away_team.calculate_goals(away_win_probability)

    return home_goals, away_goals

while True:
    # Asks for the name of the home and away teams
    home_team_name = input("Enter the name of the home team: ")
    away_team_name = input("Enter the name of the away team: ")

    # Asks for the skill of the home and away teams
    home_team_skill = int(input("Enter the skill of the home team (1-100): "))
    away_team_skill = int(input("Enter the skill of the away team (1-100): "))

    # Asks for the average goals per game of the home and away teams
    home_team_average_goals = float(input("Enter the average goals per game of the home team: "))
    away_team_average_goals = float(input("Enter the average goals per game of the away team: "))

    # Creates objects of the Team class
    home_team = Team(home_team_name, home_team_skill, home_team_average_goals)
    away_team = Team(away_team_name, away_team_skill, away_team_average_goals)

    # Calculates the result of the match
    home_goals, away_goals = calculate_result(home_team, away_team)

    # Displays the result
    print(f"Match result: {home_team.name} {home_goals} - {away_goals} {away_team.name}")

    # Asks if the user wants to continue
    response = input("Do you want to continue? (y/n): ")
    if response.lower() != 'y':
        break
