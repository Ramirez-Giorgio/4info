MappaRegioni = {
    "lombardia": ["milano", "bergamo", "brescia", "como"],
    "lazio": ["roma", "latina", "frosinone"],
    "sicilia": ["palermo", "catania", "lampedusa"]
}

def cerca():
    provincia = input("provnicia: ").lower()
    trova=0
    for regione, province in MappaRegioni.items():
        if provincia in province:
            print(f"{provincia} è in {regione}")
            trova=1
            break
    if trova==0:
        print("Provincia non presente")

cerca()