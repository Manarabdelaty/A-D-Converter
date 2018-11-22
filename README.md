# A-D-Converter

8 bit A/D Converted with sampling rate of 40 samples/sec </br>

I.	Sampling is done by taking evenly distant 40 samples from the time axis as follows: 
The distance between any two samples is 0.025 (1/sampling_frequence) </br>

![we](https://user-images.githubusercontent.com/25064257/48903753-15398980-ee65-11e8-90f8-f7a877b3345f.png)

II.	The sampled sin signal is computed as follows : </br>

![ee](https://user-images.githubusercontent.com/25064257/48903770-22ef0f00-ee65-11e8-9a98-f164f7fd4b76.png)

III.	After sampling, the signal is quantized by approximating the value of the sampled signal to the nearest level as follows:
First the number of levels is calculates as 2number of bits which is 28=256. Then, the LSB is calculated as 2/number of levels since the sine waves spans between 1 and -1 which gives an absolute value of 2 voltage. </br>

![ee](https://user-images.githubusercontent.com/25064257/48903841-52058080-ee65-11e8-869c-ba6363d89c48.png)

IV.	The quantized signal is plotted in the same graph as the analog signal as shown in plot.2

![we](https://user-images.githubusercontent.com/25064257/48903849-56319e00-ee65-11e8-9458-5da22f837f67.png)



