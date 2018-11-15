import csv

from player import Player

allPlayers = []
file = open("teams.txt", "w+")


def load_players():
    with open("./soccer_players.csv", newline="") as csvFile:
        reader = csv.DictReader(csvFile, delimiter=",")
        players = list(reader)
    for player in players:
        allPlayers.append(Player(player["Name"], player["Height (inches)"], player["Soccer Experience"], player["Guardian Name(s)"]))
    allPlayers.sort()


def assign_players_team(team1, team2, team3):
    i = 0
    for player in allPlayers:
        i += 1;
        teamNumber = i % 3
        if teamNumber == 0: team1.append(player)
        if teamNumber == 1: team2.append(player)
        if teamNumber == 2: team3.append(player)

def write_team_info_to_file(name, team):
    file.write(name + "\n")
    for member in team:
        file.write("{}, {}, {}\n".format(member.name, member.experience, member.guardians))


if __name__ == '__main__':
    dragons = []
    sharks = []
    raptors = []

    load_players()
    assign_players_team(dragons, sharks, raptors)

    write_team_info_to_file("Dragons", dragons)
    write_team_info_to_file("\n\nSharks", sharks)
    write_team_info_to_file("\n\nRaptors", raptors)
