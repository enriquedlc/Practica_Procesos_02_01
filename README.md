# Práctica Procesos 02 Ejercicio 01

Se ha desarrollado un programa genera la cantidad de procesos hijos que introduzca el usuario. Cada proceso hijo debe mostrar su identificador de proceso y el de su padre. El proceso padre debe esperar a que terminen todos los procesos hijos antes de finalizar.

Se ha usado la función `fork()` para crear los procesos hijos, y la función `sleep()` para que el proceso padre espere a que terminen los procesos hijos (se ha usado un tiempo de espera de 5 segundos en el argumento de la funcion).

En la función createSonProcess() se ha usado `getpid()` para obtener el identificador del proceso hijo y el identificador del proceso padre. Le pasamos por pareámetro *numberOfChildProcesses* el número de hijos que queremos crear indicado por el usuario.
