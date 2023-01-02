import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class t {

    private static int marker(String input, int length) {
        for (int i = 0; i < input.chars().count(); i++) {
            if (input.substring(i, i + length).chars().distinct().count() == length) {
                System.out.printf("%d%n", length + i);
                return length + i;
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        String content = new String(Files.readAllBytes(Paths.get("input.txt")));
        marker(content, 4);
        marker(content, 14);
    }

}