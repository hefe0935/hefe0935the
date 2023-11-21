import json

liste = []
listenumaralı = []

# Load the lists from a file if it exists
try:
    with open("data.json", "r") as file:
        data = json.load(file)
        liste = data["liste"]
        listenumaralı = data["listenumaralı"]
except FileNotFoundError:
    pass

while True:
    arama1 = input("Aranacak eşyayı giriniz: ")
    
    if arama1 in liste:
        index = liste.index(arama1)
        print(arama1 + " listede bulundu! Raf: " + listenumaralı[index])
    elif arama1 == "liste":
        print(liste)
    elif arama1 == "liste ekle":
        ekle1 = input("Eklemek istediğiniz eşyayı giriniz:")
        rafnumara = input("Raf numarasını giriniz:")
        listenumaralı.append(rafnumara + ": " + ekle1)
        liste.append(ekle1)
        print("raf" + rafnumara + ": " + ekle1 + " eklendi")
    else:
        found = False
        for item in listenumaralı:
            if arama1 in item:
                found = True
                print(item)
                break
        if not found:
            print("Sonuç Bulunamadı")
    
    devam = input("Devam etmek istiyor musunuz? (E/H): ")
    if devam.lower() != "e":
        # Save the lists to a file before closing the program
        with open("data.json", "w") as file:
            data = {"liste": liste, "listenumaralı": listenumaralı}
            json.dump(data, file)
        break