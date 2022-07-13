<h1 align="center">Desafio API PicPay</h1>

<p align="center">Este é o projeto que consiste em uma API que contem um metodo POST que recebe os parametros do iris dataset, essa API retorna a predição através de um modelo de RandomForest</p>

### OS ARQUIVOS :file_folder:

* app
    - IrisData.py -> _Arquivo que recebe os valores inputados no metodo POST da API_
    - main.py -> _Onde a mágica acontece, onde a API é criada, os metodos GET e POST são definidos e onde temos a predição do modelo_
    - randomforest.pkl -> _Pickle File que contem o treino do nosso modelo_
* notebook
    - consumo_api.ipynb -> _Notebook que utilizaremos para consumir a API_
* src
    - IrisTraining.py -> _Onde o nosso modelo foi treinado e a partir desse arquivo obtivemos o randomforest.pkl_
    - iris.csv -> _A nossa fonte de dados para treinarmos o nosso modelo_
* Dockerfile -> _O Dockerfile que irá criar a nossa imagem docker da nossa API_
* requirements.txt -> _A lista de pacotes que intalaremos na nossa imagem Docker_

### O MODELO :chart_with_upwards_trend:

O modelo é um modelo de classificação que da a predição de qual tipo de Iris temos de acordo com o tamanho e comprimento da petala e da sepala da flor, o modelo utilizado foi o RandomForest que foi treinado no arquivo 'IrisTraining.py' e consumo no arquivo 'main.py' atráves do Pickle File 'randomforest.pkl', a predição é o output do método post do endpoint '/predict'

### A API :computer: 

A API foi feita através do framework [Fast API](https://fastapi.tiangolo.com/)
