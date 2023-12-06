from PIL import Image
from pathlib import Path

import requests
import streamlit as st
from streamlit_lottie import st_lottie
## -- PATH --#
path = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = path / "styles/main.css"
resume_file = path / "assets/One_page_CV__March_2023_.pdf"
profile_pic = path / "assets/dario_vlt_night.jpg"
## -- LOAD ASSETS --#

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_gasgiant = load_lottie_url("https://lottie.host/cbfe0175-306e-41ec-b446-a6bbb4c0daa1/SZO6qPM995.json")
lottie_contact = load_lottie_url("https://lottie.host/19292113-e90f-462a-a30a-3507760f5d79/LpuZHZAvlj.json")

## -- PAGE CONFIG --#
page_title = "Darío González Picos"
page_icon = ":smiley:"
layout = "wide"
name = "Darío González Picos"
email = "picos@strw.leidenuniv.nl"
description = "I am interested in the observations and characterization of exoplanets and brown dwarfs. I use high-resolution spectroscopy to characterize their atmospheres and disentangle their formation pathways."
github = "github.com/DGonzalezPicos"
projects = {
    "Project 1": "This is a project I did",
    "Project 2": "This is another project I did"

}
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title)

## -- CSS --#
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    
profile_pic = Image.open(profile_pic)

## -- HERO SECTION --#
col1, col2, col3 = st.columns(3, gap='small')
with col1:
    st.image(profile_pic, width=300)
    
with col2:
    st.header(f'PhD candidate in Astronomy')
    st.subheader(f":email: {email}")

    st.write(description)
    st.write(f"🐙 Github: [{github}](https://{github})")
    st.download_button("Download CV", PDFbyte, file_name=resume_file.name, 
                       mime="application/octet-stream")
    # write emoji for email
    
with col3:
    st_lottie(lottie_gasgiant, height=300)





# lottie_coding = load_lottie_url('https://lottie.host/dec9dfbc-8e17-4d56-9d16-fad90f6f80e0/sTcYOBLMH6.lottie')
lottie_coding = load_lottie_url("https://lottie.host/cbfe0175-306e-41ec-b446-a6bbb4c0daa1/SZO6qPM995.json")
img_contact_form = Image.open('images/IMG_8758.jpg')


        
## -- MY PROJECTS --#

with st.container():
    st.write('----')
    st.header("My projects")
    st.write('##')
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image('images/IMG_8758.jpg', width=300)
    with text_column:
        st.write('### Project 1')
        st.write('This is a project I did')
        st.write('### Project 2')
        st.write('This is another project I did')
        
## -- EXPERIENCE and SKILLS --#
st.write('----')
st.write('#')
st.subheader("Experience and skills")
st.write(
    '''
    I have experience in:
    - Observational astronomy
    - Data reduction
    - Bayesian inference
    - Python programming
    - Bash scripting
    - MPI parallelization
    '''
    )

## -- EDUCATION --#
st.write('----')
st.write('#')
st.subheader("📚 Education")
st.write('#')
st.write('🚧', "**PhD candidate | Leiden University**")
st.write('2023 - present')
st.write(
    '''
    - Characterization of exoplanets and brown dwarfs with high-resolution spectroscopy
    - Disentangling formation pathways of super-Jupiters and brown dwarfs
    - New techniques for spectroscopy of directly imaged exoplanets
    '''
    )
st.write('#')
st.write('🎓', "**MSc Astronomy | Leiden University**")
st.write('2021 - 2023')
st.write(
    '''
    - Thesis: "High-resolution spectroscopy of day-side emission of ultra-hot Jupiter WASP-189b"
    - First Research Project: "Looking for transiting circumplanetary disks in ASAS-SN"
    - Publications: [Kenworthy, González Picos et al. 2021](https://arxiv.org/abs/2107.13582)
    '''
    )

st.write('#')
st.write('🎓', "**BSc Physics | Universitat de Barcelona**")
st.write('2016 - 2020')
st.write(
    '''
    - Thesis: "Characterizing exoplanet atmospheres with ARIEL"
    '''
    )