import random


TEAM_NAME = ("Madrid", "Seoul")

class Team:
    def __init__(self) -> None:
        self.name = ""
        self.score = 0

if __name__ == "__main__":
    money = 50000
    print("현재금액:", money)
    teams = []
    for tn in TEAM_NAME:
        team = Team()
        team.name = tn
        teams.append(team)
    run = True
    while run:
        team_A = teams.pop(random.randrange(len(teams)))
        team_A.score = random.randrange(8)
        team_B = teams.pop(random.randrange(len(teams)))
        team_B.score = random.randrange(8)
        print("")
        print(f"{team_A.name} vs {team_B.name}")

        betting = int(input("배팅할 금액: "))
        money = money - betting

        print(f"1. {team_A.name}이 2점차 이상으로 이긴다.  2. {team_A.name}가 2점차 이하로 이긴다.")
        print(f"3. {team_B.name}이 2점차 이상으로 이긴다.  4. {team_B.name}가 2점차 이하로 이긴다.")
        print("5. 무승부")
        if team_A.score >= team_B.score + 2:
            correct_answer = "1"
        elif team_B.score < team_A.score <= team_B.score + 2:
            correct_answer = "2"
        elif team_B.score >= team_A.score + 2:
            correct_answer = "3"
        elif team_A.score < team_B.score <= team_A.score + 2:
            correct_answer = "4"
        elif team_A.score == team_B.score:
            correct_answer = "5"
        answer = input()
        print(f"점수: {team_A.name}: {team_A.score}, {team_B.name}: {team_B.score}")
        if answer == correct_answer:
            money = money + betting*10
            betting = 0
            print("배팅 성공! 현재 남은 돈:", money)
        else:
            print("배팅 실패! 현재 남은 돈:", money)
        teams.append(team_A)
        teams.append(team_B)
        random.shuffle(teams)



