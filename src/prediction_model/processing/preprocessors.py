import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import warnings

class PearsonCorrDropTransformer(BaseEstimator, TransformerMixin):
    """
    Transformer to drop highly correlated columns
    """
    def __init__(self, variables=None, corr_threshold=0.0025):
        self.variables = variables
        self.corr_threshold = corr_threshold
        self.cols_to_drop = set()

    def pearson_corr(self, x1, x2):
        mean_x1 = np.mean(x1)
        mean_x2 = np.mean(x2)
        std_x1 = np.std(x1)
        std_x2 = np.std(x2)
        pearson = np.mean((x1 - mean_x1) * (x2 - mean_x2))/(std_x1 * std_x2)
        return pearson
        
    def fit(self, X, y=None):
        self.variables = list(set(X.columns).intersection(self.variables))
        X = X.copy()
        X = X[self.variables]
        for col in self.variables:
            if col != 'target':
                pearson = self.pearson_corr(X[col].values, y.values)
                if abs(pearson) <= self.corr_threshold:
                    self.cols_to_drop.add(col)
        return self
    
    def transform(self, X):
        if len(list(self.cols_to_drop)) == 0:
            return X
        else:
            return X.drop(list(self.cols_to_drop), axis=1)
    
    def get_feature_names_out(self, input_features=None):
        return [col for col in input_features if col not in self.cols_to_drop]

class HighCorrDropTransformer(BaseEstimator, TransformerMixin):
    """
    Transformer to drop highly correlated columns
    """
    def __init__(self, variables=None, corr_threshold=0.95, mode='missing'):
        self.variables = variables
        self.corr_threshold = corr_threshold
        self.mode = mode
        
    def fit(self, X, y=None):
        self.variables = list(set(X.columns).intersection(self.variables))
        X = X.copy()
        X = X[self.variables]
        self.cols_to_drop = set()
        # do not check corr for -1 value
        if self.corr_threshold != -1:
            self.corr_matrix = X.corr()
            for col1 in self.corr_matrix.columns:
                for col2 in self.corr_matrix.columns:
                    if col1 != col2:
                        # Check for high correlation
                        if abs(self.corr_matrix.loc[col1, col2]) >= self.corr_threshold:
                            # Check which column has more missing values
                            if self.mode == "missing":
                                col1_crit = X[col1].isna().sum()
                                col2_crit = X[col2].isna().sum()
                            if self.mode == "unique":
                                col1_crit = 1 / X[col1].nunique()
                                col2_crit = 1 / X[col2].nunique()
                            if col1_crit > col2_crit:
                                self.cols_to_drop.add(col1)
                            else:
                                self.cols_to_drop.add(col2)
        return self
    
    def transform(self, X):
        if len(list(self.cols_to_drop)) == 0:
            return X
        else:
            return X.drop(list(self.cols_to_drop), axis=1)
    
    def get_feature_names_out(self, input_features=None):
        return [col for col in input_features if col not in self.cols_to_drop]
    

class BadColsDropTransformer(BaseEstimator, TransformerMixin): 
    """
    Transformer to drop unuseful columns
    """
    def __init__(self, isnull_threshold=0.95, over_cat_threshold=0.999):
        self.isnull_threshold = isnull_threshold
        self.over_cat_threshold = over_cat_threshold
        
    def fit(self, X, y=None):
        # Columns with many missing values 
        self.missing_values = X.isna().mean().sort_values(ascending=False)
        self.cols_to_drop = set(
            self.missing_values[self.missing_values.gt(self.isnull_threshold)].index
        )
        # Columns with one higly dominant value
        for col in X.columns:
            if (X[col].value_counts(normalize=True) > self.over_cat_threshold).any():
                self.cols_to_drop.add(col)
                
        # Columns with identical values  
        for col1 in X.columns[:-1]:
            if col1 not in self.cols_to_drop:
                for col2 in X.columns[X.columns.get_loc(col1) + 1:]:
                    if X[col1].equals(X[col2]):
                        self.cols_to_drop.add(col2)
        # Columns with one value
        for col in X.columns:
            if X[col].max() == X[col].min():
                self.cols_to_drop.add(col)
                
        return self
        
    def transform(self, X):
        return X.drop(list(self.cols_to_drop), axis=1)
    
    def get_feature_names_out(self, input_features=None):
        return [col for col in input_features 
                if col not in self.cols_to_drop]

#Numerical Imputer
class NumericalImputer(BaseEstimator, TransformerMixin):
    """Numerical Data Missing Value Imputer"""
    def __init__(self, variables=None):
            self.variables = variables
    
    def fit(self, X, y=None):
        self.imputer_dict_={}
        for feature in self.variables:
            self.imputer_dict_[feature] = X[feature].mean()
        return self

    def transform(self,X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna(self.imputer_dict_[feature])
        return X
    
class DatesImputer(BaseEstimator, TransformerMixin):
    """Numerical Data Missing Value Imputer"""
    def __init__(self, variables=None):
            self.variables = variables
    
    def fit(self, X,y=None):
        self.imputer_dict_={}
        for feature in self.variables:
            self.imputer_dict_[feature] = X[feature].mean()
        return self

    def transform(self,X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna(self.imputer_dict_[feature])
        return X

#Categorical Imputer
class CategoricalImputer(BaseEstimator, TransformerMixin):
    """Categorical Data Missing Value Imputer"""
    def __init__(self, variables=None):
        self.variables = variables
    
    def fit(self, X,y=None):
        self.imputer_dict_={}
        for feature in self.variables:
            self.imputer_dict_[feature] = X[feature].mode()[0]
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna(self.imputer_dict_[feature])
        return X

class Log1pTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, num_cols=[], threshold=100):
        super().__init__()
        self.num_cols = num_cols
        self.threshold = threshold
        self.outliers_cols=[]
        
    def fit(self, X, y=None):
        X = X.copy()
        X = X[self.num_cols]
        with warnings.catch_warnings():
            warnings.simplefilter(action='ignore', category=RuntimeWarning)
            X_desc = X.describe()
        max_to_mean = (
            np.abs(X_desc.loc['max'] / X_desc.loc['mean'])
        )
        min_to_mean = (
            np.abs(X_desc.loc['min'] / X_desc.loc['mean'])
        )
        max_to_mean_finite = max_to_mean[np.isfinite(max_to_mean)]
        min_to_mean_finite = min_to_mean[np.isfinite(min_to_mean)]
        outliers_cols_max = list(max_to_mean_finite[max_to_mean_finite > self.threshold].index)
        outliers_cols_min = list(min_to_mean_finite[min_to_mean_finite > self.threshold].index)
        self.outliers_cols = outliers_cols_max + outliers_cols_min
        return self
    
    def transform(self, X):
        for col in self.outliers_cols:
            X[col] = np.log1p(np.abs(X[col])) * np.sign(X[col])
        return X
    
    def get_feature_names_out(self, input_features=None):
        return input_features
    
class DateColsTransformer(BaseEstimator, TransformerMixin):
    """Feature Engineering"""
    def __init__(self, reference_date_col='date_decision', date_cols=[]):
        self.date_cols = date_cols
        self.ref_col = reference_date_col
    
    def fit(self, X,y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X['month_decision'] = X["date_decision"].dt.month.astype('int16')
        X['weekday_decision'] = X["date_decision"].dt.month.astype('int16')
        X['day_decision'] = X["date_decision"].dt.month.astype('int16')
        
        for col_name in self.date_cols:
            if col_name == 'date_decision':
                continue
            X[col_name] = X[col_name] - X[self.ref_col]
            X[col_name] = X[col_name].dt.days.astype('int32')
        X = X.drop("date_decision", axis=1)
        return X
    
class TableDtypesTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for col in X.columns:
            if col in ["case_id", "WEEK_NUM", "num_group1", "num_group2"]:
                X[col] = X[col].astype('int64')
            elif col in ["date_decision"]:
                X[col] = pd.to_datetime(X[col])
            elif col[-1] in ("P", "A"):
                X[col] = X[col].astype('float64')
            elif col[-1] in ("M",) or 'person' in col:
                X[col] = X[col].astype('category')
            elif col[-1] in ("D",):
                X[col] = pd.to_datetime(X[col])
        return X
    
    def get_feature_names_out(self, input_features=None):
        return input_features

class DowncastTransformer(BaseEstimator, TransformerMixin):
    """
    Reduce memory usage of a Pandas DataFrame by converting 
    object types to categories and downcasting numeric columns
    """
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        start_mem = X.memory_usage().sum() / 1024**2
        print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))
        object_cols, int_cols, float_cols = [], [], []
        for col, dtype in X.dtypes.items():
            if pd.api.types.is_object_dtype(dtype):
                object_cols.append(col)
            elif pd.api.types.is_integer_dtype(dtype):
                int_cols.append(col)
            elif pd.api.types.is_float_dtype(dtype):
                float_cols.append(col)
        X[object_cols] = X[object_cols].astype('category')
        X[int_cols] = X[int_cols].apply(pd.to_numeric, downcast='integer')
        X[float_cols] = X[float_cols].apply(pd.to_numeric, downcast='float')
        
        end_mem = X.memory_usage().sum() / 1024**2
        print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
        print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
        return X
    
    def get_feature_names_out(self, input_features=None):
        return input_features