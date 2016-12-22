import numpy as np
import pandas as pd
import sklearn.preprocessing as skl_pre
from sklearn.base import BaseEstimator, TransformerMixin

class preprocessFeatures(TransformerMixin, BaseEstimator):
	"""

	"""

	def fit(self, X, y):
		return self

	def transform(self, X):

		#Select relevant features
		X = X['']

		# Dropping the unnecessary features
		X_v1 = X.drop(['Name', 'Ticket', 'Cabin'], axis=1)

		# Converting Pclass to a string so it will become one-hot encoded
		X_v1['Pclass'] = X_v1['Pclass'].astype(str)

		# I need to make dummy variables
		X_v2 = pd.get_dummies(X_v1)

		# Imputing the ages with the mean
		imputer = skl_pre.Imputer(verbose=1)

		X_v3 = pd.DataFrame(imputer.fit_transform(X_v2), columns=X_v2.columns)

		return X_v3
