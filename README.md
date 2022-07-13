<h1 align="center">Desafio API PicPay</h1>

<p align="center">Este é o projeto que consiste em uma API que contem um metodo POST que recebe os parametros do iris dataset, essa API retorna a predição através de um modelo de RandomForest</p>

### OS ARQUIVOS :file_folder:

* app
    - IrisData.py -> _Arquivo que recebe os valores inputados no metodo POST da API_
    - main.py -> _Onde a mágica acontece, onde a API é criada, o metodo POST é definido e onde temos a predição do modelo_
    - randomforest.pkl -> _Pickle File que contem o treino do nosso modelo_
* notebook
    - consumo_api.ipynb -> _Notebook que utilizaremos para consumir a API_
* src
    - IrisTraining.py -> _Onde o nosso modelo foi treinado e a partir desse arquivo obtivemos o randomforest.pkl_
    - iris.csv -> _A nossa fonte de dados para treinarmos o nosso modelo_
* Dockerfile -> _O Dockerfile que irá criar a nossa imagem docker da nossa API_
* requirements.txt -> _A lista de pacotes que intalaremos na nossa imagem Docker_

### O MODELO :chart_with_upwards_trend:

O modelo é um modelo de classificação que da a predição de qual tipo de Iris temos de acordo com o tamanho e comprimento da petala e da sepala da flor, o modelo utilizado foi o [RandomForest](https://towardsdatascience.com/understanding-random-forest-58381e0602d2) que foi treinado no arquivo 'IrisTraining.py' e consumo no arquivo 'main.py' atráves do Pickle File 'randomforest.pkl', a predição é o output do método post do endpoint '/predict'

### A API :computer: 

A API foi feita através do framework [Fast API](https://fastapi.tiangolo.com/), a API aceita requisições http para o ip 35.175.141.255, a API apenas tem um método POST na porta 80 para o endpoint '/predict', então nossa url final é 'http://35.175.141.255:80/predict', esse metodo post recebe um json no seu body, esse json deve contem os seguintes chaves: 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', todas recebendo seus devidos valores, isso será mostrado melhor quando fizermos o teste de chamar a API através do notebook.
