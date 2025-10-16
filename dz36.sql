-- 1. Создать таблицу
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price INT,
    quantity INT
);

-- 2. Добавить записи
INSERT INTO products VALUES (1, 'Яблоко', 50, 120);
INSERT INTO products VALUES (2, 'Груша', 75, 80);
INSERT INTO products VALUES (3, 'Сок', 90, 25);

-- 3. Показать всю таблицу
SELECT * FROM products;

-- 4. Показать только названия
SELECT name FROM products;

-- 5. Найти товар по цене 75
SELECT * FROM products WHERE price = 75;

-- 6. Выдать товары, где quantity > 30
SELECT * FROM products WHERE quantity > 30;

-- 7. Обновить цену яблока
UPDATE products SET price = 60 WHERE name = 'Яблоко';

-- 8. Удалить товар с id = 2
DELETE FROM products WHERE id = 2;

-- 9. Увеличить количество всех товаров на 10
UPDATE products SET quantity = quantity + 10;

-- 10. Показать товары, упорядочить по цене
SELECT * FROM products ORDER BY price;

-- 11. Показать только те, у кого цена > 80 и количество < 100
SELECT * FROM products WHERE price > 80 AND quantity < 100;

-- 12. Выбрать товары, где имя начинается на 'С'
SELECT * FROM products WHERE name LIKE 'С%';

-- 13. Посчитать количество наименований
SELECT COUNT(*) FROM products;

-- 14. Посчитать общий запас
SELECT SUM(quantity) FROM products;

-- 15. Узнать среднюю цену
SELECT AVG(price) FROM products;

-- 16. Получить максимальную цену
SELECT MAX(price) FROM products;

-- 17. Получить минимальную цену
SELECT MIN(price) FROM products;

-- 18. Выдать только уникальные цены
SELECT DISTINCT price FROM products;

-- 19. Группировка по цене, показать сколько товаров по каждой цене
SELECT price, COUNT(*) FROM products GROUP BY price;

-- 20. Показать список товаров, где цена 50 или 90
SELECT * FROM products WHERE price IN (50, 90);

-- 21. Найти товар с самой высокой ценой
SELECT * FROM products WHERE price = (SELECT MAX(price) FROM products);

-- 22. Показать товары, у которых quantity IS NOT NULL
SELECT * FROM products WHERE quantity IS NOT NULL;

-- 23. Изменить название товара на 'Компот', если имя 'Сок'
UPDATE products SET name = 'Компот' WHERE name = 'Сок';

-- 24. Добавить новый товар, если его нет
INSERT INTO products (id, name, price, quantity) 
SELECT 4, 'Вода', 30, 200 WHERE NOT EXISTS 
(SELECT 1 FROM products WHERE name = 'Вода');

-- 25. Удалить все товары, где цена менее 60
DELETE FROM products WHERE price < 60;

-- 26. Показать таблицу после всех изменений
SELECT * FROM products;
