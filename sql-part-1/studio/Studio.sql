SELECT TOP 3
    Authors,
    average_rating
FROM 
    books
ORDER BY Authors DESC, average_rating DESC;