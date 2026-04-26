class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Team:
    def __init__(self):
        self.members = []

    def add_player(self, player_obj):
        if isinstance(player_obj, Player):
            self.members.append(player_obj)

    def get_score(self):
        totalScore = 0
        for plr in self.members:
            totalScore += plr.score

        return totalScore

coolest_player_ever = Player("Razan", 100)
also_coolest_player_ever = Player("Maisoon", 100)

coolest_team_ever = Team()

coolest_team_ever.add_player(coolest_player_ever)
coolest_team_ever.add_player(also_coolest_player_ever)

print(coolest_team_ever.get_score())