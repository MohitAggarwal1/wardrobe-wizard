import pandas as pd
import pickle

# Load your Excel file
excel_file_path = 'fashion_data.xlsx'  # replace with your Excel file path
df = pd.read_excel(excel_file_path)

# Create the nested dictionary structure for the recommendations
fashion_recommendations = {}
for _, row in df.iterrows():
    key = (row['Gender'], row['Body Type'], row['Skin Tone'], row['Occasion'])
    item = {
        'name': row['Outfit Name'],
        'image': row['Image URL'],
        'link': row['Link']
    }
    if key not in fashion_recommendations:
        fashion_recommendations[key] = []
    fashion_recommendations[key].append(item)

# Save to .pkl file
pkl_file_path = 'fashion_model.pkl'
with open(pkl_file_path, 'wb') as file:
    pickle.dump(fashion_recommendations, file)

print(f"Data has been successfully converted and saved to {pkl_file_path}.")
