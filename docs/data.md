The __data__ module contains all methods which loads and pre-processes all forms of biometric data from their original format into a form which can be used by the machine learning algorithms.

The forms of data which are currently being handled are:

- Public datasets: such as the DEAP dataset and the DREAMER dataset
- Experimental data collected from OpenBCI headsets by the project team

## Dataloaders
These functions load data from their raw files and converts them to a shared format (a multi-dimensional NumPy array) for easy manipulation. There are separate dataloader classes for each type of data. Each dataloader class has the following functions:

- test
- test
- test

More detailed documentation is provided below.

::: emotion-classification.src.data.load_public_datasets
    handler: python
    rendering:
      show_root_heading: false
      show_source: false

::: emotion-classification.src.data.load_experimental_data
    handler: python
    rendering:
      show_root_heading: false
      show_source: false

## Data Preprocessing

::: emotion-classification.src.data.preprocessing
    handler: python
    rendering:
      show_root_heading: false
      show_source: false




