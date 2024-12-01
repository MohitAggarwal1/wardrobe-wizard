# Importing Modules
import streamlit as st
import pickle
import os

# Function to load the model safely
def load_fashion_model():
    model_path = 'fashion_model.pkl'
    if os.path.exists(model_path):
        with open(model_path, 'rb') as file:
            return pickle.load(file)
    else:
        st.error("Fashion model file not found.")
        return None

# Load the fashion recommender model
fashion_model = load_fashion_model()

# Function to recommend outfits
def recommend_outfit(gender, body_type, skin_tone, occasion):
    if not fashion_model:
        return []
    
    # Retrieve recommendations from the model
    recommendations = fashion_model.get((gender, body_type, skin_tone, occasion), [])
    
    if not recommendations:
        return [{"name": "No recommendations available for this combination.", "image": None, "link": None}]
    
    return recommendations

# Streamlit app layout
st.title('🧙‍♂️ Wardrobe Wizard 👗')
st.subheader('Magic for Every Occasion, See Yourself in Style!')

# Create two columns for a 2x2 layout
col1, col2 = st.columns(2)

# Place select boxes in each column
with col1:
    gender = st.selectbox('Select your gender:', ['Male', 'Female'])
    body_type = st.selectbox('Select your body type:', ['Slim', 'Curvy', 'Athletic'])

with col2:
    skin_tone = st.selectbox('Select your skin tone:', ['Fair', 'Brown', 'Dark'])
    occasion = st.selectbox('Select the occasion:', ['Casual', 'Formal', 'Party', 'Wedding'])

if st.button('Get Recommendations'):
    with st.spinner("Loading recommendations..."):
        recommendations = recommend_outfit(gender, body_type, skin_tone, occasion)
    
    st.subheader('Recommended Outfits:')
    
    if recommendations and recommendations[0]['name'] == "No recommendations available for this combination.":
        st.warning("No recommendations available for this combination.")
    
    # Set up columns for each recommendation
    cols = st.columns(len(recommendations))
    
    # CSS styling for white link text without underline and uniform image size
    st.markdown("""
        <style>
        .custom-link {
            color: white;
            text-decoration: none;
        }
        .recommendation-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 10px;
        }
        .recommendation-image {
            width: 130px;
            height: 180px;
            object-fit: fill;
            border-radius: 10px; /* Optional: Add rounded corners */
        }
        </style>
        """, unsafe_allow_html=True)

    # Loop through each recommendation and assign it to a column
    for i, rec in enumerate(recommendations):
        with cols[i]:
            if rec['image']:
                # Make the image clickable by wrapping it in an HTML <a> tag
                st.markdown(
                    f'<a href="{rec["link"]}" target="_blank">'
                    f'<img src="{rec["image"]}" class="recommendation-image"></a>',
                    unsafe_allow_html=True
                )
            else:
                st.image("https://via.placeholder.com/130x180?text=No+Image", width=130)  # Default placeholder image

            # Display product name as plain text (unclickable)
            st.markdown(f'**{rec["name"]}**')

# Footer Section
st.markdown("""
    <style>
        .footer {
            margin-top: 30px;
            text-align: center;
            color: gray;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        © 2024 Wardrobe Wizard | Developed by Mohit Aggarwal
    </div>
    """, unsafe_allow_html=True)
