# midiFill

This repository helps in creating transitions between midi tracks with deep learning. It contains functionality to scrape and process a midi dataset, partly using Kevin-Yang's (@jason9693) repository [here](https://github.com/jason9693/midi-neural-processor), and then train a transformer on the data using a modified version of the music tranformer as implemented by Damon Gwinn, Ben Myrick and Ryan Marshall [here](https://github.com/gwinndr/MusicTransformer-Pytorch). To create transitions instead of causally predicting the next token based only on the previous ones, masking is written so that the transformer has access to a random number of the following tokens as well. The idea behind this is that is learns to fill in an arbitrary number of notes up until the next track starts.

## How to use
1. Find a midi dataset or ask a webmaster permission to scrape their data.
2. Process it as per the instructions from the [Music Transformer](https://github.com/gwinndr/MusicTransformer-Pytorch)
3. Same goes for the training. Although this repository contains a modified version, training should still work

## Results
The loss of this version is, as expected, better than the original because the model has access to more data. In practice though, it appears to have learned mostly to repeat previous sequences of notes and is not yet in a state to produce good transitions, and is thus still work-in-progress. On an AMD Radeon W7900 with ROCm drivers, training 100 epochs took around 10 hours.

![](https://github.com/file-acomplaint/midiFill/blob/main/MusicTransformer-Pytorch/loss_graph.png?raw=true)
