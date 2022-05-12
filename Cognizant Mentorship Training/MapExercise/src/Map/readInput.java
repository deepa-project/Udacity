package Map;

public class readInput {

    public static void main(String[] args) {

        String input = "";
        System.out.println("Enter the input");

        while (!input.equals("exit")) {
            input = System.console().readLine();
            System.out.println(input);
        }

    }

}
