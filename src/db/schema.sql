
DROP TABLE IF EXISTS candy;
DROP TABLE IF EXISTS users;


CREATE TABLE candy(
    id              SERIAL PRIMARY KEY,
    competitorname	TEXT,
    chocolate	        BOOLEAN,
    fruity	          BOOLEAN,
    caramel	          BOOLEAN,
    peanutyalmondy	  BOOLEAN,
    nougat	          BOOLEAN,
    crispedricewafer  BOOLEAN,
    hard	            BOOLEAN,
    bar	              BOOLEAN,
    pluribus	        BOOLEAN,
    sugarpercent	    DECIMAL,
    pricepercent	    DECIMAL,
    winpercent        DECIMAL
);

CREATE TABLE users(
    id  SERIAL PRIMARY KEY,
   username varchar (50),
   password varchar (400),
   session_key  TEXT
);
INSERT INTO users (id,username, password) VALUES (1,'shubham', '10f6d3ce9d854d1ebfc1ca7d1981fafc122a9970093382f2c5c72cfa6ab47572');
INSERT INTO users (id,username, password,session_key) VALUES (2,'jason', '9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1','c4fb0455f432a7176325b89b8a2003c82e41fc27a5ab07c15a64fc036e4563a4');
