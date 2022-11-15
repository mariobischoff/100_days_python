enemies = 1

def increase_enemies():
    global enemies
    enemies += 1 
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

# Global Scope
# player_health = 10
# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# game_level = 3
# def create_enemy():
#     enemies = ["skeleton", "zombie", "alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

# print(new_enemy)