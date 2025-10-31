--Start by joining the `books` and `book_tags` tables ON the `books.best_book_id` and `book_tags.goodreads_book_id`. We want the *most popular* book, so think about ordering the table in a way that will display both the book title and the number of times a book tag has been used.

--Minimum Desired output:_  The title of the most tagged book, and the number of times the book has been tagged.

SELECT
    b.title
FROM
    BooksDB.dbo.books AS b
INNER JOIN
    BooksDB.dbo.to_read AS tr ON b.book_id = tr.book_id
WHERE
    tr.user_id = 38457; 