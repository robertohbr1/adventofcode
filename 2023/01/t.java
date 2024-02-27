import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class t {
    public static int Soma(String dados) {
        int sum = 0;
        for (String block : dados.split("\r?\n")) {
            String onlyNum = block.replaceAll("[a-z]", "");
            sum += ((onlyNum.charAt(0) - '0') * 10) + (onlyNum.charAt(onlyNum.length() - 1) - '0');
        }
        return sum;
    }

    public static int Ajusta(String dados) {
        String[] nums = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        for (int i = 1; i <= 9; i++) {
            String numStr = nums[i];
            dados = dados.replaceAll(numStr, numStr.charAt(0) +  Integer.toString(i) + numStr.charAt(numStr.length() - 1));
        }
        return Soma(dados);
    }

    public static void main(String[] args) throws IOException {

        String content = Files.readString(Paths.get("input.txt"), StandardCharsets.UTF_8).strip();

        System.out.printf("Round 1: %s%n", Soma(content)); // 55386
        System.out.printf("Round 2: %s%n", Ajusta(content)); // 54824
    }
}
