# Waveform Details & Parameter Interpretation
## Flank Ratio Variation
The higher the flank ratio (1.3) the steeper the rise and fall of the voltage framework becomes, causing pronounced peaks in certain conditions.
![Flank Ratio Modification][evidence/assets/initial-data-exploration/flank-ratio.png]

## Voltage Variation
Voltage directly affects the amount of electrical current given to each chip.
![Voltage Variation][evidence/assets/initial-data-exploration/voltage.png]
## dt2 Variation
dt2 measures the timing offset for the beginning of the voltage pulse.

| **Parameter**          | **dt2=−300**                        | **dt2=−1100**                         | **Effect of more negative dt2** |
| ---------------------- | ----------------------------------- | ------------------------------------- | ------------------------------- |
| **Zero-Volt Duration** | Longer (~$0.9 \ \mu\text{s}$)       | Shorter (~$0 \ \mu\text{s}$)          | **Reduces** dwell time at 0 V   |
| **Rising Edge Start**  | Starts later (~$2.4 \ \mu\text{s}$) | Starts earlier (~$1.5 \ \mu\text{s}$) | **Advances** the timing         |
| **Waveform Position**  | Standard                            | Shifted Left                          | **Accelerates** the cycle       |
![dt2 Variation] [evidence/assets/initial-data-exploration/dt2.png]
dt2 likely controls the delay of the first rising edge, while the rest of the waveform stays the same as a block. 