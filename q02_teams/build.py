# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


def teams(data=data):
    teams = []
    for team in data['info'] ['teams']:
        teams.append(team)

    return teams
teams(data)
print(teams)
