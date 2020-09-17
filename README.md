# About
Nothing too complicated, just testing out a very basic integration of PostgreSQL with puthon

# Pre-requisites 
you will have to install the tabulate library if you want the output in table form. Trust me, it will be very ugly otherwise.

` pip install tabulate `

If you are having trouble or simply do not want to download the library:

* comment out the 'import tabulate' statement (line 2)

* comment out the  #print_using_table statement (line 34)

* uncomment the '#print_without_table' block of code. (lines 37-40)

## ERRORS
If you rerun the code, you will have to drop the table by uncommenting line 16 because the table will already exist, and therefore line 17 will fail.

