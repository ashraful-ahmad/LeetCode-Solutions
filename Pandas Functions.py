import pandas as pd 

'Creating a DataFrame'

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     "Age": [24, 27, 22, 32],
#     "City": ['New York', 'Los Angeles', 'Chicago', 'Houston']}

# data = pd.read_csv("C:/Users/White/Downloads/weekday.csv")

# data = pd.read_excel("C:/Users/White/Downloads/file_example_XLS_10")

# df = pd.DataFrame(data)
# print(df)

'Exploring Data in pandas'

# data = pd.read_excel("C:/Users/White/Downloads/file_example_XLS_100.xls")

# print(data) # Display the entire DataFrame with first 5 and last 5 rows
# print(data.head(10))  # Display the first 10 rows
# print(data.tail(10))  # Display the last 10 rows
# print(data.columns)  # List of column names
# print(data.info())  # Summary of the DataFrame
# print(data.describe())  # Statistical summary of numerical columns
# prrint(data.shape)  # Number of rows and columns
# print(data.dtypes)  # Data types of each column
# print(data['Price'])  # Access a specific column
# print(data[['Price', 'Quantity']])  # Access multiple columns
# print(data.isnull().sum())  # Check for missing values in each column

'handling duplicates from data'

# data = pd.read_csv("C:/Users/White/Downloads/weekday.csv")

# # print(data)
# # print(data.duplicated("Day_Id").sum()) #Returns boolean series denoting duplicate rows
# print(data.drop_duplicates("Name")) #Returns DataFrame with duplicate rows removed

'Handling Missing values  or Null Values'

# data = pd.read_csv("C:/Users/white/Downloads/Excel Sheets/weekday.csv")

# print(data)

# print(data.isnull().sum()) #Check for missing values in each column
# print(data.fillna(0)) #Fill missing values with a specified value
# print(data.dropna()) #Remove rows with missing values
# print(data['Name'].fillna("Unknown")) #Fill missing values in a specific column
# print(data['Name'].dropna()) #Remove missing values in a specific column
# print(data['Name'].replace("Alice", "Alicia")) #Replace specific values in a column
# print(data.replace(np.nan,"hello ")) #Replace all NaN values with Hello
# print(data.fillna(method = "bfill")) #Replace all Nan/ null values with backward values
# print(data.fillna(method = "ffill")) #Replace all Nan value with forward value

'Column Transformation'

# data = pd.read_csv("C:/Users/white/Downloads/Excel Sheets/weekday.csv")

# print(data['Name'].str.upper()) #Convert text in a column to uppercase
# print(data['Name'].str.lower()) #Convert text in a column to lowercase
# data.loc[data['Day_Id'] % 2 == 0, 'EVE OR ODD'] = 'Even Day' #Conditional update of values in a column
# data.loc[data['Day_Id'] % 2 != 0, 'EVE OR ODD'] = 'Odd Day' #Conditional update of values in a column
# dat = data.rename(columns={"Name": "Full Name"}) #Renaming columns
# data["Name + ID"] = data["Name"] + " " + data["Day_Id"].astype(str) #Creating a new column by combining existing columns

# print(data)

'use of methods and Function for column Transformation'

# data = pd.read_csv("C:/Users/white/Downloads/Excel Sheets/samples_10.csv")

# data['Bonus'] = (data['Salary']/100) * 20 #Creating a new column based on a calculation from an existing column
# print(data)

# data = {'Months': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']}
# df = pd.DataFrame(data)

# def Short_Months(month):
#     return month[:3]

# df['Short_Months'] = df['Months'].map(Short_Months) #Applying a custom function to a column
# print(df)


'GroupBy and Aggregation'


# data = pd.read_csv("C:/Users/white/Downloads/Excel Sheets/samples_10.csv")
# print(data)

    #'Grouping the data by a specific column and calculating the mean'
# grouped_data = data.groupby(['Country','Gender']).agg({'User_id':'count'})
# print(grouped_data)

    #Aggregating multiple statistics
# agg_data = data.groupby(['Country','Gender']).agg({'Salary': ['mean', 'max', 'min'], 'Age': 'mean'})
# print(agg_data)

'Merge , Join and Concatenate'

# data1 = pd.DataFrame({
#     'ID': [1, 2, 3, 4],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David']
# })

# data2 = pd.DataFrame({
#     'ID': [1, 2, 5, 6],
#     'Salary': [70000, 80000, 90000, 100000]
# })

# Merging dataframes
# merged_data = pd.merge(data1, data2, on='ID', how='outer')
# merged_data = pd.merge(data1, data2, on='ID', how='inner')
# merged_data1 = pd.merge(data1, data2, on='ID', how='left')
# merged_data2 = pd.merge(data1, data2, on='ID', how='right')
# print(merged_data1)


# Concatenating dataframes
# concatenated_data = pd.concat([data1, data2], ignore_index=True)
# print(concatenated_data)

# Joining dataframes
# data1.set_index('ID', inplace=True)
# data2.set_index('ID', inplace=True)
# joined_data = data1.join(data2, how='outer')
# print(joined_data)

'Compare two DataFrames'

# data1 = pd.DataFrame({
#     'ID': [1, 2, 3, 4],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David']
# })

# data2 = pd.DataFrame({
#     'ID': [1, 2, 5, 6],
#     'Name': ['Alice', 'Bob', 'Eve', 'Frank']
# })
# comparison = data1.compare(data2, align_axis=0) #Compare two DataFrames and show differences
# print(comparison)
# print(data1.equals(data2)) #Check if two DataFrames are equal
