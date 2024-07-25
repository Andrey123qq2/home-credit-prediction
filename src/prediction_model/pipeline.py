from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

from prediction_model.config import config
import prediction_model.processing.preprocessors as pp
# from config import config
# import processing.preprocessors as pp
from  category_encoders import CatBoostEncoder

# loan_pipe=Pipeline(
#     [
#         ('Numerical Imputer', pp.NumericalImputer(variables=config.NUMERICAL_FEATURES)),
#         ('Categorical Imputer', pp.CategoricalImputer(variables=config.CATEGORICAL_FEATURES)),
#         ('Temporal Features', pp.TemporalVariableEstimator(variables=config.TEMPORAL_FEATURES, 
#         reference_variable=config.TEMPORAL_ADDITION)),
#         ('Categorical Encoder', pp.CategoricalEncoder(variables=config.FEATURES_TO_ENCODE)),
#         ('Log Transform', pp.LogTransformation(variables=config.LOG_FEATURES)),
#         ('Drop Features', pp.DropFeatures(variables_to_drop=config.DROP_FEATURES)),
#         ('Scaler Transform', MinMaxScaler()),
#         ('Linear Model', LogisticRegression(random_state=1))
#       ]
# )

#   num_pipeline = make_pipeline(
#       InfImputer(),
#       NanConstImputer(),
#       Log1pTransformer(),
# #         PowerTransformer(copy=False),
#   )
#   low_card_pipeline = make_pipeline(
#       OneHotEncoder(
#           dtype=np.int8, drop='if_binary', sparse_output=False,
#           min_frequency=0.02, handle_unknown='infrequent_if_exist'
#       ),
#   )
#   high_card_pipeline = make_pipeline(
#       CatBoostEncoder(),
# #         PowerTransformer(copy=False),
#   )

loan_pipe=Pipeline(
    [
        ('TableDtypes Transformer', pp.TableDtypesTransformer()),
        ('Downcast Transformer', pp.DowncastTransformer()),
        ('Numerical Imputer', pp.NumericalImputer(variables=config.NUMERICAL_FEATURES)),
        ('Categorical Encoder', CatBoostEncoder(cols=config.CATEGORICAL_FEATURES)),
        ('Categorical Imputer', pp.CategoricalImputer(variables=config.CATEGORICAL_FEATURES)),
        ('Dates Imputer', pp.DatesImputer(variables=config.DATE_FEATURES)),
        ('Dates Transformer', pp.DateColsTransformer(date_cols=config.DATE_FEATURES)),
        ('Log Transform', pp.Log1pTransformer(num_cols=config.NUMERICAL_FEATURES)),
        # ('PearsonCorrDrop Transformer', pp.PearsonCorrDropTransformer(variables=config.NUMERICAL_FEATURES + config.DATE_FEATURES)),
        # ('HighCorrDrop Transformer', pp.HighCorrDropTransformer(variables=config.NUMERICAL_FEATURES + config.DATE_FEATURES, mode='unique')),
        ('Scaler Transform', MinMaxScaler(copy=False)),
        ('Linear Model', LogisticRegression(random_state=1, verbose=1, solver='liblinear'))
        # ('Linear Model', LinearRegression(positive=True))
    ], verbose=True
)
LogisticRegression()


# (penalty: Literal['l1', 'l2', 'elasticnet'] | None = "l2", *, dual: bool = False, tol: Float = 0.0001, C: Float = 1, fit_intercept: bool = True, 
#  intercept_scaling: Float = 1, class_weight: Mapping | str | None = None, random_state: Int | RandomState | None = None, 
# solver: Literal['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'] = "lbfgs", max_iter: Int = 100, 
# multi_class: Literal['auto', 'ovr', 'multinomial'] = "auto", verbose: Int = 0, warm_start: bool = False, 
# n_jobs: Int | None = None, l1_ratio: Float | None = None) -> None