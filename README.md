# pieplot_eda
Generate pie plots to show energy values from LMOEDA analysis 

LMOEDA analysis (Su2009, Su2012, Su2014, Su2020) is used to decompose interaction energies between molecules, and is implemented in the quantum chemistry package GAMESS-US, https://www.msg.chem.iastate.edu/gamess/

The analysis yields interaction energy values, such as these:

 -------------
 OWN BASIS SET                                       HARTREE          KCAL/MOL
 -------------
 ELECTROSTATIC ENERGY                  ES=         -0.688593           -432.10
 EXCHANGE ENERGY                       EX=         -0.176962           -111.05
 REPULSION ENERGY                     REP=          0.390004            244.73
 POLARIZATION ENERGY                  POL=         -0.324303           -203.50
 MP2 DISPERSION ENERGY               DISP=         -0.064149            -40.25
 TOTAL INTERACTION ENERGY HF OR DFT     E=         -0.799854           -501.92
 TOTAL INTERACTION ENERGY MP2           E=         -0.864003           -542.17
  

 -------------
 ALL BASIS SET                                       HARTREE          KCAL/MOL
 -------------
 ELECTROSTATIC ENERGY                  ES=         -0.687475           -431.40
 EXCHANGE ENERGY                       EX=         -0.176203           -110.57
 REPULSION ENERGY                     REP=          0.387366            243.08
 POLARIZATION ENERGY                  POL=         -0.322565           -202.41
 MP2 DISPERSION ENERGY               DISP=         -0.059998            -37.65
 TOTAL INTERACTION ENERGY HF OR DFT     E=         -0.798877           -501.30
 TOTAL INTERACTION ENERGY MP2           E=         -0.858875           -538.95

This python scripts plots these interaction energies as a pie chart.

Requirements: python3 and the following packages: argparse, re, matplotlib
To install these:
>pip3 install argparse, re, matplotlib

To run the script:
>python3 pieplot_eda.py (arguments)

