DECLARE @v1
TABLE (VALUE bigINT);

INSERT INTO
    @v1 (VALUE)
VALUES
    (125),
    (17);

DECLARE @v2
TABLE (VALUE bigINT);

DECLARE @x INT = 0;

WHILE @x < 25 BEGIN IF @x % 2 = 0 BEGIN
DELETE @v2;

INSERT INTO
    @v2 (VALUE)
SELECT
    CASE
        WHEN VALUE = 0 THEN 1
        WHEN LEN(CAST(VALUE AS VARCHAR)) % 2 = 0 THEN SUBSTRING(
            CAST(VALUE AS VARCHAR),
            1,
            LEN(CAST(VALUE AS VARCHAR)) / 2
        )
        ELSE VALUE * 2024
    END VALUE
FROM
    @v1;

INSERT INTO
    @v2 (VALUE)
SELECT
    SUBSTRING(
        CAST(VALUE AS VARCHAR),
        (LEN(CAST(VALUE AS VARCHAR)) / 2) + 1,
        1000
    ) VALUE
FROM
    @v1
WHERE
    LEN(CAST(VALUE AS VARCHAR)) % 2 = 0;

END ELSE BEGIN
DELETE @v1;

INSERT INTO
    @v1 (VALUE)
SELECT
    CASE
        WHEN VALUE = 0 THEN 1
        WHEN LEN(CAST(VALUE AS VARCHAR)) % 2 = 0 THEN SUBSTRING(
            CAST(VALUE AS VARCHAR),
            1,
            LEN(CAST(VALUE AS VARCHAR)) / 2
        )
        ELSE VALUE * 2024
    END VALUE
FROM
    @v2;

INSERT INTO
    @v1 (VALUE)
SELECT
    SUBSTRING(
        CAST(VALUE AS VARCHAR),
        (LEN(CAST(VALUE AS VARCHAR)) / 2) + 1,
        1000
    ) VALUE
FROM
    @v2
WHERE
    LEN(CAST(VALUE AS VARCHAR)) % 2 = 0;

END
SET
    @x = @x + 1;

IF @x = 25
SELECT
    'Resposta 1:',
    COUNT(*)
FROM
    @v2 END
    -- Rotina muito demorada para calcular 75 vezes
    --select 'Resposta 2:', count_big(*) from @v2