# Wardrobe Wizard 👗

Wardrobe Wizard is a personalized outfit recommendation app powered by a machine learning model, designed to offer fashion suggestions based on your preferences and characteristics. With options tailored to gender, body type, skin tone, and occasion, it helps you discover the perfect style for any event.

## Features
- **Personalized Recommendations**: Get outfit suggestions based on your input.
- **Interactive Interface**: Built with Streamlit for a smooth and user-friendly experience.
- **Clickable Images**: Each outfit recommendation includes an image and a direct link to view or purchase the item.

## Installation and Setup

### Prerequisites
- Python 3.7 or later
- Required Python packages:
  ```bash
  pip install streamlit pickle5
  ```

### Steps to Run the App
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/your-username/wardrobe-wizard.git
   cd wardrobe-wizard
   ```

2. Run the application using Streamlit:
   ```bash
   streamlit run app.py
   ```

3. Open the link provided by Streamlit (typically `http://localhost:8501`) in your web browser.

## Project Overview

### Core Components

#### Importing Necessary Modules
The app uses Streamlit for the frontend and `pickle` for loading the pre-trained model.
```python
import streamlit as st
import pickle
```

#### Loading the Fashion Model
The pre-trained fashion recommendation model is loaded as follows:
```python
fashion_model = pickle.load(open('fashion_model.pkl', 'rb'))
```

#### Outfit Recommendation Function
The `recommend_outfit` function generates outfit suggestions based on user input for gender, body type, skin tone, and occasion.
```python
def recommend_outfit(gender, body_type, skin_tone, occasion):
    recommendations = fashion_model.get((gender, body_type, skin_tone, occasion), [])
    
    if not recommendations:
        return [{"name": "No recommendations available for this combination.", "image": None, "link": None}]
    
    return recommendations
```

### Streamlit User Interface
- **Input Options**: Dropdowns and selectors to input preferences.
- **Output Display**: Grid layout showcasing outfit recommendations with images and clickable links.

#### Example Layout
```python
st.title('🤓 Wardrobe Wizard 👗')
st.subheader('Magic for Every Occasion, See Yourself in Style!')
```

## Custom Styling
Custom CSS enhances the visual presentation of recommendations:
- **Clickable Images**: Product images link directly to the item page.
- **Consistent Design**: Uniform styling for text and links.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your forked repository.
4. Open a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Let Wardrobe Wizard be your stylist! Discover outfits that match your unique style and make every occasion special.
