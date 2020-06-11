name = input("Guten Tag! Wie heißt du? ")

while True:
    print("Hi " + name + ", das hier ist ein Helferlein, der dir Kilometer in Meilen umrechnet.")
    km = int(input("Bitte tippe die Kilometerzahl ein, die du umrechnen möchtest: "))
    mile = int(km * 0.621371)
    print(mile)
    Auswahl = input("Möchtest du noch eine Kilometerzahl in Meilen umrechnen? ")
    if Auswahl != "ja":
        break