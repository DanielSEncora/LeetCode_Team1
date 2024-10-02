import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args){
        int max = 0;
        int izq = 0;

        Set<Object> charSet = new HashSet<>();
        String secuencia = "pwwkew";

        for(char chars: secuencia.toCharArray()){
            charSet.add(chars);
        }


        System.out.println(charSet);

        /*
        max= 0
        izq=0
        recorrer el string
        loop si set tiene string[i]:

        Set delete string[izq]

        izq++

        max = el mayor de max o (i-izq+1)

        set add string[i]
                */

    }
}

        /*  TODO:
            Convertir string en arreglo de chars
            actual
            max

            String palabra = "tale"
            Set = [c]
            iterador = 3
            iteradorMax = 4

            "abcc"

            loop{
                si ! SET.has string[i]
                    agregar string[i]
                    iterador++
                else{
                    newString = palabra.substring() //eliminando caracter hasta izquierda
                    if iterador > iteradorMax
                        iteradorMax = iterador

                    i=0
                    iterador = 0

                }
            }

            return iteradorMax


        max= 0
        izq=0
        recorrer el string
            loop si set tiene string[i]:

                Set delete string[izq]

                izq++

            max = el mayor de max o (i-izq+1)

            set add string[i]

        */
