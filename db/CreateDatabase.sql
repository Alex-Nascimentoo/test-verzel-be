USE verzel;

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
  photo varchar(255)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO vehicles (brand, model, v_version, price, color, category, engine, transmission, v_year, km_old) VALUES ('Porsche', 'Cayenne', 'Turbo GT', 500000, 'Azul da meia noite', 'SUV', 'V8 biturbo', 'automatic', 2024, 0);

INSERT INTO vehicles (brand, model, v_version, price, color, category, engine, transmission, v_year, km_old) VALUES ('Porsche', '911', 'Carrera GTS', 700000, 'Verde', 'sports', '6 cilindros', 'automatic', 2023, 7000);

INSERT INTO vehicles (brand, model, v_version, price, color, category, engine, transmission, v_year, km_old) VALUES ('Lambroghini', 'Aventador', 'SVJ', 1300000, 'Roxo', 'sports', 'V12', 'automatic', 2021, 50000);

INSERT INTO vehicles (brand, model, v_version, price, color, category, engine, transmission, v_year, km_old) VALUES ('Lamborghini', 'Revuelto', '', 2100000, 'Laranja', 'sports', 'V12', 'automatic', 2022, 0);

INSERT INTO vehicles (brand, model, v_version, price, color, category, engine, transmission, v_year, km_old) VALUES ('Audi', 'R8', '', 900000, 'Cinza', 'sports', 'V10', 'automatic', 2019, 30000);