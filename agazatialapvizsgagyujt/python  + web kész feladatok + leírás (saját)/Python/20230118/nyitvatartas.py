time = int(input("Hány óra van most? "))

if time >= 8 and time < 16:
    print("A bolt nyitva van")
    print(f"Ennyi órád van még odaérni: {16-time}")
else:
    print("A bolt zárva van")