public class Aproximacion1 {
    public static void main(String[] args) {
        double x = -0.75;
        int n = 0;
        double resultado = 1.0;
        double z = 0.00000001; // 8 cifras significativas

        double termino = 1.0;
        double factorial = 1.0;

        do {
            n++;
            termino *= x / n;
            factorial *= n;

            resultado += termino;

            double epsilonA = Math.abs((Math.exp(x) - resultado) / Math.exp(x)) * 100;

            System.out.printf("Iteración %d: %.8f, εa = %.8f%%\n", n, resultado, zA);
        } while (Math.abs(termino / resultado) > epsilon);

        System.out.println("\nResultado final: " + resultado);
        System.out.println("Número de iteraciones: " + n);
    }
}