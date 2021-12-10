# author: LM (AMDG) 12/5/21
def positions(games_tied, games_won_first_team, games_won_second_team):

    total_winning_points_first_team = int(games_won_first_team) * 3
    total_winning_points_second_team = int(games_won_second_team) * 3
    total_tied = int(games_tied)

    total_points_second_team = total_winning_points_second_team + int(games_tied)

    total_points_first_team = total_winning_points_first_team + int(games_tied)

    if total_points_first_team > total_points_second_team:
        return("The first team won the group stage.")
    elif total_points_first_team < total_points_second_team:
        return("The second team won the group stage.")
    else:
        return("They both teams have {0}".format(total_tied))
       

games_won_first_team = input("PLease enter the number of wins the first team won. ")
games_tied = input("Please enter the number of games tied. ")
games_won_second_team = input("Please enter the number of games the second team won. ")
positions(games_tied, games_won_first_team, games_won_second_team)

print(positions(1, 2, 3) == "The second team won the group stage.")
print(positions(0, 2, 3) == "The second team won the group stage.")
print(positions(1, 1, 3) == "The second team won the group stage.")
print(positions(0, 1, 0) == "The first team won the group stage.")