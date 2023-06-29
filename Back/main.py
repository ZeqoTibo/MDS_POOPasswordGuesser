from models.Engine import Engine

datas = ["test", "testouille", "tibo", "chien", "arrivé", "AEYOUYG", "2023-12-18"]

# print(len(Engine(datas, ["upper"]).passwords))
# print(len(Engine(datas, ["upper", "lower"]).passwords))
# print(len(Engine(datas, ["upper", "lower", "capitalize"]).passwords))
# print(len(Engine(datas, ["upper", "lower", "capitalize", "accent"]).passwords))
print(Engine(datas, ["upper", "lower", "capitalize", "accent", "date"]).passwords)
