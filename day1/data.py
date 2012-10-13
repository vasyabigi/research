description = [
    'AngleDegree',
    'DegRel',
    'Angles',
    'Length',
    'LenRel',
    'LInterval',
    'LInterRel',
    'Thickness',
    'ThickRel',
    'NodeStack',
    'ClustSize',
    'ClustQty',
    'Triangles',
    'Connectiv',
    'HurstPnts',
    'HurstExp',
    'Ass.Nmn',
    'Ass.Stud'
]

result_data = list()
with open("result_data.txt", "r") as f:
    lines = f.readlines()
    for line in lines[31:]:
        result_data.append(line.replace(" ", "").split("\t")[:19])

result_data_reversed = list()
with open("result_data_reversed.txt", "r") as f:
    lines = f.readlines()
    for line in lines[31:]:
        result_data_reversed.append(line.replace(" ", "").split("\t")[:19])

result_data_shuffled = list()
with open("result_data_shuffled.txt", "r") as f:
    lines = f.readlines()
    for line in lines[31:]:
        result_data_shuffled.append(line.replace(" ", "").split("\t")[:19])
