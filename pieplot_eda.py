import argparse
import re
import matplotlib.pyplot as plt

# parse the arguments

parser = argparse.ArgumentParser(description='Generate a pie plot from LMOEDA output')
parser.add_argument('file', nargs=1,
                    help='GAMESS output file from an LMOEDA calculation')
parser.add_argument('--plot_own', dest='accumulate', action='store_const',
                    const='plot_own', default='plot_all_basis',
                    help='Generate plot of EDA with "OWN BASIS SET" (default: "ALL BASIS SET")')

args = parser.parse_args()
eda_file=args.file[0]

if args.accumulate == 'plot_own':
    b_plot_own=1
else:
    b_plot_own=0

# define a boolean to identify position in file
b_int_ener=0
b_own_basis=0
b_all_basis=0

# define lists that will be used in pyplot
labels=[]
data=[]
explode=[]

# open the file and extract all energy values
with open(eda_file) as f:
    for line in f:
        # check for the appearance of lines that define blocks to be handled
        if 'SUMMARY OF INTERACTION ENERGIES':
            b_int_ener=1
        if 'OWN BASIS SET' in line and b_int_ener:
            b_own_basis=1
        if 'ALL BASIS SET' in line and b_int_ener:
            b_all_basis=1
        if 'TOTAL INTERACTION ENERGY' in line and b_own_basis:
            b_own_basis=0
        if 'TOTAL INTERACTION ENERGY' in line and b_all_basis:
            b_all_basis=0
        
        # if we're in the correct reading block, get the type of energy
        if (
            ('ENERGY' in line or 'CORRELATION' in line) 
            and ((b_own_basis and b_plot_own) or (b_all_basis and not b_plot_own))
        ):
            line=line.replace('FREE','')
            nrg_type='NONE'
            nrg_val='NONE'
            match = re.search(r"\s+(\w.*)\s+ENERGY",line)
            if match:
                nrg_type = match.group(1)
            else:
            # matching something like this:
            # DFT CORRELATION                     CORR=...
            # in this case we want to match "DFT CORRELATION"
                match = re.search(r"\s+(\w.*)\s+(\w+=)",line)
                if match:
                    nrg_type = match.group(1)

            match = re.search(r"([-+]?[0-9]*\.?[0-9]+)$",line)
            if match:
                nrg_val = match.group(1)

            if (nrg_type != 'NONE' and nrg_val != 'NONE'):
                if '-' in nrg_val:
                    label = nrg_type + "\n" + nrg_val
                else:
                    label = nrg_type + "\n+" + nrg_val 
                # the labels will be type of energy + values
                labels.append(label)
                # convert value to int and add the absolute value to list
                nrg_val=float(nrg_val)

                if (nrg_val<0):
                    explode.append(0.)
                    nrg_val *=-1
                else:
                    explode.append(0.1)
            
                data.append(nrg_val)

if (not data):
    print ("No data to plot. Exiting")
    exit()

fig, ax = plt.subplots()
plt.pie(data, explode=explode, labels=labels, shadow=False, autopct='%1.1f%%')
ax.set_title("LMOEDA analysis, all values in kcal/mol")
plt.show()
