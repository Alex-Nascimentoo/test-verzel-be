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
  photo varchar(256) not null
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO vehicles (brand, model, v_version, price, color, category, engine, transmission, v_year, km_old, photo) VALUES ('Porsche', 'Cayenne', 'Turbo GT', 500000, 'Azul da meia noite', 'SUV', 'V8 biturbo', 'automatic', 2024, 0, 'https://images.unsplash.com/photo-1696315072523-1bd90867944b?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');

INSERT INTO vehicles (brand, model, v_version, price, color, category, engine, transmission, v_year, km_old, photo) VALUES ('Porsche', '911', 'Carrera GTS', 700000, 'Verde', 'sports', '6 cilindros', 'automatic', 2023, 7000, 'https://images.unsplash.com/photo-1471479917193-f00955256257?q=80&w=1631&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');

INSERT INTO vehicles (brand, model, v_version, price, color, category, engine, transmission, v_year, km_old, photo) VALUES ('Lambroghini', 'Aventador', 'SVJ', 1300000, 'Roxo', 'sports', 'V12', 'automatic', 2021, 50000, 'https://www.carscoops.com/wp-content/uploads/2019/05/5cc2d1db-lamborghini-aventador-svj.jpg');

INSERT INTO vehicles (brand, model, v_version, price, color, category, engine, transmission, v_year, km_old, photo) VALUES ('Lamborghini', 'Revuelto', '', 2100000, 'Laranja', 'sports', 'V12', 'automatic', 2022, 0, 'https://medialamborghini-meride-tv.akamaized.net/meride/lamborghini/video/images/folder1/1252/vlcsnap-2023-03-17-16h18m30s840.jpg');

INSERT INTO vehicles (brand, model, v_version, price, color, category, engine, transmission, v_year, km_old, photo) VALUES ('Audi', 'R8', '', 900000, 'Cinza', 'sports', 'V10', 'automatic', 2019, 30000, 'https://images.unsplash.com/photo-1629450994457-fce28d578d5f?q=80&w=1631&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');