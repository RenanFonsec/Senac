create database db_crud_0223;
use db_crud_0223;

create table pessoas (
id int auto_increment,
nome varchar(70),
dataNasc date,
primary key (id)
);

insert into pessoas value (1, 'Renan', '2005-01-21');
insert into pessoas (nome, dataNasc) value ('Renan', '2005-01-21');
select * from pessoas;

update pessoas set nome = "Mateus" where id = 1;
