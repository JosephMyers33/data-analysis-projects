SELECT
    title,
    authors,
    average_rating
FROM
    BooksDB.dbo.books
WHERE
    authors LIKE 'Brandon Sanderson%' OR
    authors LIKE 'J.K. Rowling%' OR
    authors LIKE 'Lane T. Dennis%'
ORDER BY
    authors ASC,
    average_rating DESC;