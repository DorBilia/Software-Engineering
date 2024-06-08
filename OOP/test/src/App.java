import java.util.Arrays;

public class App {
    public static double[] func(double[] numbers) {
        // TODO implement this method to create a new array and return it
        // each number in the new array is a multiplication of the equivalent value in
        // the numbers array, multiplied by 2
        // e.g. for the input {1,2,3} the returned array will be {2,4,6}
        if (numbers.length != 0) {
            double[] res = new double[numbers.length];
            for (int i = 0; i < numbers.length; i++) {
                res[i] = numbers[i] * 2;
            }
            return res;
        }
        return null;
    }

    public static void main(String[] args) throws Exception {
    }
}
