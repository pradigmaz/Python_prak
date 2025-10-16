-- 1. Создать таблицу сотрудников
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary INT,
    hired DATE
);

-- 2. Добавить сотрудников
INSERT INTO employees VALUES (1, 'Иванов И.И.', 'Менеджер', 40000, '2022-01-10');
INSERT INTO employees VALUES (2, 'Петров П.П.', 'Программист', 60000, '2022-02-15');
INSERT INTO employees VALUES (3, 'Сидоров С.С.', 'Бухгалтер', 35000, '2023-03-05');

-- 3. Выбрать всех сотрудников
SELECT * FROM employees;

-- 4. Найти программиста
SELECT * FROM employees WHERE position = 'Программист';

-- 5. Изменить зарплату Иванова
UPDATE employees SET salary = 45000 WHERE name = 'Иванов И.И.';

-- 6. Уволить бухгалтера
DELETE FROM employees WHERE position = 'Бухгалтер';

-- 7. Выбрать сотрудников с зарплатой больше 40000
SELECT * FROM employees WHERE salary > 40000;

-- 8. Добавить нового, если пусто
INSERT INTO employees (id, name, position, salary, hired) VALUES (4, 'Новиков Н.Н.', 'Аналитик', 50000, '2023-10-01');

-- 9. Отсортировать по дате найма
SELECT * FROM employees ORDER BY hired;

-- 10. Показать только имя и зарплату
SELECT name, salary FROM employees;

-- 11. Обновить позицию сотрудника с id = 2
UPDATE employees SET position = 'Старший программист' WHERE id = 2;

-- 12. Посчитать количество сотрудников
SELECT COUNT(*) FROM employees;

-- 13. Узнать среднюю зарплату
SELECT AVG(salary) FROM employees;

-- 14. Найти сотрудников, у которых имя начинается на П
SELECT * FROM employees WHERE name LIKE 'П%';

-- 15. Показать всех, где зарплата или 35000 или 50000
SELECT * FROM employees WHERE salary IN (35000, 50000);