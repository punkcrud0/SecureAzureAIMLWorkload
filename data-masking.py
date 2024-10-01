import pandas as pd

# Load the dataset
df = pd.read_csv('sensitive-data.csv')

# Mask sensitive columns
# For example, masking Social Security Numbers (SSN)
if 'SSN' in df.columns:
    df['SSN'] = df['SSN'].apply(lambda x: '***-**-' + str(x)[-4:])

# Mask Email Addresses
if 'Email' in df.columns:
    df['Email'] = df['Email'].apply(lambda x: x[0] + '***@' + x.split('@')[1])

# Mask Phone Numbers
if 'Phone' in df.columns:
    df['Phone'] = df['Phone'].apply(lambda x: '(***) ***-' + str(x)[-4:])

# Save the masked dataset
df.to_csv('masked-data.csv', index=False)

print("Data masking completed. Masked data saved to 'masked-data.csv'.")
