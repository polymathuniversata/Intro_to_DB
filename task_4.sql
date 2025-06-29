-- Use the alx_book_store database
USE alx_book_store;

-- Print full description of books table without using DESCRIBE or EXPLAIN
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'Books';
