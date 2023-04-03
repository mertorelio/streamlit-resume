import streamlit as st 



def projects_main():
    st.subheader("Text Generation")
    
    col1, = st.columns([1])
    
    with col1:
        st.write("[Github Link](https://github.com/mertorelio/text_generator)")
    
    
    st.write("""
            :heavy_check_mark: Datasets: Philosophers Quotes from azquotes.com, using Web Scraping with Selenium
            <br> 
             :heavy_check_mark: Using Tensorflow/Keras i made a simple text generation with an RNN. If you give the model a
sentence, it will complete it and produce new sentences             
             """,unsafe_allow_html=True)
    
    st.subheader("Chatbot")
    col1,col2 = st.columns([1,1])
    
    with col1:
        st.write("[Github Link](https://github.com/mertorelio/chatbot-tf)")
    
    with col2:
        st.write("[Hugging Face Space Link](https://huggingface.co/spaces/mertbozkurt/basic-chatbot)")
       
    st.write("""
            :heavy_check_mark: I prepared a small dataset. I trained the model using the Tensorflow and nltk libraries.
            <br> 
             :heavy_check_mark: I made a simple interface with the Python tkinter library and created a small demo.
             <br> 
             :heavy_check_mark: Finally, I made it work on the web with streamlit and hugging-face.
             """,unsafe_allow_html=True)

    st.subheader("Fast Style Transfer")
    
    
    
    st.write("[Hugging Face Space Link](https://huggingface.co/spaces/mertbozkurt/style-transfer)")
    
    st.write("""
            :heavy_check_mark: I used Tensorflow Hub module for image stylization.
            <br> 
             :heavy_check_mark: I made a simple interface with streamlit and published on hugging-face.
             
             """,unsafe_allow_html=True)
    
    st.subheader("Deep Learning Models")
    col1,col2= st.columns([1,1])
    with col1:
        st.write("[Github Link](https://github.com/mertorelio/deeplearning_models)")
    
    with col2:
        st.write("[Hugging Face Space Link](https://huggingface.co/spaces/mertbozkurt/models)")
    
   
    
    st.write("""
            :heavy_check_mark: I trained models for binary classification, cat and dog pictures, face detection, disaster tweet
classification, movie recommendation system etc.
            <br> 
             :heavy_check_mark: I made it all models work on the web with streamlit.
             <br>
             :heavy_check_mark: Finally I created a docker image with dockerfile and deployed on hugging-face
             """,unsafe_allow_html=True)
    
    st.subheader("Image Colorization")
    col1,col2,= st.columns([1,1])
    with col1:
        st.write("[Kaggle Notebook Link](https://www.kaggle.com/code/mertbozkurt5/basic-image-colorization)")
    
    with col2:
        st.write("[Kaggle Dataset Link](https://www.kaggle.com/datasets/mertbozkurt5/image-colorization)")
    
   
    
    st.write("""
            :heavy_check_mark: Dataset that I have prepared using google_images_download module
            <br> 
             :heavy_check_mark: The model is basic CNN architecture.
             
             """,unsafe_allow_html=True)

