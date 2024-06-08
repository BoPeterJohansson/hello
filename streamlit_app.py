import streamlit as st

from random import randint

# Välkommstfras och spelbeskrivning
def welcome_message():
    print(f'''
        {70 * "="}
        Wohahaha, välkommen till zombiehuset!
        Du har blivit inlåst i ett hus fullt av zombies.
        För att ta dig ut måste du svara rätt på matematiska frågor.
        Om du inte väljer rätt dörr ut ur rummen blir du uppäten av zombies.
        Lycka till!
        {70 * "="}
        ''')

# Slumpar fram en unik faktor
def get_unique_factor(used_factors):
    while True:
        factor = randint(0, 12)
        if factor not in used_factors:
            used_factors.append(factor)
            return factor

def input_multiplication_question(tabell, factor):
    # Multiplicerar spelarens valda tabell med en slumpad faktor
    produkt = tabell * factor
    # Frågar efter spelarens svar
    svar = int(input(f"\nVad blir {tabell} * {factor}? "))
    return svar == produkt

# Slumpar dörren zombiesarna gömmer sig bakom och ber spelaren välja dörr
def input_zombie_door_selection(frågor):
    if frågor == 0:
        return 0, 0  # Inga zombies bakom den sista dörren
    zombies = randint(1, frågor + 1)
    print(f"Du har {frågor + 1} dörrar framför dig. Bakom en dörr väntar zombiesarna.")

    while True:
        dörr = int(input(f"Vilket dörr väljer du? (1-{frågor + 1}): "))
        if dörr == 0:
            print(f"Hallå dummer, du kan inte välja dörr 0!\nVälj en dörr mellan 1 och {frågor + 1}.")
        elif dörr > (frågor + 1):
            print(f"Hallå dummer, du måste välja en dörr mellan 1 och {frågor + 1}.")
        else:
            break

    return dörr, zombies

def input_play_game():
    # Antalet frågor spelaren har kvar att svara på
    frågor = 12
    # Slumpade faktorer som redan använts för att förhindra upprepning
    faktorer = []
    # Spelarens valda multiplikationstabell
    tabell = int(input("Välj en multiplikationstabell! (2-12): "))

    # Initierar en loop för antal frågor
    for _ in range(frågor):
        factor = get_unique_factor(faktorer)

        # Kollar utfallet av spelarens svar
        if input_multiplication_question(tabell, factor):
            print("\nRätt svar!")
            frågor -= 1
        else:
            print("\nDu har blivit uppäten av en zombie!")
            return

        dörr, zombies = input_zombie_door_selection(frågor)

        if frågor == 0:
            print("Grattis! Du har svarat rätt på alla frågor och klarat dig ur zombiehuset!")
            return

        if dörr != zombies:
            print(f"Du klarade dig den här gången, zombiesarna var bakom dörr {zombies}!")
            print(f"Du har svarat rätt på {12 - frågor} frågor och har {frågor} frågor kvar.")
        else:
            print("Du har klivit rakt in i ett rum fullt av zombies!")
            return

# Huvudprogram
def main():
    nytt_spel = "j"
    while nytt_spel == "j":
        welcome_message()
        input_play_game()

        # Frågar spelaren om vill spela igen
        nytt_spel = input("Vill du spela igen? (j/n) ")

    # Fras om spelaren väljer att inte fortsätta spela
    print("\nFegis!")
    print("Vi ses när du har samlat mer mod...hahaha!")

if __name__ == "__main__":
    main()