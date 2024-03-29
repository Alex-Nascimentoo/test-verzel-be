# Lista de veículos à venda - API

## Instruções de uso

### Com docker
__1.__ Após clonar o repositório localmente, inicialize o app com o comando ```docker compose up -d``` e a aplicação estará pronta para os testes.

Este comando irá criar um container chamado ```test-verzel-container``` rodando a aplicação Flask na **porta 8080** e outro container chamado ```verzel-db``` rodando um banco de dados MySQL.

#

### Sem docker

__1.__ Após clonar o repositório localmente, baixe as dependências listadas no arquivo ```requirements.txt```

__2.__  Com as dependências prontas, crie seu bando de dados MySQL e crie a tabela com o seguite código:
```sql
CREATE TABLE vehicles (
  id integer not null auto_increment primary key,
  brand varchar(100),
  model varchar(100),
  v_version varchar(100),
  price integer,
  color varchar(100),
  category varchar(100),
  engine varchar(100),
  transmission varchar(100),
  v_year integer,
  km_old integer,
  photo varchar(256) not null
);
```

__3.__ Agore conecte a API ao seu banco de dados MySQL a partir da linha 9 do arquivo ```app.py```.

__4.__ Para poder rodar o app Flask, adicione a variável que indica o app a ser executado, utilize o comando ```export FLASK_APP=app```.

__5.__ Agora é só inicializar a aplicação em Flask com o comando ```flask run``` e estamos prontos para testar o aplicativo.

## Rotas

__POST__ ```http://localhost:5000/api/users/login``` retorna um JSON com o seguinte objeto:
```json
{
  "message": "Logged in successfully",
  "token": "token<string>"
}
```

__GET__ ```http://localhost:5000/api/vehicles``` retorna um JSON com uma lista de objetos do tipo:
```javascript
{
  "id": number,
  "brand": string,
  "model": string,
  "version": string,
  "price": number,
  "color": string,
  "category": string,
  "engine": string,
  "transmission": string,
  "year": number,
  "km_old": number,
  "photo": string
},
```

__GET__ ```http://localhost:5000/api/vehicles/:id``` retorna um JSON com um único objeto do mesmo tipo acima

__POST__ ```http://localhost:5000/api/vehicles?token={token<string>}``` cadastra um novo veículo no banco de dados e retorna o mesmo com o código HTTP 201. A rota espera um JSON no body do tipo:
```javascript
{
	"brand": string,
	"model": string,
	"version": string,
	"price": number,
	"color": string,
	"category": string,
	"engine": string,
	"transmission": string,
	"year": number,
	"km_old": number,
	"photo": string
}
```

__PUT__ ```http://localhost:5000/api/vehicles?id={id<int>}&token={token<string>}``` atualiza o veículo especificado pelo id. A rota espera um objeto JSON no body do igual ao da rota acima.

__DELETE__ ```http://localhost:5000/api/vehicles/:id``` deleta um veículo do banco de dados de acordo com o id especificado na rota.










