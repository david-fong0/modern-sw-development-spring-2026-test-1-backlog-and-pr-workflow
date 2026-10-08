# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

#Security Audit: Hardcoded credentials present a security vulnerability.
#Fix: SECRET_CODE variable was removed
p_hp = 50
b_hp = 50
MAX_HP = 50

#Attack function already functional
def attack():
    global b_hp
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

#Heal function already functional
def heal():
    global p_hp
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    p_hp += 20
    if p_hp > MAX_HP:
        p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")

    #Security Audit: Removed the [c]heat option from input prompt
    choice = input("Action [a]ttack, [h]eal: ").lower()

    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()
    else:
        print("Invalid choice! Please choose 'a' or 'h'.")

    #Win Condition that displays Victory! or Game Over! based on if the player or boss dies first
    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
