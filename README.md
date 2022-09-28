# Acertijo-100-prisioneros
Resolución del acertijo 100 prisioneros a traves de metodos numericos

El acertijo consiste en que cada uno de 100 prisioneros debe encontrar su número en uno de los 100 cajones para sobrevivir y si alguno no lo encuentra, todos morirán; y, cada prisionero puede abrir sólo 50 cajones y no puede comunicarse con los demás prisioneros, excepto en el debate previo de la estrategia. (extraido de Wikipedia)

En el programa uso 3 funciones:

llenarCajas() Consiste en una funcion que llena una lista con números aleatorios que no se repiten entre sí hasta que la lista tenga un largo de 100. Para ello primero asigno un numero aleatorio a la variable "num", luego recorro la lista para saber si ese numero ya se encuentra (linea 7). Si no lo encuentra, lo agrego.

buscarNumero(): Es la funcion en la que cada prisionero entra al cuarto a buscar su número, leyendo el valor que contiene la lista en la posición de su numero. Si no tiene su numero se fija en la posición de la lista cajas que encontró, hasta un máximo de 50 veces. Si no encuentra el número despues de 50 iteraciones, retorna false, caso contrario retorna true.

lograronSalir(): Esta funcion contempla la llamada a la función buscarNumero() 100 veces (una por cada prisionero). Si algún prisionero no logró encontrar su número, el ciclo se rompe retornando un false. Caso contrario, si todos los prisioneros encontraron su número, retorna true.

por último itero 100 veces la busqueda de los prisioneros, contando la cantidad de veces que lograron salir y mostrando en la pantalla. Para eso en cada iteración lleno las cajas, y luego en una sentencia if llamo a la funcion lograronSalir(). Siempre que se cumpla la condición (es decir, que lograronSalir() retorne true) sumo 1 al contador. Luego de 100 veces muestro el contador en la consola, sorprendentemente acercandose siempre a 32
