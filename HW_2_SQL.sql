--SQL_DDL
--Первая часть.
--
--Таблица employees
--
--Создать таблицу employees
--- id. serial,  primary key,
--- employee_name. Varchar(50), not null
--Наполнить таблицу employee 70 строками.


CREATE TABLE employees(
	id serial primary key,
	employee_name varchar(50) not null
);

SELECT * FROM employees


-- для заполнения таблицы 70 строками использую скрипт в Python:

--from array import *
--arr = array('i', range(1,71))
--for i in range(len(arr)):
--    print(" %d (default,'Padawan_%d'), " %(i, arr[i]))


INSERT INTO employees(id, employee_name)
VALUES (default,'Padawan_1'),
 (default,'Padawan_2'),
  (default,'Padawan_3'),
  (default,'Padawan_4'),
  (default,'Padawan_5'),
  (default,'Padawan_6'),
  (default,'Padawan_7'),
  (default,'Padawan_8'),
  (default,'Padawan_9'),
  (default,'Padawan_10'),
  (default,'Padawan_11'),
  (default,'Padawan_12'),
  (default,'Padawan_13'),
  (default,'Padawan_14'),
  (default,'Padawan_15'),
  (default,'Padawan_16'),
  (default,'Padawan_17'),
  (default,'Padawan_18'),
  (default,'Padawan_19'),
  (default,'Padawan_20'),
  (default,'Padawan_21'),
  (default,'Padawan_22'),
  (default,'Padawan_23'),
  (default,'Padawan_24'),
  (default,'Padawan_25'),
  (default,'Padawan_26'),
  (default,'Padawan_27'),
  (default,'Padawan_28'),
  (default,'Padawan_29'),
  (default,'Padawan_30'),
  (default,'Padawan_31'),
  (default,'Padawan_32'),
  (default,'Padawan_33'),
  (default,'Padawan_34'),
  (default,'Padawan_35'),
  (default,'Padawan_36'),
  (default,'Padawan_37'),
  (default,'Padawan_38'),
  (default,'Padawan_39'),
  (default,'Padawan_40'),
  (default,'Padawan_41'),
  (default,'Padawan_42'),
  (default,'Padawan_43'),
  (default,'Padawan_44'),
  (default,'Padawan_45'),
  (default,'Padawan_46'),
  (default,'Padawan_47'),
  (default,'Padawan_48'),
  (default,'Padawan_49'),
  (default,'Padawan_50'),
  (default,'Padawan_51'),
  (default,'Padawan_52'),
  (default,'Padawan_53'),
  (default,'Padawan_54'),
  (default,'Padawan_55'),
  (default,'Padawan_56'),
  (default,'Padawan_57'),
  (default,'Padawan_58'),
  (default,'Padawan_59'),
  (default,'Padawan_60'),
  (default,'Padawan_61'),
  (default,'Padawan_62'),
  (default,'Padawan_63'),
  (default,'Padawan_64'),
  (default,'Padawan_65'),
  (default,'Padawan_66'),
  (default,'Padawan_67'),
  (default,'Padawan_68'),
  (default,'Padawan_69'),
  (default,'Padawan_70');
 
-- Таблица salary
--
--Создать таблицу salary
--- id. Serial  primary key,
--- monthly_salary. Int, not null
--Наполнить таблицу salary 15 строками:
--- 1000
--- 1100
--- 1200
--- 1300
--- 1400
--- 1500
--- 1600
--- 1700
--- 1800
--- 1900
--- 2000
--- 2100
--- 2200
--- 2300
--- 2400
--- 2500

CREATE TABLE salary(
	id serial primary key,
	monthly_salary int not null
);

SELECT * FROM salary;

INSERT INTO salary(id, monthly_salary)
VALUES (default ,1000),
(default ,1100),
(default , 1200),
(default ,1300),
(default , 1400),
(default ,1500),
(default ,1600),
(default ,1700),
(default ,1800),
(default , 1900),
(default ,2000),
(default ,2100),
(default ,2200),
(default ,2300),
(default ,2400),
(default ,2500);

--Таблица employee_salary
--
--Создать таблицу employee_salary
--- id. Serial  primary key,
--- employee_id. Int, not null, unique
--- salary_id. Int, not null
--Наполнить таблицу employee_salary 40 строками:
--- в 10 строк из 40 вставить несуществующие employee_id


CREATE TABLE employee_salary(
	id serial primary key,
	employee_id int not null unique,
	salary_id int not null 
	);

SELECT * FROM employee_salary;

--для заполнения строк использую скрипт в Python:
--
--from random import randint
--
--employee = []
--salary = []
--for i in range(40):
--    employee.append(randint(200,300))
--    salary.append(randint(1000,3000))
--
--    print(('default',employee[i],salary[i]))

INSERT INTO employee_salary(id,employee_id,salary_id)
VALUES (default ,3,7),
(default ,1,4),
(default ,5,9),
(default ,40,13),
(default ,23,4),
(default ,11,2),
(default ,52,10),
(default ,15,13),
(default ,26,4),
(default ,16,1),
(default ,33,7),
(default, 207, 2898),
(default, 255, 1306),
(default, 297, 1478),
(default, 291, 1309),
(default, 299, 2998),
(default, 276, 1863),
(default, 215, 1274),
(default, 205, 2160),
(default, 239, 2766),
(default, 208, 2552),
(default, 264, 2739),
(default, 240, 2237),
(default, 268, 2308),
(default, 250, 1717),
(default, 233, 2166),
(default, 246, 2854),
(default, 236, 2893),
(default, 267, 2462),
(default, 216, 1011),
(default, 203, 2304),
(default, 281, 1350),
(default, 254, 1519),
(default, 265, 2446),
(default, 269, 2614),
(default, 271, 2340),
(default, 259, 1928),
(default, 202, 1194),
(default, 279, 1270),
(default, 204, 2648),
(default, 294, 1783);

--Таблица roles
--
--Создать таблицу roles
--- id. Serial  primary key,
--- role_name. int, not null, unique
--Поменять тип столба role_name с int на varchar(30)
--Наполнить таблицу roles 20 строками:
--id role_name
--1 Junior Python developer
--2 Middle Python developer
--3 Senior Python developer
--4 Junior Java developer
--5 Middle Java developer
--6 Senior Java developer
--7 Junior JavaScript developer
--8 Middle JavaScript developer
--9 Senior JavaScript developer
--10 Junior Manual QA engineer
--11 Middle Manual QA engineer
--12 Senior Manual QA engineer
--13 Project Manager
--14 Designer
--15 HR
--16 CEO
--17 Sales manager
--18 Junior Automation QA engineer
--19 Middle Automation QA engineer
--20 Senior Automation QA engineer


CREATE TABLE roles(
	id serial primary key,
	role_name int not null unique
);

SELECT * FROM roles;

ALTER TABLE roles
ALTER COLUMN role_name type varchar(30);

INSERT INTO roles(id,role_name)
VALUES (default,'Junior Python developer'),
(default ,'Middle Python developer'),
(default ,'Senior Python developer'),
(default ,'Junior Java developer'),
(default ,'Middle Java developer'),
(default ,'Senior Java developer'),
(default ,'Junior JavaScript developer'),
(default ,'Middle JavaScript developer'),
(default ,'Senior JavaScript developer'),
(default ,'Junior Manual QA engineer'),
(default ,'Middle Manual QA engineer'),
(default ,'Senior Manual QA engineer'),
(default ,'Project Manager'),
(default ,'Designer'),
(default ,'HR'),
(default ,'CEO'),
(default ,'Sales manager'),
(default ,'Junior Automation QA engineer'),
(default ,'Middle Automation QA engineer'),
(default ,'Senior Automation QA engineer');

--Таблица roles_employee
--
--Создать таблицу roles_employee
--- id. Serial  primary key,
--- employee_id. Int, not null, unique (внешний ключ для таблицы employees, поле id)
--- role_id. Int, not null (внешний ключ для таблицы roles, поле id)
--Наполнить таблицу roles_employee 40 строками.

CREATE TABLE roles_employee(
	id serial primary key,
	employee_id int not null unique,
	role_id int not null,
	foreign key(employee_id) references employees(id),
	foreign key(role_id) references roles(id)
);

SELECT * FROM roles_employee;

INSERT INTO roles_employee(id,employee_id,role_id)
VALUES (default, 45, 12),
(default, 18, 6),
(default, 7, 12),
(default, 64, 13),
(default, 54, 7),
(default, 69, 17),
(default, 34, 14),
(default, 5, 3),
(default, 43, 2),
(default, 49, 19),
(default, 39, 16),
(default, 62, 8),
(default, 4, 1),
(default, 25, 15),
(default, 2, 14),
(default, 67, 5),
(default, 11, 16),
(default, 40, 9),
(default, 19, 18),
(default, 24, 4),
(default, 59, 3),
(default, 6, 4),
(default, 46, 5),
(default, 3, 16),
(default, 36, 20),
(default, 22, 20),
(default, 41, 2),
(default, 57, 10),
(default, 1, 19),
(default, 21, 12);


