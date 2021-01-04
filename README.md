# pieplot_eda
Generate pie plots to show energy values from LMOEDA analysis 

LMOEDA analysis (Su2009, Su2012, Su2014, Su2020) is used to decompose interaction energies between molecules, and is implemented in the quantum chemistry package GAMESS-US, https://www.msg.chem.iastate.edu/gamess/

The analysis yields interaction energy values. This python scripts plots these interaction energies as a pie chart.

Requirements: python3 and the following packages: argparse, re, matplotlib
To install these:
>pip3 install argparse, re, matplotlib

To run the script:
>python3 pieplot_eda.py (arguments)

Basic usage:
>python3 pieplot_eda.py lmoeda.log
replace lmoeda.log with your GAMESS output file name that contains LMOEDA analysis

If you want to plot the results for "own basis set"
>python3 pieplot_eda.py --plot_own lmoeda.log

References:

@Article{Su2009,
  Title                    = {Energy decomposition analysis of covalent bonds and intermolecular interactions},
  Author                   = {Su, P and Li, H},
  Journal                  = {J Chem Phys},
  Year                     = {2009},
  Pages                    = {014102},
  Volume                   = {131}
}

@Article{Su2012,
  Title                    = {{Free energy decomposition analysis of bonding and nonbonding interactions in solution}},
  Author                   = {Su, P. and Liu, H. and Wu, W. },
  Journal                  = {J Chem Phys},
  Year                     = {2012},
  Month                    = {Jul},
  Number                   = {3},
  Pages                    = {034111},
  Volume                   = {137}
}

@Article{Su2014,
  Author="Su, P.  and Jiang, Z.  and Chen, Z.  and Wu, W. ",
  Title="{{E}nergy decomposition scheme based on the generalized {K}ohn-{S}ham scheme}",
  Journal="J Phys Chem A",
  Year="2014",
  Volume="118",
  Number="13",
  Pages="2531--2542",
  Month="Apr"
}

@article{Su2020,
  author = {Su, Peifeng and Tang, Zhen and Wu, Wei},
  title = {Generalized Kohn-Sham energy decomposition analysis and its applications},
  journal = {WIREs Comput. Mol. Sci.},
  volume = {10},
  number = {5},
  pages = {e1460},
  year = {2020}
}
