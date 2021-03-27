file1 = open("out.txt","w")
read = open("in.txt","r")

class Team:
    def __init__(self, id):
        self.id = id
        self.problem_inputs =   [[0, 0, 0, 0, 0]
                                ,[0, 0, 0, 0, 0]
                                ,[0, 0, 0, 0, 0]
                                ,[0, 0, 0, 0, 0]
                                ,[0, 0, 0, 0, 0]]
        self.score = 0
        self.penalty_time = 0


def solve(case, final):
    teams, logs = [int(x) for x in read.readline().split(' ')]
    team_list = []
    for i in range(0, teams):
        a = Team(i+1)
        team_list.append(a)

    for i in range(0, logs):
        timestamp, teamid, problem, inp, scored = [int(x) for x in read.readline().split(' ')]
        if scored == 1 and team_list[teamid-1].problem_inputs[problem-1][inp-1] != 1:
            team_list[teamid-1].score += inp * 100
            team_list[teamid-1].penalty_time += timestamp
            team_list[teamid-1].problem_inputs[problem-1][inp-1] = 1
    team_list.sort(key=lambda x: (-x.score, x.penalty_time, x.id))
    result = f'Case #{case}: '
    for team in team_list:
        result += f'{team.id} '
    result.rstrip()
    if final:
        file1.write(f'{result}')
    else:
        file1.write(f'{result}\n')

n = int(read.readline())
for i in range(0, n):
    solve(i+1, i == n-1)
 
    
file1.close()
