import pandas as pd
import math


def trhist_file_handler(file : str, val = "p") ->pd.core.frame.DataFrame:
    # This function provide extraction data from LS-DYNA trhist file to Pandas DataFrame
    # Code automaticly detect number of passed trhist sensors and provide extraction of several values:
    # X, Y, Z, Vx, Vy, Vz, efp, rho, rvol, active
    # additionaly calulation of pressure is providet by key "p"

    f = open(file)
    lines = f.readlines()

    val_ids ={"x": 1,       "y": 2,       "z": 3,      "vx": 4,      "vy": 5,      "vz": 6,
      "sx": 7,      "sy": 8,      "sz": 9,     "sxy": 10,     "syz": 11,     "szx": 12,
     "efp": 13,     "rho": 14,    "rvol": 15,  "active": 16, "p": "p"}
    val_id = val_ids[val]
    numofcurves = 0
    numofvals = 0
    for i in range(len(lines[1])):
        if (lines[1][i+1] ==" " and  lines[1][i] !=" "):
            numofcurves = int(''.join(lines[1][:i+1].split()))
            numofvals = int(''.join(lines[1][i+1:].split()))
            break
    out_dict = {"t": []}
    for i in range(numofcurves):
        out_dict["trhist"+str(i+1)+", "+val] = []
    skiprow = 0
    for i in range(len(lines)):
        if "0.00000E+00" in lines[i]:
            skiprow = i
            break
    rows_of_one_trhist = math.ceil(numofvals/6)
    all_trhists_block = rows_of_one_trhist* numofcurves
    if val != "p":
        pointer = [math.ceil(val_id/6), val_id%6]
    else:
        pointer = [math.ceil(val_ids["sx"] / 6-1), val_ids["sx"] % 6-1]
    for i in range(skiprow,len(lines)):

        if((i - skiprow) % (all_trhists_block+1) == 0):
            out_dict["t"].append(float(lines[i]))
            for j in range(numofcurves):
                try:
                    frst_row = list(map(float, lines[i + j*rows_of_one_trhist+  1].split()))
                except:
                    frst_row = [0,0,0,0,0,0]
                try:
                    scnd_row = list(map(float, lines[i + j*rows_of_one_trhist+  2].split()))
                except:
                    scnd_row = [0,0,0,0,0,0]
                try:
                    thrd_row = list(map(float, lines[i + j*rows_of_one_trhist+  3].split()))
                except:
                    thrd_row = [0, 0, 0, 0, 0, 0]
                loc_rows = [frst_row,scnd_row,thrd_row]
                if val != "p":
                    extracted_value = loc_rows[pointer[0]][pointer[1]]
                else:
                    extracted_value = -(loc_rows[pointer[0]][pointer[1]] + loc_rows[pointer[0]][pointer[1]+1] + loc_rows[pointer[0]][pointer[1]+2])/3
                out_dict["trhist"+str(j+1)+", "+val].append(extracted_value)
    df = pd.DataFrame(out_dict)
    return df

#Example code
if __name__ == "__main__":
    filename = "trhist"
    value_to_extract = "p"

    mydf = trhist_file_handler(file = filename, val = value_to_extract)
    print(mydf)
