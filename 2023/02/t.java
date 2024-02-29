import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class t {
    public static void main(String[] args) throws IOException {

        String cal = Files.readString(Paths.get("input.txt"), StandardCharsets.UTF_8).strip();
        int s1 = 0;
        int s2 = 0;
        for (String lin : cal.split("\r?\n")) {
            lin = lin.substring(5);
            String[] v = lin.split(": ");
            int x = Integer.valueOf(v[0]);
            lin = v[1].replace(",", ";");
            v = lin.split("; ");
            int r = 0;
            int g = 0;
            int b = 0;
            for (String s : v) {
                String[] v2 = s.split(" ");
                int q = Integer.valueOf(v2[0]);
                String cor = v2[1];
                // Max: 12 red cubes, 13 green cubes, and 14 blue cubes
                if ((cor.equals("red") && q > 12)
                        || (cor.equals("green") && q > 13)
                        || (cor.equals("blue") && q > 14)) {
                    x = 0;
                }
                if (cor.equals("red")) {
                    r = Math.max(r, q);}
                else if (cor.equals("green")) {
                    g = Math.max(g, q);
                } 
                else if (cor.equals("blue")) {
                    b = Math.max(b, q);
                }
            }
            s1 += x;
            s2 += (r * g * b);
        }

        System.out.printf("Round 1: %s%n", s1); // 2156
        System.out.printf("Round 2: %s%n", s2); // 66909
    }
}
