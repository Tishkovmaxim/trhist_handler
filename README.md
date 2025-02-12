# TRHIST_HANDLER
This code provide extraction data from LS-DYNA trhist file to Pandas DataFrame
Code automaticly detect number of passed trhist sensors and number of passed values.

To use function trhist_file_handler you need to specify path to trhist file and desireble value to extract.

The following keys are currently available:
* "x" - x coordinate
* "y" - y coordinate
* "z" - z coordinate
* "vx" - x velocity
* "vy" - y velocity
* "vz" - z velocity
* "sx" - x normal stress
* "sy" - y normal stress
* "sz" - z normal stress
* "sxy" - xy shear stress
* "syz" - yz shear stress
* "szx" - zx shear stress
* "efp" - effective plastic strain
* "rvol" - reference volume
* "active" - element number
* "p" - pressure (this value is calculated by (sx + sy + sz)/3)
