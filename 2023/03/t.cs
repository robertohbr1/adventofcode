var linesFile = File.ReadAllLines("input.txt");

var cal = new string[linesFile.Length + 2];

var x = 1;
foreach (string line in linesFile)
{
    cal[x++] = "." + line + ".";
}
cal[0] = new String('.', cal[1].Length);
cal[x] = cal[0];

var digits = "0123456789";
var digitsPoint = digits + ".";

int s1 = 0;
int s2 = 0;

for (x = 1; x < cal.Length - 1; x++)
{
    var y = 1;
    while (y <= cal[0].Length - 1)
    {
        if (digits.Contains(cal[x][y]))
        {
            var inic = y;
            y++;
            while (digits.Contains(cal[x][y]))
            {
                y++;
            }
            var fim = y - 1;
            s1 += TestaNum(x, inic, fim);
        }
        else
        {
            y += 1;
        }
    }
}

for (x = 1; x < cal.Length - 1; x++)
{
    for (var y = 1; y <= cal[0].Length - 1; y++)
    {
        if (cal[x][y] == '*')
        {
            s2 += TestaMult(x, y);
        }
    }
}

Console.WriteLine($"Round 1: {s1}"); // 546312
Console.WriteLine($"Round 2: {s2}"); // 87449461

int TestaNum(int lin, int inic, int fim)
{
    for (var x = lin - 1; x <= lin + 1; x++)
    {
        for (var y = inic - 1; y <= fim + 1; y++)
        {
            if (!digitsPoint.Contains(cal[x][y]))
            {
                return Int32.Parse(cal[lin].Substring(inic, fim - inic + 1));
            }
        }
    }
    return 0;
}

void buscaNum(int lin, int col, List<int> list)
{
    if (digits.Contains(cal[lin][col]))
    {
        while (digits.Contains(cal[lin][col - 1]))
        {
            col--;
        }
        var s = "";
        while (digits.Contains(cal[lin][col]))
        {
            s += cal[lin][col];
            col++;
        }
        list.Add(Int32.Parse(s));
    }
}

int TestaMult(int lin, int col)
{
    List<int> list = new List<int>();
    for (var x = lin - 1; x <= lin + 1; x++)
    {
        if (digits.Contains(cal[x][col]))
        {
            buscaNum(x, col, list);
        }
        else
        {
            buscaNum(x, col - 1, list);
            buscaNum(x, col + 1, list);
        }
    }
    if (list.Count > 1)
    {
        return list[0] * list[1];
    }
    else
    {
        return 0;
    }
}