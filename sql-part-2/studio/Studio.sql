SELECT count(language_code) AS 'ENGLISH TITLES'
FROM BooksDB.dbo.books
WHERE LEFT(language_code,2) <> 'en';