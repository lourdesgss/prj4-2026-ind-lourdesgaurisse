# Canon Presentation

### PRINTER DETAIL

A printer has 8 print heads for every colour in [C, M, Y, K]

- Every print head has 4 chips.
- 32 chips in total, but we skip 0 and 31, leaving us with 30 individual chips.
- Every chip has 1136 nozzles, with the final 16 nozzles overlapping → so 1120 nozzles used

### WAVEFORM DETAILS

3 parameters to tune:

- Voltage
- Flank ratio
- Delta t2 (dt2)
- Voltage and Flank ratio are per chip parameters
- dt2 is a per nozzle parameter

### WHAT TYPE OF PRINTS ARE USED TO GET DATA

- Up front, a Voltage and Flank ratio were defined, e.g. {22, 1.02}, {24, 1.28} etc.
- 5 dt2 are defined up front: [-1100, -900, -700, -500, -300]
- For a set of prints, every chip for every colour is given the same {V, F_r}
- On every sheet 6 ‘coverages’ (amount of ink) are printed
- Every coverage is printed 5 times, once using a different dt2 from the above list for every single nozzle
- This means every sheet has 30 ‘sets’ of data per chip for a given {V, F_r}
- Every sheet is printed 6 times with the exact same settings

### WHAT IS BEING MEASURED

When such a test chart is printed:

- The scanner scans the sheet, processing is done:
- For every nozzle (1120), in every chip (30)
- A Scanner Density (SD) value is logged, for every single coverage (also 30).
- This means 1 sheet gives us 1120 ∗ 30 ∗ 30 = 1,008,000 SD values
- Scanner Density tells us something about how dark a colour is:
- 0 means there is no colour at all
- 1 means the darkest possible colour

### DATA SET

- 4 colors
- 30 chips per color
- 1120 nozzles per chip
- 30 different {V, F_r} combinations
- 5 dt2 per {V, F_r}
- 6 coverage levels per {V, F_r, dt2}
- 6 repeated sheets per waveform set
- Total of: 4 ∗ 30 ∗ 1120 ∗ 30 ∗ 5 ∗ 6 ∗ 6 = 725,760,000 individual samples

### THINGS TO KEEP IN MIND

- Different colors behave differently
- Every single chip behaves differently
- Every nozzle in a chip behaves slightly differently
- Scanner resolution is lower than print resolution:
- Ink from neighboring nozzles influences SD measurement of a nozzle
