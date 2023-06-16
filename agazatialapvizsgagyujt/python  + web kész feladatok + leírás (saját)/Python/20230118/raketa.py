hours = int(input("Hány órás visszaszámlálást tervezünk? "))

count = 0
for i in range(hours, 0, -1):
    print(f"Visszaszámlálás {i}")
    cancel = input("Fel kell függeszteni a visszaszámlálást (i/n)? ")
    if cancel == "i":
        count += 1
print(f"A rakéta a visszaszámlálást követően ennyi órával indult: {count + hours}")