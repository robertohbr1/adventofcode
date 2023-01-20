import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class t {

    public static String letters() {
        return "abcdefghijklmnopqrstuvwxyz";
    }

    private static int Calc(String c) {
        String lowerupper = letters() + letters().toUpperCase();
        return (lowerupper.indexOf(c) + 1);
    }

    public static void main(String[] args) throws IOException {
        String[] content = Files.readString(Paths.get("input.txt")).split("\n");
        int soma = 0;
        for (String txt : content) {
            int md = txt.length() / 2;
            for (String c : txt.substring(0, md).split("")) {
                if (txt.substring(md).indexOf(c) > -1) {
                    soma += Calc(c);
                    break;
                }
            }
        }
        System.out.printf("Round 1: %s%n", soma);

        soma = 0;
        for (int y = 0; y < content.length; y += 3) {
            for (String c : content[y].split("")) {
                if ((content[y + 1].indexOf(c) > -1) && (content[y + 2].indexOf(c) > -1)) {
                    soma += Calc(c);
                    break;
                }
            }
        }
        System.out.printf("Round 2: %s%n", soma);
    }
}
