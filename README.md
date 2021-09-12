# NER_STREAMLIT

A general purpose Named Entity Recognition model using Spacy.
- UI - guarded by Streamlit.
- This application was deployed to Heroku.
-  <strong><b> APP LINK : https://ner-streamlit-nav.herokuapp.com/</b></strong>

### REQUIREMENTS:

* Python 3.7+
* spacy==3.0.0
* streamlit
* spacy_streamlit
* Download the en_core_web_sm package for Spacy v3.0.0 as follows. 
```sh
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz
```

### CREATING VENV IN CONDA:
```sh
conda create --name myenv
```
Using a virtual environment:
```sh
conda activate myenv
```
Deactivating a virtual environment:
```sh
conda deactivate myenv
```
### RUNNING THE APPLICATION:
- Install all the dependencies in the virtual environment.
- Then run :
```sh
streamlit run app.py
```
- Your app will be running in the local server.
- Then deploy the app to Heroku or some other platforms you like!
- Build pack to be added in Heroku :  
```sh
heroku/python
```
- The home page of the web app is shown below:
<div class="row">
    <img src="Home_page.png" title='HomePage' alt="index" style="width:100%">
</div>
