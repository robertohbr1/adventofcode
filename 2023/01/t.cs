var lines = File.ReadAllLines("input.txt");
var counter1 = 0;
var counter2 = 0;

foreach (var line in lines)
{
    int RetNum(string s)
    {
        return (s.First(Char.IsDigit) - '0') * 10 + s.Last(Char.IsDigit)  - '0';
    }
    string ReplaceNums(string s)
    {
        string[] nums = { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
        for(int x = 1; x <= nums.Length; x++)
        {
            s = s.Replace(nums[x - 1], nums[x - 1][0].ToString() + x.ToString() + nums[x - 1][nums[x - 1].Length - 1].ToString());
        }
        return s;
    }


    counter1 += RetNum(line);
    counter2 += RetNum(ReplaceNums(line));
}

Console.WriteLine($"Round 1: {counter1}"); // 55386
Console.WriteLine($"Round 2: {counter2}"); // 54824
