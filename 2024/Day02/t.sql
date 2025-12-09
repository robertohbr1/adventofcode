DROP TABLE IF EXISTS #t;

/* Exemplo de lista
51 52 55 58 60 61 62 61
64 65 67 70 72 74 77 77
2 4 6 9 11 14 18
79 81 82 84 86 88 91 97
81 83 84 81 83
...
 */
CREATE TABLE
    #t (lin VARCHAR(100));

BULK INSERT #t
FROM
    'C:\Python\AdventOfCode\2024\Day02\input.txt'
WITH
    (
        FIELDTERMINATOR = '\t',
        rowtERMINATOR = '\n',
        KEEPNULLS
    );

DECLARE @r INT,
@total1 INT = 0,
@total2 INT = 0;

DECLARE @lin VARCHAR(1000);

DECLARE lines_cursor CURSOR FOR
SELECT
    lin
FROM
    #t;

OPEN lines_cursor
FETCH NEXT
FROM
    lines_cursor INTO @lin WHILE @@FETCH_STATUS = 0 BEGIN DECLARE @v1
TABLE (row INT, VALUE INT);

DECLARE @v2
TABLE (row INT, VALUE INT, difer INT);

DELETE @v1;

INSERT INTO
    @v1 (row, VALUE)
SELECT
    ROW_NUMBER() OVER (
        ORDER BY
            (
                SELECT
                    0
            )
    ) AS row,
    CAST(VALUE AS INT) VALUE
FROM
    string_split (@lin, ' ');

DECLARE @ut INT,
@x INT;

SELECT
    @ut = MAX(row)
FROM
    @v1;

SET
    @x = 0;

SET
    @r = 0;

WHILE @x <= @ut BEGIN
DELETE @v2;

INSERT INTO
    @v2 (row, VALUE, difer)
SELECT
    row,
    VALUE,
    CAST(VALUE AS INT) - CAST(
        LAG(VALUE) OVER (
            ORDER BY
                row
        ) AS INT
    ) AS difer
FROM
    @v1
WHERE
    row <> @x;

/* Conta as sequencias onde os números estão em sequencia (positiva ou negativa), sem números repetidos e sem diferença entre os números consecutivos maior que 3 */
/* Quando @x = 0, testa todos os valores, e se Ok, adiciona 1 em total1 e 1 em total2 */
/* Quando @x > 0, testa retirando um valor em cada execução e se Ok (sem esse valor retirado), adiciona 1 somente em total2 */
SELECT
    @r = 1
FROM
    @v2
WHERE
    difer IS NULL
    AND NOT EXISTS (
        SELECT
            1
        FROM
            @v2
        WHERE
            difer = 0
            OR ABS(difer) > 3
    )
    AND EXISTS (
        SELECT
            1
        FROM
            (
                SELECT
                    MIN(difer) i,
                    MAX(difer) m
                FROM
                    @v2
            ) tab
        WHERE
            (
                i > 0
                AND m > 0
            )
            OR (
                i < 0
                AND m < 0
            )
    );

IF @r = 1 BEGIN IF @x = 0
SET
    @total1 = @total1 + @r
SET
    @total2 = @total2 + @r BREAK END
SET
    @x = @x + 1 END
FETCH NEXT
FROM
    lines_cursor INTO @lin;

END;

CLOSE lines_cursor;

DEALLOCATE lines_cursor;

SELECT
    '1:' Result,
    @total1
UNION ALL
SELECT
    '2:' Result,
    @total2;