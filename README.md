# Bio-informatics: Predicting secondary structure of a protein.
## Information 
Unfortunately, the program will perform different on different systems. When launching the software for the first time, it will take some time as it installs all the needed the dependencies for the program to use the model for predictions.

## About the files:
    main.py: creation of the software application
    data_analyzis.ipynb: notebook with some data analysis and foundation for model training
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

[![Installation Guide](https://img.youtube.com/vi/_ZsMhehQh8I/0.jpg)](https://www.youtube.com/watch?v=_ZsMhehQh8I)

You can download the software here: https://github.com/iTroned/bio-informatics-protein-structure/releases/tag/v1.0.0

To use the program is very straight forward:

1. Open the downloaded .exe file.
2. Wait for the installation to be complete, this may take some time depending on your internet and computer specification.
3. Press predict once, to freeze the program and make it ready for predictions.
4. Paste in sequences in the text box, and press predict.
5. Output is the secondary structure prediction: C: Random coil, E: Beta sheet and H: Alpha Helix.

## Access the notebook:
DISCLAIMER: The dataset used is too big for Github. Please download it from here: https://www.kaggle.com/datasets/alfrandom/protein-secondary-structure?select=2018-06-06-ss.cleaned.csv

1. To access the notebook files it is recommended to set up your own dependency.
2. Download the ZIP file from Github.
3. Install anaconda: https://docs.anaconda.com/free/anaconda/install/windows/
4. Open conda:
5. conda create -n nyenv python=3.9
6. conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
7. python -m pip install "tensorflow<2.11"
8. Install all the dependencies in the list below:
9. Open VSCode through conda by writing code:
   
   ![image](https://github.com/iTroned/bio-informatics-protein-structure/assets/73116702/b23c45a4-786f-4e3b-99e7-39a63c0e2c9d)
10. Ctrl + Shift + P -> Open User Settings (JSON)
    
   ![image](https://github.com/iTroned/bio-informatics-protein-structure/assets/73116702/d6b9008e-af32-4ab4-b45b-a480a57903db)
   
11. Add this command at the bottom of the settings and save it: "terminal.integrated.inheritEnv": false

![image](https://github.com/iTroned/bio-informatics-protein-structure/assets/73116702/3833a937-352a-4eba-81d3-07886f2c518a)


 ## Dependencies
 | Library | Version |
 |---------|---------|
 | python | 3.9.19 |
 | numpy | 1.26.4 |
 | tensorflow | 2.10.1 |
 | pandas | 2.2.1 |
 | matplotlib | 3.8.3 |
 | pickleshare | 0.7.5 |
 | nltk | 3.8.1 | 
 | scikit-learn | 1.4.1 |
 | gensim | 4.3.2 |
 | seaborn | 0.13.2 |
 | cudatoolkit | 11.2.2 |
 | cudnn | 8.1.0 |
 
 
 
 
     
