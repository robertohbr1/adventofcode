DROP TABLE IF EXISTS #t;DROP TABLE IF EXISTS #v1;DROP TABLE IF EXISTS #v2;

-- Carrega uma lista de numeros abaixo, por exemplo:
--64256   78813
--46941   56838
--47111   50531
--48819   41511
--...

create table #t(lin varchar(100));
BULK INSERT #t
   FROM 'C:\Python\AdventOfCode\2024\Day01\input.txt'
   WITH (
      FIELDTERMINATOR = '\t',
      rowtERMINATOR = '\n',
      KEEPNULLS
   );

-- Separar em duas colunas e ordenar
select num, ROW_NUMBER() OVER (ORDER BY num) AS RowNum into #v1 from (select left(lin, charindex(' ', lin) - 1) + 0 num from #t) a;
select num, ROW_NUMBER() OVER (ORDER BY num) AS RowNum into #v2 from (select right(lin, charindex(' ', reverse(lin)) - 1) + 0 num from #t) a;

-- O resultado 1 é a soma das diferenças entre os valores das duas colunas ordenadas
select '1:' Result, sum(abs(#v1.num - #v2.num)) from #v1 inner join #v2 on #v1.RowNum = #v2.RowNum
union all
-- O resultado 2 é o valor da primeira coluna * (multiplicado) pela quantidade de ocorrências na segunda coluna
select '2:' Result, sum(num) from (select (#v1.num * (select count(*) from #v2 where #v2.num = #v1.num)) num from #v1) a;
