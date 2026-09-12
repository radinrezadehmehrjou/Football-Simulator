"""
Module:
Data Manager

Owner:
Amirali Khajouei

Phase:
1
"""

def load_players(path) :
    lst = []

    with open(path) as txt :
        for l in txt :
            line = l.strip("/n")
            
            dic = {}
            
            if line == "" :
                continue
            
            for i in line.split(",") :
                
                key, value = i.strip().split(":")
                dic[key] = value
            lst.append(dic)
        return lst

def load_teams(path) :
    lst = []
    with open(path) as file :
        for i in file :
            dic = {} 
            
            for l in i.split(",") :
                key , value = l.strip().split(":")
                dic[key] = value
            lst.append(dic)
    return lst

def calculate_team_power():
    players = load_players()
    teams = load_teams()
    
    # محاسبه توان هر تیم
    team_powers = []
    for i in range(0, len(players), 5):
        team_power = sum(int(players[j]["power"]) for j in range(i, min(i+5, len(players))))
        team_powers.append(team_power)
    
    # بروزرسانی توان تیم‌ها
    for i in range(len(teams)):
        if i < len(team_powers):
            teams[i]["power"] = str(team_powers[i])
    
    return teams



"""
Phase 2:

"""