from numpy import array


class Column:
    ANGLE_DEGREE = 0
    DEG_REL = 1
    ANGLES = 2
    LENGTH = 3
    LEN_REL = 4
    L_INTERVAL = 5
    L_INTER_REL = 6
    THICKNESS = 7
    THICK_REL = 8
    NODESTACK = 9
    CLUST_SIZE = 10
    CLUST_QTY = 11
    TRIANGLES = 12
    CONNECTIV = 13
    HURST_PNTS = 14
    HURST_EXP = 15
    ASS_NMN = 16
    ASS_STUD = 17


result_data = list()
with open("result_data.txt", "r") as f:
    lines = f.readlines()
    for line in lines[31:]:
        result_data.append(line.replace(" ", "").split("\t")[:19])
result_data = array(result_data).transpose()

result_data_reversed = list()
with open("result_data_reversed.txt", "r") as f:
    lines = f.readlines()
    for line in lines[31:]:
        result_data_reversed.append(line.replace(" ", "").split("\t")[:19])
result_data_reversed = array(result_data_reversed).transpose()

result_data_shuffled = list()
with open("result_data_shuffled.txt", "r") as f:
    lines = f.readlines()
    for line in lines[31:]:
        result_data_shuffled.append(line.replace(" ", "").split("\t")[:19])
result_data_shuffled = array(result_data_shuffled).transpose()
