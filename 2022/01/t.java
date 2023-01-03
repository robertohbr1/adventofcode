import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class t {
    public static void main(String[] args) throws IOException {
        String content = Files.readString(Paths.get("input.txt"), StandardCharsets.UTF_8).strip();

        List<Integer> Cals = new ArrayList<>();

        for (String block : content.split("\r?\n\r?\n")) {
            int nSum = 0;
            for (String line : block.split("\r?\n")) {
                nSum += Integer.parseInt(line);
            }
            Cals.add(nSum);
        }
        Cals.sort((a, b) -> b - a);
        System.out.printf("Round 1: %s%n", Cals.get(0));
        System.out.printf("Round 2: %s%n", Cals.get(0) + Cals.get(1) + Cals.get(2));
    }
}
