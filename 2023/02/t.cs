var lines = File.ReadAllLines("input.txt");
int s1 = 0;
int s2 = 0;

foreach (string line in lines)
{
    
    string lin = line.Substring(5);
    string[] v = lin.Split(": ");
    int x = Int32.Parse(v[0]);
    lin = v[1].Replace(",", ";");
    v = lin.Split("; ");
    int r = 0;
    int g = 0;
    int b = 0;
    foreach (string s in v) {
        string[] v2 = s.Split(" ");
        int q = Int32.Parse(v2[0]);
        string cor = v2[1];
        // Max: 12 red cubes, 13 green cubes, and 14 blue cubes
        if ((cor == "red" && q > 12) || (cor == "green" && q > 13) || (cor == "blue" && q > 14)) {
            x = 0;
        }
        if (cor == "red") {
            r = Math.Max(r, q);}
        else if (cor ==  "green") {
            g = Math.Max(g, q);
        } 
        else if (cor == "blue") {
            b = Math.Max(b, q);
        }
    }
    s1 += x;
    s2 += (r * g * b);
}

Console.WriteLine($"Round 1: {s1}"); // 2156
Console.WriteLine($"Round 2: {s2}"); // 66909
