"""
Created on Wed Apr  1 15:37:04 2020
@author : Karim Gheddache

"""

import pandas as pd
import streamlit as st
from streamlit import components


df = pd.read_csv('british_airways_clean.csv')

st.title("Les avis clients sur British Airways ")

st.sidebar.title('Sommaire')
pages = st.sidebar.radio('Navigation', ['Présentation du Projet', 'Analyses des Avis', 'Modélisation des sujets abordés'])

if pages == 'Présentation du Projet':
    st.image("graphiques/British_airways_data_science_project.jpg")
    st.write("## Présentation du Projet ")
    st.write("L’industrie aérienne est l’une des industries les plus importantes au monde. C’est un contributeur majeur à l’économie mondiale et c’est également un acteur clé dans la mobilité mondiale des personnes et des biens. Le secteur du transport aérien est un secteur très compétitif et il est important que les compagnies aériennes comprennent leurs clients afin de leur fournir le meilleur service possible.")
    st.write("Pour British Airways l'objectif de ce projet est d'analyser les avis des clients de British Airways afin de comprendre leurs besoins et leurs attentes. ")
    st.write("###### En ce qui me concerne j'ai fait cette étude car je dois aller à Trinidad et Tobago (l'année prochaine) pour une compétition de Steel Band(l'instrument de musique national trinidadien. Le voyage le plus direct se fait avec British Airways...).")
    
    st.write("## Collecte des données")
    st.write("Les données ont été collectées à partir du site web https://www.airlinequality.com/. SkyTrax est une plateforme d'avis en ligne qui permet aux entreprises de collecter et de gérer les avis des clients.  J'ai collecté et agrégé 3731 avis de clients de British Airways entre le 9 octobre 2011 et le 9 janvier 2024. ")
    st.dataframe(df.head())


if pages == 'Analyses des Avis':
    st.write("## Analyses des Avis")
    st.write("#### Notes moyennes des passagers depuis 2011")
    st.image("graphiques/mean_rating.png", width=800)
    st.write("Les notes ne sont pas bonnes sur British Airways avec plus de 2 passagers sur 10 qui donnent la note minimale de 1/10 et 50% des passagers qui donnent une note inférieure à 5/10. ")
    st.write("#### Evaluation du service au sol")
    st.image("graphiques/ground.png", width=800)
    st.write("Les passagers perçoivent le service au sol comme mauvais voire très mauvais. ")  
    st.write("#### Evaluation du service à bord")
    st.image("graphiques/cabin_staff.png", width=800)
    st.write("Les passagers perçoivent le service à bord comme bon voire trsè bon. C'est le service le mieux noté par les passagers. ")
    st.write("#### Evaluation de la nourriture")
    st.image("graphiques/food.png", width=800)
    st.write("Près de 40% des passagers perçoivent la nourriture comme mauvaise. Le reste des passagers est satisfait ")
    st.write("#### Evaluation du divertissement")
    st.image("graphiques/entertainment.png", width=800)
    st.write("Cette rubrique ne concerne que les vols long courrier, d'où le nombre élevé de manquants. Le retour client est plutôt mauvais. ")
    st.write("#### Evaluation du rapport qualité prix")
    st.image("graphiques/value.png", width=800)
    st.write("Les passagers perçoivent le rapport qualité prix comme mauvais. ")
    st.header("Conclusion")
    st.write("graphiques/Les passagers sont globalement insatisfaits du service de British Airways. Ils sont particulièrement insatisfaits du service au sol et de la nourriture.  ")
    st.image("graphiques/moyenne_mensuelle.png", width=800)
    st.write("###### Attention toutefois à l'interprétation de ces résultats. La période Covid a été entraîné une forte volatilité des avis avec des notes de 1/10 qui n'avaient jamais été données auparavant ni après. Il faudrait faire une étude plus approfondie pour comprendre les raisons de cette forte volatilité. ")

if pages == 'Modélisation des sujets abordés':
    st.write("## Topics Modeling")
    st.write("#### Visualisation des sujets")
    st.write("#### Après modélisation des sujets abordés par les passagers, on obtient le graphique intéractif suivant : ")
    with open('lda.html', 'r') as f:
        html_string = f.read()
    components.v1.html(html_string, width=1300, height=800, scrolling=False)
    st.write('Le Topic 1 est le plus important avec 71% des avis. Il est associé aux mots clés suivants : "siège, classe, personnel navigant, temps, service, lounge, repas. ')
    st.write("Les autres topics sont moins importants et sont associés à la destination.")
    st.write('Le Topic 1 est le plus grand, les plus éloigné des autres et est situé à gauche. Cela indique que les passagers sont plus préoccupés par le service que par les autres sujets.')
    st.write("#### Visualisation du nuage de mots")
    st.image("graphiques/wordcloud.png", width=800)
    st.write('Selon les nuages de mots les passagers semblent très insastisfaits de la compagnie British Airways')
    st.write("## Réservation ou pas ? ")
    st.write("###### hum ....je vais voir s'il y a d'autres alternatives ! ")

    



        





