from variables import *
import yaml
import json 

with open ("./archivos/avatar.json", "r") as file:
    json_data = json.load(file)
    #print(json_data)

nombres = json_data["personajes"]
for nombre in nombres:
    print(nombre["nombre"])

for alias in nombres:
    if alias["alias"] is None:
        print(alias["nombre"], ": No tiene alias")
    else:
        print(alias["nombre"], "alias:", alias["alias"])

yaml_dump = yaml.dump(json_data, indent=2, allow_unicode=True, sort_keys=False)

with open("./archivos/avatar.yaml", "w") as file:
    file.write(yaml_dump)

print("Archivo YAML guardado")