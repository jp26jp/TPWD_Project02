import csv

from player import Player

all_players = []
teams = open("teams.txt", "w+")


def load_players():
    """
    Loads players from the .csv file, adds them to the `all_players` array,
    and sorts them by their experience
    """
    with open("./soccer_players.csv", newline="") as csvFile:
        reader = csv.DictReader(csvFile, delimiter=",")
        players = list(reader)
    for player in players:
        all_players.append(Player(player["Name"], player["Height (inches)"], player["Soccer Experience"], player["Guardian Name(s)"]))
    all_players.sort()


def assign_players_team(team1, team2, team3):
    """
    Loops through all_players array and adds one player at a time to each team.
    Player's are divided equally by experience because the all_players array
    is sorted by player's experience.

    :param team1: an empty array of the first team
    :param team2: an empty array of the second team
    :param team3: an empty array of the third team
    """
    for index, player in enumerate(all_players):
        teamNumber = index % 3
        if teamNumber == 0: team1.append(player)
        if teamNumber == 1: team2.append(player)
        if teamNumber == 2: team3.append(player)


def write_team_info_to_file(name, team):
    """
    Creates a file with each team's roster.

    :param name: the name of the team
    :param team: an array of the players on the team
    """
    teams.write(name + "\n")
    for member in team:
        teams.write("{}, {}, {}\n".format(member.name, member.experience, member.guardians))


def write_player_letters(team, team_name):
    """
    Creates a unique file for each team members guardians informing them
    which team their child belongs to and when practice is

    :param team: the array of team members
    :param team_name: a string that is the name of the team
    :return:
    """
    for member in team:
        name = member.name.lower().replace(" ", "_")
        file = open("{}.txt".format(name), "w+")
        file.write("Dear {},\n".format(member.guardians))
        file.write("Your human, {}, has been accepted by the terrifying {}. Practice is at sunrise tomorrow.".format(member.name, team_name))


if __name__ == '__main__':
    dragons = []
    sharks = []
    raptors = []

    load_players()
    assign_players_team(dragons, sharks, raptors)

    write_team_info_to_file("Dragons", dragons)
    write_team_info_to_file("\n\nSharks", sharks)
    write_team_info_to_file("\n\nRaptors", raptors)

    write_player_letters(dragons, "Dragons")
    write_player_letters(sharks, "Sharks")
    write_player_letters(raptors, "Raptors")