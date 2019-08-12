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

# Using the Python code

In the Python code example you can generate any function you would like. Simply change the following code with your function. 

str(bin(int(     Your function goes here(l/N)         )))[2:].zfill(8)

The "l/N" allows you to sample your function on the interval [0,1] sampled uniformly N times. This is assuming that floats are being used as the input of your function. The "zfill(8)" is to fill the rest of the string with 0's until we reach 8-bits. You could change the 8 to 10 if you would like to use 10 bits instead. 

# Adding a DAC to the project

The following code is to put the output of our module into an 8-bit DAC. A simple DAC can be constructed out of a resistor ladder connected to 8-pins of the FPGA. In your Top module you will need to add "output [0:7] DAC". Which will make the 8-pins an output for your FPGA. I've added my .utc file for alocating those 8 pins to the DAC. The following code is just an example instance for adding the module to your top-module. 

wire [7:0] DAC_q;

assign DAC = DAC_q;

Signal_ROM Signal (

  .clk(clk),
  
  .Signal_out(DAC_q)
  
);
