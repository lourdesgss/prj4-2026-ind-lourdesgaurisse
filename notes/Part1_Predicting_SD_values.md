
# Predicting Colour (SD) Based on Parameters

The first part of the assignment is designing a model that will predict the colour (SD value, a number between 0 and 1) given a set of parameters for the **typical nozzle** given:
- **Color** (C, M, Y, K – categorical)
- **Voltage (V)** – per‑chip parameter
- **Flank ratio (F_r)** – per‑chip parameter
- **Delta t2 (dt2)** – per‑nozzle parameter (but for a "typical nozzle", you treat it as an input)
- **Coverage** – amount of ink (6 levels)

The output is a single **SD value**.  For a "typical nozzle", we should **average across all nozzles in a chip** for each unique combination of parameters.

The assignment says: _"predicts colour that a typical nozzle would produce"_, which means **ignore nozzle‑to‑nozzle variation** (for the core model). You do **not** need to identify high‑std nozzles for this core model. That analysis is only for the _extension_ (customising waveforms per nozzle to improve macro‑uniformity). 

## Aggregating Correctly

So far, I have aggregated the dataset in the following way:

For each unique combination of `(Color, HeadIdx, V, F_r, dt2, Coverage)`:

- Compute the **mean** of each nozzle’s SD across 6 sheets → `Value_xxx_mean`
- Compute the **standard deviation** of each nozzle’s SD across sheets → `Value_xxx_std`
- Drop nozzles 1120‑1135.
- Drop groups without exactly 6 sheets.

The following step for this core model is to collapse the 1120 nozzle means into one number per group (the average SD across nozzles -> the **typical nozzle**).



