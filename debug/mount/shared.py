import random

#Code om een valide BSN te genereren
def is_valid_bsn(bsn):
    #Controleer of een BSN voldoet aan de elfproef.
    total = 0
    bsn_str = str(bsn).zfill(9)  # Zorg ervoor dat het BSN 9 cijfers bevat
    for i, digit in enumerate(bsn_str):
        multiplier = 9 - i if i < 8 else -1
        total += int(digit) * multiplier
    return total % 11 == 0

def generate_valid_bsn():
    #Genereer een geldig BSN dat voldoet aan de elfproef.
    while True:
        bsn = random.randint(100000000, 999999999)  # Genereer een willekeurig 9-cijferig getal
        if is_valid_bsn(bsn):
            return str(bsn)

# Genereer een geldig BSN en print deze
# valid_bsn = generate_valid_bsn()
# print(f"Een geldig BSN: {valid_bsn}")