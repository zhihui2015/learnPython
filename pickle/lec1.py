import pickle

game_data = {
    "position": "N2 E3",
    "pocket": ["keys", "knife"],
    "money": 160,
    "agp": (18, 35)
}

save_file = open("save.dat", "wb")
pickle.dump(game_data, save_file)
save_file.close()

load_file = open("save.dat", "rb")
load_game_data = pickle.load(load_file)
print(load_game_data)
load_file.close()

