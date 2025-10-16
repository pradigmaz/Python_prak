-- 1. Создать таблицу книг
CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    year INT,
    price INT
);

-- 2. Добавить данные о книгах
INSERT INTO books VALUES (1, 'Мотивация', 'Rifkin', 2021, 450);
INSERT INTO books VALUES (2, 'Парадокс', 'Liu', 2019, 300);
INSERT INTO books VALUES (3, 'Выбор', 'Moti', 2022, 390);

-- 3. Показать все книги
SELECT * FROM books;

-- 4. Найти книгу по автору
SELECT * FROM books WHERE author = 'Rifkin';

-- 5. Показать книги, изданные позже 2020
SELECT * FROM books WHERE year > 2020;

-- 6. Показать все уникальные авторы
SELECT DISTINCT author FROM books;

-- 7. Увеличить цену всех книг на 10
UPDATE books SET price = price + 10;

-- 8. Показать максимальную цену книги
SELECT MAX(price) FROM books;

-- 9. Показать минимальную цену
SELECT MIN(price) FROM books;

-- 10. Подсчитать среднюю цену
SELECT AVG(price) FROM books;

-- 11. Посчитать количество книг каждого автора
SELECT author, COUNT(*) FROM books GROUP BY author;

-- 12. Показать сумму всех цен книг
SELECT SUM(price) FROM books;

-- 13. Удалить книгу Moti
DELETE FROM books WHERE author = 'Moti';

-- 14. Показать оставшиеся книги, отсортировать по году издания
SELECT * FROM books ORDER BY year;
