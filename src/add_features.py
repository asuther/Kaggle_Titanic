import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class addFeatures(TransformerMixin, BaseEstimator):
	"""

	"""
	def __init__(self):
		pass

	def fit(self, X, y):
		return self

	def transform(self, X):
		
		X['FamilySize'] = X['SibSp'] + X['Parch'] + 1

		return X
