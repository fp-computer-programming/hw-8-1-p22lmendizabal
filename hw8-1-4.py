# author: LM (AMDG) 12/5/21
def positions(games_tied, games_won_first_team, games_won_second_team):

    total_winning_points_first_team = int(games_won_first_team) * 3
    total_winning_points_second_team = int(games_won_second_team) * 3
    total_tied = int(games_tied)

    total_points_second_team = total_winning_points_second_team + int(games_tied)

    total_points_first_team = total_winning_points_first_team + int(games_tied)

    if total_points_first_team > total_points_second_team:
        print("The first team won the group stage.")
    if total_points_first_team < total_points_second_team:
        print("The second team won the group stage.")
    else:
        print("Both teams had the same amount of points")

    if total_points_first_team > total_points_second_team:
        print("The first team has " + str(total_points_first_team) + "amount of points.")
    elif total_points_first_team < total_points_second_team:
        print("The second team has " + str(total_points_first_team) + "amount of points.")
    else:
        print("Both teams had " + str(total_tied))

games_won_first_team = input("PLease enter the number of wins the first team won. ")
games_tied = input("Please enter the number of games tied. ")
games_won_second_team = input("Please enter the number of games the second team won. ")
positions(games_tied, games_won_first_team, games_won_second_team)

print(positions(games_won_first_team) = "The first team won the group stage."))