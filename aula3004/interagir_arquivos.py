with open('./resultados.csv', 'w') as file:
    try:
        file.write("aloha")
        print("a" + 1)
        file.write("tchau")
    except:
        print("Deu ruim")
