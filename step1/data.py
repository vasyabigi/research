from numpy import array


class Column:
    ANGLE = 0
    DEGREE = 1
    DEG_REL = 2
    ANGLES = 3
    LENGTH = 4
    LEN_REL = 5
    L_INTERVAL = 6
    L_INTER_REL = 7
    THICKNESS = 8
    THICK_REL = 9
    NODESTACK = 10
    CLUST_SIZE = 11
    CLUST_QTY = 12
    TRIANGLES = 13
    CONNECTIV = 14
    HURST_PNTS = 15
    HURST_EXP = 16
    ASS_NMN = 17
    ASS_STUD = 18

# Results for array with 10 000 points
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


# Results for array with 50 000 points
big_result_data = list()
with open("big_data_results.txt", "r") as f:
    lines = f.readlines()
    for line in lines[31:]:
        big_result_data.append(line.replace(" ", "").split("\t")[:19])
big_result_data = array(big_result_data).transpose()

big_result_data_reversed = list()
with open("big_data_reversed_results.txt", "r") as f:
    lines = f.readlines()
    for line in lines[31:]:
        big_result_data_reversed.append(line.replace(" ", "").split("\t")[:19])
big_result_data_reversed = array(big_result_data_reversed).transpose()

big_result_data_shuffled = list()
with open("big_data_shuffled_results.txt", "r") as f:
    lines = f.readlines()
    for line in lines[31:]:
        big_result_data_shuffled.append(line.replace(" ", "").split("\t")[:19])
big_result_data_shuffled = array(big_result_data_shuffled).transpose()
