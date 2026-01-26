import numpy as np #import numpy to create arrays
from astropy.table import Table #make tables using astropy

variablex = np.arange(0.0062831853, ((2*np.pi)-0.00627690212), 0.00627690212)
# non-inclusive range from (0,2) with step size for 1000 steps
sine_variablex = np.sin(variablex)

sine_table = Table()
sine_table['x'] = variablex
sine_table['sin(x)'] = sine_variablex

sine_table['x'].format = "{:.3f}"
sine_table['sin(x)'].format = "{:.3f}"

def main():
    print(sine_table)

if __name__=='__main__':
    main()