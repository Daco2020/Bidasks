-- mysql내 명령어 : source db_schema.sql

CREATE DATABASE ant_test_db CHARACTER SET UTF8;

use ant_test_db;

CREATE TABLE codes(
    id           INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    code         VARCHAR(10) NOT NULL UNIQUE KEY
)CHARSET=utf8;

CREATE TABLE bidasks(
    id         INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    code       VARCHAR(10) NOT NULL,
    volume     INT NOT NULL,
    bid        INT NOT NULL,
    ask        INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)CHARSET=utf8;

CREATE TABLE test(
    id           INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    columA       VARCHAR(10) NOT NULL,
    columB       VARCHAR(10) NOT NULL,
    columC       VARCHAR(10) NOT NULL,
    columD       VARCHAR(10) NOT NULL
)CHARSET=utf8;

