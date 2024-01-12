# Lista de veículos à venda - API

## Instruções de uso

### Com docker
__1.__ Após clonar o repositório localmente, baixe as dependências com o comando ```pip install flask flask-cors mysql-connector-python pyjwt```

__2.__ Com as dependências prontas, rode o comando ```docker compose up -d```, isso irá subir um contâiner de nome "db" com MySQL na porta 3306, lá vai estar o banco e cinco registros pré-prontos para testar a aplicação.

__3.__ Para poder rodar o app Flask adicione a variável que indica o app a ser executado, utilize o comando ```export FLASK_APP=main```.

__4.__ Agora é só inicializar a aplicação em Flask com o comando ```flask run``` e estamos prontos para testar o aplicativo.

#

### Sem docker

__1.__ Após clonar o repositório localmente, baixe as dependências com o comando ```pip install flask flask-cors mysql-connector-python pyjwt```

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

__3.__ Agore conecte a API ao seu banco de dados MySQL a partir da linha 9 do arquivo ```main.py```.

__4.__ Para poder rodar o app Flask adicione a variável que indica o app a ser executado, utilize o comando ```export FLASK_APP=main```.

__5.__ Agora é só inicializar a aplicação em Flask com o comando ```flask run``` e estamos prontos para testar o aplicativo.

## Rotas

__GET__ ```http://localhost:5000/vehicles``` retorna um JSON com uma lista de objetos do tipo:
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

__GET__ ```http://localhost:5000/vehicles/:id``` retorna um JSON com um único objeto do mesmo tipo acima

__POST__ ```http://localhost:5000/vehicles``` cadastra um novo veículo no banco de dados e retorna o mesmo com o código http 201. A rota espera um JSON no body do tipo:
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

__PUT__ ```http://localhost:5000/vehicles/:id``` atualiza o veículo especificado pelo id. A rota espera um objeto JSON no body do igual ao da rota acima.

__DELETE__ ```http://localhost:5000/vehicles/:id``` deleta um veículo do banco de dados de acordo com o id especificado na rota.










