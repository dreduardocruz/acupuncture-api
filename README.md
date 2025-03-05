# Acupuncture App

Este projeto é um aplicativo destinado a médicos acupunturistas, que contém informações abrangentes sobre pontos de acupuntura, meridianos e combinações de pontos, conforme reconhecido pela Organização Mundial da Saúde (OMS).

## Estrutura do Projeto

- **src/app.py**: Ponto de entrada da aplicação. Inicializa o aplicativo e configura as rotas e middleware necessários.
- **src/controllers/points_controller.py**: Contém a classe `PointsController`, que gerencia os pontos de acupuntura, incluindo a recuperação de informações sobre pontos, meridianos e combinações.
- **src/models/point.py**: Define a classe `Point`, representando um ponto de acupuntura com propriedades como nome chinês, localização anatômica e descrição.
- **src/models/meridian.py**: Define a classe `Meridian`, representando um meridiano com suas características e níveis energéticos.
- **src/models/combination.py**: Define a classe `Combination`, que representa combinações de pontos para tratar síndromes da Medicina Tradicional Chinesa e doenças ocidentais.
- **src/routes/points_routes.py**: Define as rotas relacionadas aos pontos de acupuntura, utilizando o `PointsController` para gerenciar as requisições.
- **src/services/points_service.py**: Contém a classe `PointsService`, que implementa a lógica de negócios para manipular dados de pontos, meridianos e combinações.
- **src/types/index.py**: Exporta tipos e interfaces utilizados em todo o projeto, como tipos para requisições e respostas.
- **requirements.txt**: Lista as dependências necessárias para o projeto, incluindo bibliotecas para desenvolvimento web e manipulação de dados.

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   ```
2. Navegue até o diretório do projeto:
   ```
   cd acupuncture-app
   ```
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para iniciar o aplicativo, execute o seguinte comando:
```
python src/app.py
```

O aplicativo estará disponível em `http://localhost:5000`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.