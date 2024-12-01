# Wardrobe Wizard 👗

Wardrobe Wizard is a personalized outfit recommendation app powered by a machine learning model, designed to offer fashion suggestions based on your preferences and characteristics. With options tailored to gender, body type, skin tone, and occasion, it helps you discover the perfect style for any event.


## Features
- **Personalized Recommendations**: Get outfit suggestions based on your input.
- **Streamlit Interface**: An interactive and user-friendly interface to make your experience smooth and enjoyable.
- **Clickable Images**: Each outfit recommendation comes with an image and a link to view or purchase the item.


## Setup Instructions

### Prerequisites
1. Python 3.7+
2. Install the required packages:
```bash
pip install streamlit pickle5
```


### Running the App
1. Clone the repository and navigate to the app's directory.
2. Run the following command to start the app:
```bash
streamlit run app.py
```


3. Open the link provided by Streamlit (typically `http://localhost:8501`).

## Code Overview

### Importing Modules

```python
import streamlit as st
import pickle
```


### Loading the Model
```python
fashion_model = pickle.load(open('fashion_model.pkl', 'rb'))
```


### Outfit Recommendation Function
The `recommend_outfit` function uses the `fashion_model.pkl` data to generate outfit suggestions based on:
- **Gender**
- **Body Type**
- **Skin Tone**
- **Occasion**

```python
def recommend_outfit(gender, body_type, skin_tone, occasion):
    recommendations = fashion_model.get((gender, body_type, skin_tone, occasion), [])
    
    if not recommendations:
        return [{"name": "No recommendations available for this combination.", "image": None, "link": None}]
    
    return recommendations
```


### Streamlit Layout
The app interface includes:
- **Selectors** for gender, body type, skin tone, and occasion.
- **Recommendations**: A display of suggested outfits in a grid layout.


### Example App Layout
```python
st.title('🧙‍♂️ Wardrobe Wizard 👗')
st.subheader('Magic for Every Occasion, See Yourself in Style!')
```


## Custom Styling
CSS is used to enhance the display of recommendations:
- **Clickable Images**: Product images link directly to the item.
- **White Text Links**: Styling ensures a consistent look for links and image presentation.


