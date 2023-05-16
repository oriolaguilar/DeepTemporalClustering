"""
Implementation of the Deep Temporal Clustering model
Dataset loading functions

@author Florent Forest (FlorentF9)
"""

import numpy as np
from tslearn.datasets import UCR_UEA_datasets
from tslearn.preprocessing import TimeSeriesScalerMeanVariance
from sklearn.preprocessing import LabelEncoder

ucr = UCR_UEA_datasets()
# UCR/UEA univariate and multivariate datasets.
all_ucr_datasets = ucr.list_datasets()


def load_ucr(dataset='CBF'):
    X_train, y_train, X_test, y_test = ucr.load_dataset(dataset)
    X = np.concatenate((X_train, X_test))
    y = np.concatenate((y_train, y_test))
    if dataset == 'HandMovementDirection':  # this one has special labels
        y = [yy[0] for yy in y]
    y = LabelEncoder().fit_transform(y)  # sometimes labels are strings or start from 1
    assert(y.min() == 0)  # assert labels are integers and start from 0
    # preprocess data (standardization)
    X_scaled = TimeSeriesScalerMeanVariance().fit_transform(X)
    return X_scaled, None#y


def load_data_USA():
  print("---------------- USA -------------------")
  original_shape = (764, 18, 10)
  print(original_shape)
  loaded_arr = np.loadtxt("/content/sample_data/data_usa.txt")
  loaded_arr = loaded_arr.reshape(
    loaded_arr.shape[0], loaded_arr.shape[1] // original_shape[2], original_shape[2])
  
  X_scaled = TimeSeriesScalerMeanVariance().fit_transform(loaded_arr)
  return X_scaled, None

def load_data_CHINA():
  print("---------------- CHINA -------------------")
  original_shape = (479, 100, 8)
  print(original_shape)
  loaded_arr = np.loadtxt("/content/sample_data/data_china.txt")
  loaded_arr = loaded_arr.reshape(
    loaded_arr.shape[0], loaded_arr.shape[1] // original_shape[2], original_shape[2])
  
  X_scaled = TimeSeriesScalerMeanVariance().fit_transform(loaded_arr)
  return X_scaled, None

def load_data(dataset_name):
    if dataset_name == "USA":
        return load_data_USA()
    if dataset_name == "CHINA":
        return load_data_CHINA()
    if dataset_name in all_ucr_datasets:
        return load_ucr(dataset_name)
    else:
        print('Dataset {} not available! Available datasets are UCR/UEA univariate and multivariate datasets.'.format(dataset_name))
        exit(0)
