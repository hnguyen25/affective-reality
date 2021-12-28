"""
LOAD_PUBLIC_DATASETS
Huy Nguyen (2021)

Used to load cleaned EEG data from publicly available datasets, such as the DEAP and DREAMER datasets, into a common data format.
"""

class DreamerDataloader:
    """Used to load data obtained from the DREAMER public dataset.

    Example:

    Attributes:

    """

    def load_raw_data(self, filepath : str):
        """
        Args:
            filepath (str): path to DREAMER file (must be in .mat format)

        Returns:
            numpy.array: raw data file loaded into python
        """
        return None

    def get_dataset_info(self, filepath : str):
        """
        Args:
            filepath (str): path to DREAMER file (must be in .mat format)

        Returns:
            dict: dictionary with important info about dataset
        """
        return None

    def load_data(self, filepath : str, num_subjects=-1, num_trials=-1, choose_randomly=False):
        """
        Args:
            filepath (str): path to DREAMER file (must be in .mat format)
            num_subjects (int): if not -1, choose the number of participants from the dataset to pull data from; cannot exceed total number of participants as specified in get_dataset_info()
            num_trials (int): if not -1, choose the number of trials for each participant to pull data from; cannot exceed total number of trials done in experiments as specified in get_dataset_info()
            choose_randomly (bool): if num_subjects is not -1, then randomly choose subjects whose data will be loaded.
        Returns:
            numpy.array: loaded data in a shared data format
        """
        return None

class DEAPDataloader:
    """Used to load data obtained from the DEAP public dataset.

    Example:

    Attributes:

    """

    def load_raw_data(self, filepath : str):
        """
        Args:
            filepath (str): path to DREAMER file (must be in .mat format)

        Returns:
            numpy.array: raw data file loaded into python
        """
        return None

    def get_dataset_info(self, filepath : str):
        """
        Args:
            filepath (str): path to DREAMER file (must be in .mat format)

        Returns:
            dict: dictionary with important info about dataset
        """
        return None

    def load_data(self, filepath : str, num_subjects=-1, num_trials=-1, choose_randomly=False):
        """
        Args:
            filepath (str): path to DREAMER file (must be in .mat format)
            num_subjects (int): if not -1, choose the number of participants from the dataset to pull data from; cannot exceed total number of participants as specified in get_dataset_info()
            num_trials (int): if not -1, choose the number of trials for each participant to pull data from; cannot exceed total number of trials done in experiments as specified in get_dataset_info()
            choose_randomly (bool): if num_subjects is not -1, then randomly choose subjects whose data will be loaded.
        Returns:
            numpy.array: loaded data in a shared data format
        """
        return None