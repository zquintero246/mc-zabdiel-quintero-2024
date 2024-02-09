import java.util.*;




//PROFE, LO HICE EN UN COMPILADOR ONLINE, NO SE SI YA QUEDO


public class Conjuntos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Set<Double> conjunto1 = leerConjunto(scanner, "primer");
        Set<Double> conjunto2 = leerConjunto(scanner, "segundo");

      
          System.out.println("Elija una operacion: ");
          System.out.println("1. Union");
          System.out.println("2. Interseccion");
          System.out.println("3. Diferencia");
          System.out.println("4. Diferencia Simetrica");
          
          
        int opcion = scanner.nextInt();

        Set<Double> resultado = new HashSet<>();
        switch (opcion) {
            case 1:
                resultado.addAll(conjunto1);
                resultado.addAll(conjunto2);
                break;
            case 2:
                  resultado.addAll(conjunto1);
                resultado.retainAll(conjunto2);
                break;
            case 3:
                resultado.addAll(conjunto1);
                resultado.removeAll(conjunto2);
                break;
            case 4:
                Set<Double> temp1 = new HashSet<>(conjunto1);
                Set<Double> temp2 = new HashSet<>(conjunto2);
                temp1.removeAll(conjunto2);
                temp2.removeAll(conjunto1);
                resultado.addAll(temp1);
                resultado.addAll(temp2);
                break;
            default:
                System.out.println("Opcion invalida");
                return;
        }

       
        System.out.println("Conjunto resultante: " + resultado);
        System.out.println("Cardinalidad del conjunto resultante: " + resultado.size());

        scanner.close();
    }

    public static Set<Double> leerConjunto(Scanner scanner, String ordinal) {
        Set<Double> conjunto = new HashSet<>();

        System.out.println("Ingrese la cantidad de numeros en el " + ordinal + " conjunto: ");
        int cantidad = scanner.nextInt();

        System.out.println("Ingrese los numeros en el " + ordinal + " conjunto: ");
        for (int i = 0; i < cantidad; i++) {
            conjunto.add(scanner.nextDouble());
        }

        return conjunto;
    }
}