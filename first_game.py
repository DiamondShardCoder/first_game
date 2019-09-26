from random import randint

def calc_monster_dmg(dmg_min, dmg_max):
    return randint(dmg_min, dmg_max)

def game_winner(winner_name):
    print(winner_name + ' has won!')

result = []

counter = 0

game_running = True

while game_running == True:
    player = {'name': 'input', 'attack_dmg': 15, 'health': 100, 'heal': 15}
    monster = {'name': 'Demon', 'attack_dmg_min': 10, 'attack_dmg_max': 20, 'health': 100}
    
    counter += 1

    monster_won = False
    player_won = False

    new_round = True

    print('---' * 7)
    player['name'] = input('Enter player name: ')

    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')
    print('---' * 7)

    while new_round == True:
        print('1) Attack')
        print('2) Heal')
        print('3) Exit')
        print('4) Result')

        player_choise = input('Enter your option: ')

        if player_choise == '1':
            player['health'] = player['health'] - calc_monster_dmg(monster['attack_dmg_min'], monster['attack_dmg_max'])
            monster['health'] = monster['health'] - player['attack_dmg']
            print('---' * 7)
            print(player['name'] + ' has ' + str(player['health']) + ' health')
            print(monster['name'] + ' has ' + str(monster['health']) + ' health')
            print('---' * 7)
            
            if player['health'] <= 0:
                monster_won = True
                player_won = False
                new_round = False
            
            elif monster['health'] <= 0:
                player_won = True
                monster_won = False
                new_round = False
            
            else:
                new_round = True
        
        elif player_choise == '2':
            player['health'] = player['health'] + player['heal']
            player['health'] = player['health'] - calc_monster_dmg(monster['attack_dmg_min'], monster['attack_dmg_max'])
            print(player['name'] + ' has ' + str(player['health']) + ' health')
            print(monster['name'] + ' has ' + str(monster['health']) + ' health')
            
            if player['health'] <= 0:
                monster_won = True
                player_won = False
                new_round = False
            
            elif monster['health'] <= 0:
                player_won = True
                monster_won = False
                new_round = False
                
            else:
                new_round = True
                
        elif player_choise == '3':
            new_round = False
            game_running = False
        
        elif player_choise == '4':
            for game_results in result:
                print(game_results)
        
        else:
            print('Invalid input')
        
        if player_won:
            game_winner(player['name'])
            round_results = (player['name'] + ' had ' + str(player['health']) + ' HP' + ' and ' + monster['name'] + ' had ' + str(monster['health']) + ' HP!')
            result.append(round_results)
            new_round = False

        elif monster_won:
            game_winner(monster['name'])
            round_results = (player['name'] + ' had ' + str(player['health']) + ' HP' + ' and ' + monster['name'] + ' had ' + str(monster['health']) + ' HP!')
            result.append(round_results)
            new_round = False

    if counter == 1:
        print(str(counter) + ' fight completed!')
    else:
        print(str(counter) + ' fights completed!')


        
        
    



    


            

        
            
        
        





    


