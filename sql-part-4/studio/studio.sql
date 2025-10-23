SELECT 
    B.title,
    B.original_publication_year
FROM
    BooksDB.dbo.books B
WHERE
    B.average_rating <(SELECT AVG(CAST(R.rating AS FLOAT))
                        FROM BooksDB.dbo.ratings R 
                        WHERE R.book_id = B.book_id
                        )
ORDER BY
    B.original_publication_year,
    B.title;