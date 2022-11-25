import streamlit as st
from PIL import Image
import style

st.title('ArtMaster')

img = st.sidebar.selectbox(
    'Select the image you want to transform.',
    ('amber.jpg', 'cat.png')
)

style_name = st.sidebar.selectbox(
    'Select the style you want to be applied.',
    ('candy', 'mosaic', 'rain_princess', 'udnie')
)

model = "saved_models/" + style_name + ".pth"
input_image = "/Users/bilbaothanos14/Documents/GitHub/ArtMaster/neural_style/images/content-images/" + img
output_image = "/Users/bilbaothanos14/Documents/GitHub/ArtMaster/neural_style/images/output-images/" + style_name + "-" + img

st.write("### Source Image:")
image = Image.open(input_image)
st.image(image, width = 400)
clicked = st.button('Stylize')

if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)
    st.write("### Output Image:")
    image = Image.open(output_image)
    st.image(image, width=400)