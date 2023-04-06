import streamlit as st 

def about_main():
      
    st.subheader("Profile Summary")
    st.markdown("""
             <pre>\tI'm 4th grade computer engineer student at Ondokuz Mayis University. 
             I am the organizer of GDG Samsun. 
             I was a core member and mentor in the Global AI Hub organization.
             I'm interested in AI.So I'm constantly trying to teach new things in this field.
             I've been using Python for 3 years,
            I'm also work with Tensorflow/Keras. I have some theoretical knowledge in the field
            of ML/DL. I am trying to improve myself by reading documents and reading
            different codes on kaggle. I'm still trying to improve myself in various subjects like data
            analysis, NLP, transformers, GANs. I don't have any professional experience in IT or AI but i
            think i'm good at learning new things. I'm still looking for a job or internship.
        
             """,unsafe_allow_html=True)
    st.subheader("Education")
    st.write("Bachelor - Computer Engineering")
    st.write("ONDOKUZ MAYIS UNIVERSITY / SAMSUN 2019 - 2023")
    st.subheader("Skills")
    st.markdown("""
                | Skill | :star::star::star::star::star: |
| --- | --- |
| Python| :star::star::star::star: |
| Tensorflow/Keras | :star::star::star:|
| OpenCV | :star::star::star: |
| Scikit-learn | :star: |
| Data Visualization | :star: |
                
                
                
                
                """, unsafe_allow_html=True)
    st.subheader("Courses & Certificates")
    st.write("""[Coursera - Tensorflow](https://www.coursera.org/account/accomplishments/certificate/WUM6LA22FPYD)
             <br>
             [Coursera - Tensorflow with CNN](https://www.coursera.org/account/accomplishments/certificate/TGEEGV798DU8)
             <br>
             [Coursera - Structuring Machine Learning Projects](https://www.coursera.org/account/accomplishments/verify/TMXMQRWC3KB7)
             <br>
             [Udemy - Deep Learning with Python](https://www.udemy.com/certificate/UC-4f0edf7e-aa8f-4b3d-a89e-71acbe5e99ec/)
             <br>
             [Udemy - Machine Learning with Python](https://www.udemy.com/certificate/UC-bbdc02ce-e188-4507-b88c-2171b8a2889a/)
             <br>
             [(Work in progress) Udemy - TensorFlow Developer Certificate in 2023: Zero to Mastery](https://www.udemy.com/course/tensorflow-developer-certificate-machine-learning-zero-to-mastery/)
             """,unsafe_allow_html=True)
