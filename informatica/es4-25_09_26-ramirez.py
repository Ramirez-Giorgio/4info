#tavola pitagorica 
print("tavola pitagorica")
d = 10
for r in range( d + 1):
    for c in range( d + 1):
        prodotto = r * c
        print(f"{prodotto:5}", end="")# Il :3 indica di riservare 3 spazi per il numero, allineandolo a destra
    print("\n")
print("\n\n\n\n")
for r in range( d + 1):
    for c in range( d + 1):
        prodotto = r + c
        print(f"{prodotto:5}", end="")# Il :3 indica di riservare 3 spazi per il numero, allineandolo a destra
    print("\n")