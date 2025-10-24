SELECT
    T.tag_id,
    T.tag_name
FROM
    BooksDB.dbo.tags T
WHERE
    T.tag_id IN (
        -- This subquery finds all tag_ids used over 100,000 times
        SELECT
            BT.tag_id
        FROM
            BooksDB.dbo.book_tags BT
        GROUP BY
            BT.tag_id
        HAVING
            COUNT(BT.tag_id) > 100000 -- Count how many books have each tag
    );