import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class t {
    public static void main(String[] args) throws IOException {
        String[] content = Files.readString(Paths.get("input.txt"), StandardCharsets.UTF_8).strip().split("\r?\n");

        int soma = 0;
        int match = 0;
        for (String txt : content) {
            int b1 = (txt.charAt(0) - 'A');
            int b2 = (txt.charAt(2) - 'X');

            if (b1 == b2)
                match = 3;
            else if (b1 == (((b2 + 2) % 3)))
                match = 6;
            else
                match = 0;
            soma += (b2 + 1) + match;
        }
        System.out.printf("Round 1: %s%n", soma);

        soma = 0;
        for (String txt : content) {
            int b1 = (txt.charAt(0) - 'A');
            int b2 = (txt.charAt(2) - 'X');

            match = (b1 + b2) % 3;
            if (match == 0)
                match = 3;

            soma += match + (b2 * 3);
        }
        System.out.printf("Round 2: %s%n", soma);
    }
}
