import os

import numpy as np
import pandas as pd

package_directory = os.path.dirname(os.path.abspath(__file__))

def load_training_data(data_path = 'raw/train.csv'):
	"""

	Returns X and y for the Titanic training dataset

	"""
	#Load the raw data
	data_train = pd.read_csv(package_directory + '/../data/%s' % data_path)

	#Index the dataset according to the PassengerId
	data_train_indexed = data_train.set_index('PassengerId')
	
	#Create the design matrix and target vector
	X = data_train_indexed.drop(['Survived'], axis=1)
	y = data_train_indexed['Survived']

	return X, y

	