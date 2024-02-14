import java.lang.runtime.SwitchBootstraps;
import java.util.*;

class Taller2 {

    public static void main(str[] args) {

        Scanner scanner = new scanner(System.in);

        set<Int> ConUniversal = LeerConjunto(Scanner, "U");
        set<Int> ConA = LeerConjunto(Scanner, "A");

        boolean CompConjunt = ConUniversal.containsAll(ConA);

        if (CompConjunt) {

        } else {
            System.out.println("A no es subconjunto de U, terminando programa");
            return;
        }

        System.out.println(
                "Porfavor elija la operacion: " + "\n" + "1. (U u A) n A" + "\n" + "2. (U n A) ∆ A" + "3. (U - A) ∆ A");

        int opcion = scanner.nextInt();

        set<Int> resultado1 = new HashSet<>();
        set<Int> resultado2 = new HashSet<>();

        switch (opcion) {
            case 1:

                resultado1.addAll(ConUniversal);
                resultado1.addAll(ConA);

                resultado2.addAll(ConUniversal);
                resultado2.retainAll(ConA);

                System.out.println(resultado2);

                break;

            case 2:

                resultado1.addAll(ConUniversal);
                resultado1.retainAll(ConA);

                resultado1 = diferenciaSimetrica(resultado1, ConUniversal);
                System.out.println(resultado1);

                break;

            case 3:

                resultado1.addAll(ConUniversal);
                resultado1.removeAll(ConA);

                resultado1 = diferenciaSimetrica(resultado1, ConA);

                System.out.println(resultado1);

                break;
            default:
                break;
        }

    }

    public static Set<Int> LeerConjunto(Scanner scanner, String con) {

        set<Int> conjunto = new HashSet<>();

        System.out.println("Porfavor ingrese la cantidad de numeros en el" + con + "Conjunto: " + "\n" + "-");

        int cant = scanner.nextInt();

        System.out.println("Porfavor ingrese los numeros en el " + con + "Conjunto: " + "\n" + "-");
        for (int i = 0; i < cant; i++) {

            conjunto.add(scanner.nextInt());

        }

        return conjunto;

    }

    private Set<Int> diferenciaSimetrica(Set<Int> A, Set<Int> B) {

        set<Int> union = new HashSet<Int>();
        union.addAll(A);
        union.addAll(B);

        Set<Int> interseccion = new HashSet<Int>();
        interseccion.addAll(A);
        interseccion.addAll(B);

        Set<Int> resultado = new HashSet<Int>();
        resultado.addAll(union);
        resultado.removeAll(interseccion);

        return resultado;
    }

}