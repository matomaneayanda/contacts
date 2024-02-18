create database if not exists contacts;

use contacts;

create table numbers (
name varchar(100),
last_name varchar(100),
cellphone_number varchar(10),
primary key (cellphone_number)
);
commit;