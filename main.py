import pydealer
talia = pydealer.Deck()
talia.shuffle()
Gracz1 = talia.deal(26)
Gracz2 = talia.deal(26)
print(Gracz1)
print("--------------")
print(Gracz2)
for i in range (4):
    if Gracz1[i]> Gracz2[i]:
        print(f"Wygrał gracz1 w pojedynku {Gracz1[i]} vs {Gracz2[i]}")

    elif Gracz1[0]< Gracz2[0]:
        print(f"Wygrał gracz2 w pojedynku {Gracz1[i]} vs {Gracz2[i]}")
    else:
        print("Był remis")