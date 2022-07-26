players = ['Andreea', 'Ionel', 'Eva','Mitica', 'Gabi', 'Alin', 'Alice', 'Cristi',
            'Corina', 'Mihai', 'Anca', 'Teodor', 'Maria', 'Gustav', 'Ionela']

# version 1
team1_1 = players[1::2]
team2_1 = players[2::2]

print('version 1:')
print(f'team 1 is {team1_1}')
print(f'team 2 is {team2_1}')

# version 2
team1_2 = players[:len(players)//2]
team2_2 = players[len(players)//2+1:]

print('version 2:')
print(f'team 1 is {team1_2}')
print(f'team 2 is {team2_2}')
