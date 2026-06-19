# Final Reflection

## Overview

With the project drawing to a close, the final stretch of work shifted from further model development toward consolidation and communication. Together with a classmate, we built a simple frontend on top of the `HardwarePredictor`/`NeuralPredictor` system, designed specifically to demonstrate the different models we'd developed over the course of the project to a non-technical audience during the presentation. Rather than presenting raw metrics and notebooks, the interface lets a user set the physical input parameters (Voltage, F_r, dt2, Color) and immediately see the resulting per-chip and full 33,600-nozzle waveform predictions rendered as interactive charts, with an option to export results to CSV. Splitting the work this way let us move quickly while keeping the presentation grounded in something tangible.

## Reflection

Looking back across the whole project, the trajectory from independent-row regression, through spatial CNNs, to a physically-grounded baseline-plus-coupling formulation, taught me as much about the value of stepping back to question assumptions as it did about the specific modelling techniques themselves. The chip-grid issue uncovered partway through is a good example: it would have been easy to keep iterating on architecture without ever noticing that the spatial axis itself was being misused.

Although the project's official timeline has now ended, I don't consider the problem closed for myself. The coupling-network formulation in particular feels like it's only scratched the surface of what's possible, as there are still open questions around the unmeasured physical domains (thermal, alignment, manufacturing tolerances) that I'd like to explore further, and I intend to keep working on this independently, both because I find the problem genuinely interesting and because I think there's more headroom in the physically-motivated approach than the project timeline allowed us to explore.

## Evidence

- [NiceGUI Predictor Frontend](../evidence/code/predictor_frontend.py)