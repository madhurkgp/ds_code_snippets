# Function to convert date to pandas datetime datatype
def cnv_2_datetime(df,col_name='application_date'):
  df[col_name] = pd.to_datetime(df[col_name], format='%d-%m-%Y')
  return df


# Function to convert categorical columns as pandas category type
def cnv_2_category(df,col_names):
  for col in col_names:
    df[col] = df[col].astype('category')
  return df


# To drop columns
def drop_col(df,col_names):
  df.drop(col_names, axis=1,inplace=True)
  return df
