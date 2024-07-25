import os
import pandas as pd
import joblib
from glob import glob

from prediction_model.config import config
# import config

# def set_table_dtypes(df):
#     for col in df.columns:
#         if col in ["case_id", "WEEK_NUM", "num_group1", "num_group2"]:
#             df[col] = df[col].astype('int64')
#         elif col in ["date_decision"]:
#             df[col] = pd.to_datetime(df[col])
#         elif col[-1] in ("P", "A"):
#             df[col] = df[col].astype('float64')
#         elif col[-1] in ("M",) or 'person' in col:
#             df[col] = df[col].astype('category')
#         elif col[-1] in ("D",):
#             df[col] = pd.to_datetime(df[col])
#     return df

# def downcast(df):
#     """
#     Reduce memory usage of a Pandas DataFrame by converting 
#     object types to categories and downcasting numeric columns
#     """
#     start_mem = df.memory_usage().sum() / 1024**2
#     print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))
#     object_cols, int_cols, float_cols = [], [], []
#     for col, dtype in df.dtypes.items():
#         if pd.api.types.is_object_dtype(dtype):
#             object_cols.append(col)
#         elif pd.api.types.is_integer_dtype(dtype):
#             int_cols.append(col)
#         elif pd.api.types.is_float_dtype(dtype):
#             float_cols.append(col)
#     df[object_cols] = df[object_cols].astype('category')
#     df[int_cols] = df[int_cols].apply(pd.to_numeric, downcast='integer')
#     df[float_cols] = df[float_cols].apply(pd.to_numeric, downcast='float')
    
#     end_mem = df.memory_usage().sum() / 1024**2
#     print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
#     print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
#     return df

def load_dataset(base_file, file_names, mode='train'):
    """Read Data"""
    base_file_path = os.path.join(config.DATAPATH, f"{mode}{base_file}")
    all_data_df = pd.read_parquet(base_file_path)
    for file in file_names:
        file_pattern = os.path.join(config.DATAPATH,  f"{mode}{file}")
        chunks = []
        for i, file in enumerate(glob(str(file_pattern))):
            file_path = os.path.join(config.DATAPATH, file)
            chunk_df = pd.read_parquet(file_path)
            chunks.append(chunk_df) 
        file_df = pd.concat(chunks)
        all_data_df = all_data_df.merge(file_df, how="left", on="case_id")

    # all_data_df = set_table_dtypes(all_data_df)
    # all_data_df = downcast(all_data_df)
    print("df shape:", all_data_df.shape)
    return all_data_df

def save_pipeline(pipeline_to_save):
    """Store Output Of Pipeline
    Exporting pickle file of trained Model """
    save_file_name = config.PIPELINE_FILE_NAME
    save_path = os.path.join(config.SAVED_MODEL_PATH, save_file_name)
    joblib.dump(pipeline_to_save, save_path)
    print("Saved Pipeline : ",save_file_name)

def load_pipeline(pipeline_to_load):
    """Importing pickle file of trained Model"""
    save_path = os.path.join(config.SAVED_MODEL_PATH, pipeline_to_load)
    trained_model = joblib.load(save_path)
    return trained_model
