    """"
        Objectif :
            Clean the given CSV dataset to insert it into PostgresQL TABLE:
    """


# Clean the given CSV dataset  to insert it into a PostrgresSQL table:
# Instructions :
# 1 : implementation the function df_nan_filter it takes a panda dataframe as input and applies
# - Remove the rows if size if NAN.
# - Set languages as "EN" if NAN.
# - Set Price as 0.0 if NAN.
# - set average use Rating as the Median of the column if NAN.
# - Set user Rating count as 1 if NAN.

import pandas as pd


def df_nan_filter(df):
    
    """
    Apply filters on NAN VAUES
    args : 
        df : Pandas DataFrame
    Returns: 
        Filtered dataframe.
    Raises:
        This function shouldnt rainses any exception.
        
    """
    print(df["Size"].isnull().count())
    df['Size'].dropna()
    print("After drop : "+ df['Size'].isnull().count())
    
    df['Languages'].fillna('EN', inplace = True)
    # Calcule the Average:
    #Average = df['Rating'].median()
    df["Rating"].fillna(df.mean())
    df["User Rating Count"].fillna(1)
    
    
    
# Create a function change_date_format that will change the date format from dd/mm/yyyy to yyyy-mm-dd
def change_date_format(date: str):
    date = pd.to_datetime(date.dt.strftime("%Y-%m-%d"))

# Create a function to clean the value of each row:

def  string_filter(s: str):
    """
    Apply filters in orders to clean the string
    Args : s: String
    Returns : Filtered String.
    Raise :
     This function shouldnt raise any Exception
    """
    # Filter : \\t, \\n, \\U1a1b2c3d4, \\u1a2b, \\x1a
    # turn \ ' into '
    # replace remaining \\ with \
    # Turn multiple spaces into one space
    import re
    
    s = re.sub(r'''\\+(t|n|U[a-z0-9]{8}|u[a-z0-9]{4}|x[a-z0-9]{2}|[\.]{2}''', ' ', s)
    s = s.replace('\\\'','\'').replace('\\\\','\\')
    s = re.sub(r' +',' ',s)
    return (s)     
                                       