from models.Engine import Engine

datas = ["titi", "tata", "2023-12-18"]
options = ["upper", "lower", "capitalize", "accent", "date", "leet", "char"]
engine = Engine(datas, options)
print(engine.passwords)
