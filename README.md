# Signal-Generator-on-FPGA
This is just a quick signal generator that I made. I have a feeling it will be useful in future projects as a selectable signal generator to test different signals.

The important bit of code for changing which signal the signal generator is using is at the bottom of the Signal_ROM.v file. Simply replace n with the number of which signal you would like to select. 

signal_q <= Signal [n][addr];

right now:
n=0 is a sine wave;
n=1 is a hyperbolic tangent wave;
n=2 is an arctangent wave.

The period or time it takes for the signal to repeat itself can be calculated via 1/(Clock Speed/Samples)

In this case my clock speed is 50MHz, and the number of samples of each chosen wave form is 256. 
Thus, the expected period is 1/(50MHz/256) = 1/(196kHz)
or 195000 times per second. 
