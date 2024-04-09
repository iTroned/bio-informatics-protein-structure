# Bio-informatics: Predicting secondary structure of a protein.
## Information 
Unfortunately, the program will perform different on different systems. When launching the software for the first time, it will take some time as it installs all the needed the dependencies for the program to use the model for predictions.
### Known bugs:
    The first time the user presses predict, the program will freeze. 
    This is because the model is initialized, please be patient and not close the program.
    Windows will most likely flag the program as unsafe, as it is missing a digital signature.
### System requirements:
    Operating system: Windows
### Recommended requirements:
    Graphics card: A CUDA compatible graphics card: https://developer.nvidia.com/cuda-gpus
    If no graphics card is found, the software will default and use the CPU. However, all predictions will take longer on the CPU.
    
## Download and use the program:
Installation guide: https://www.youtube.com/watch?v=_ZsMhehQh8I
You can download the software here: https://github.com/iTroned/bio-informatics-protein-structure/releases/tag/v1.0.0

To use the program is very straight forward:

1. Open the downloaded .exe file.
2. Wait for the installation to be complete, this may take some time depending on your internet and computer specification.
3. Press predict once, to freeze the program and make it ready for predictions.
4. Paste in sequences in the text box, and press predict.
5. Output is the secondary structure prediction: C: Random coil, E: Beta sheet and H: Alpha Helix.
