import streamlit as st 
import spacy_streamlit
import spacy
from spacy import displacy
from pathlib import Path
path = Path("en_core_web_sm")
nlp = spacy.load(path)

import os
from PIL import Image


def main():
	"""A Simple NLP app with Spacy-Streamlit"""
	
	st.title("NER APP USING SPACY by NAVANEETH")
	our_image = Image.open(os.path.join('img.jpg'))
	st.image(our_image)

	menu = ["NER"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "NER":
		st.subheader("NAMED ENTITY RECOGNITION")
		raw_text = st.text_area("PASTE YOUR TEXT BELOW AND PRESS CTRL+ENTER","Enter Text Here")
		docx = nlp(raw_text)
		spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)

if __name__ == '__main__':
	main()
  
