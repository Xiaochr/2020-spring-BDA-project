import json


data = {"Berlin": [13.40, 52.52], "Frankfurt": [8.68, 50.11], "Muechen": [11.58, 48.14], 
        "Hamburg": [9.99, 53.55], "Bremen": [8.80, 53.08], "Dresden": [13.44, 51.02], 
        "Hannover": [9.43, 52.22], "Koeln": [6.58, 50.56], "Mainz": [8.16, 50.00], "Stuttgart": [9.11, 48.47]}

json_data = json.dumps(data)
with open("./data/city_coor.json", "w") as f:
    f.write(json_data)
