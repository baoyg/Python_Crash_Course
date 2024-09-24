# alien_0只包含一个外星人信息
# 如果是一群外星人呢？
# 创建一个外星人列表，每个外星人都是一个字典

alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 实际上外星人有很多，每个外星人都是代码自动生成的

aliens = []

for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print('...')

# print(f"Total number of aliens:{len(aliens)}.")
