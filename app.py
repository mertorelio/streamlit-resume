from pathlib import Path
from streamlit_option_menu import option_menu
import streamlit as st
from PIL import Image
from about import about_main
from edu import edu_main
from projects import projects_main

st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 2rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Mert-Bozkurt-Resume.pdf"
profile_pic = current_dir / "assets" / "pp1.png"


# --- GENERAL SETTINGS ---
NAME = "Mert Bozkurt"
DESCRIPTION = """ Junior Machine Learning Engineer
"""
EMAIL = "bozkurtmert374@gmail.com"


    
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

def main():
    # --- HERO SECTION ---
    col11, col12  = st.columns(2, gap="small")
    with col11:
        st.image(profile_pic, width=230)

    with col12:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        col1,col2,col3,col4 = st.columns(4,gap="small")
        with col1 :
            st.markdown('<a href="https://www.linkedin.com/in/mert-bozkurt-b07096181/"><img src="https://www.iconpacks.net/icons/2/free-linkedin-logo-icon-2430-thumb.png" width=35 height=35></a>', unsafe_allow_html=True)
    
        with col2 :
            st.markdown('<a href="https://github.com/mertorelio"><img src="https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/github-512.png" width=35 height=35></a>', unsafe_allow_html=True)
        with col3 :
            st.markdown('<a href="https://medium.com/@mertbozkurt0"><img src="https://cdn-icons-png.flaticon.com/512/5968/5968906.png" width=35 height=35></a>', unsafe_allow_html=True)
        
        with col4 :
            st.markdown('<a href="mailto:bozkurtmert374@gmail.com"><img src="https://cdn-icons-png.flaticon.com/512/281/281769.png" width=35 height=35></a>', unsafe_allow_html=True)
        
       
    
 
    selected = option_menu(
            menu_title=None,  # required
            options=["About", "Education & Skills", "Projects"],  # required
            #icons=["house", "book", "envelope","envelope"], 
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#00bbf9"},
                "icon": {"color": "orange", "font-size": "0px"},
                "nav-link": {
                    "font-size": "13px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#00f5d4"},
            },
        )
    if selected == "About":
        about_main()
    if selected == "Education & Skills":
        edu_main()
    if selected == "Projects":
        projects_main()
    


if __name__ == "__main__":
    main()
