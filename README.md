### Documentación y Solución Del Problema Tiendita
El siguiente problema a solucionar es la implementacion de una factura, la cual almacenara los siguientes datos, "El Rol con cedula Numero, debe pagar Valor por el producto Codigo", donde el rol será bien sea estudiante o profesor. El usuario podrá realizar lo siguiente:
*  Digitar el numero de cedula
* Elegir su rol, bien sea profesor, estudiante y este ultimo con la opcion de becado o no.
* Posteriormente, si eligio estudiante se le preguntara si es becado, de no ser asi, el programa pasa a solicitar el respectivo producto, su codigo, precio y numero de unidades.

Con respecto al modelo computacional aplicado, se trata de la _**computacion algoritmica**_, esta consta de distintos algoritmos, o bien una secuencia de pasos para obtener un resultado en especifico, tal como se hace en este código.

Entrando mas en detalle acerca del codigo, especialmente de su desarrollo,tenemos que funciona por medio de ciclos, para hacer mas facil el recorrido de los datos y así sea conciso el proceso final. A continuacion encontrara un paso a paso del funcionamiento del codigo, superficialmente pero a la hora de probarlo, entendera por completo lo que se llevo a cabo.

En primer lugar, la consola solicita al usuario su cedula, necesaria para el print de la factura final. Seguido de esto, se pregunta el respectivo rol del usuario, bien sea profesor o estudiante becado o no becado,para poder clasificar y asignar el debido descuento.  

El siguiente paso, el cual puede presentar una incoherencia, es preguntarle al usuario si desea realizar un compra, si acepta, continua al proceso de asignar el producto, su codigo, precio y cantidad, de no ser asi, el ciclo termina y vuelve a preguntar por la celula, asi sucesivamente hasta que se ingrese la letra "o". En el apartado donde se llena el formulario para el producto, tenemos "codigo: NombreDelProducto Precio NumeroDeUnidades" donde al ingresar los datos correspondientes, arroja de inmediato el precio con el descuento ya aplicado, el rol, numero de identificacion y codigo del producto.   
   
La forma como se calcula todo este codigo, es por medio de listas y matrices, donde el unico procedimiento matematico seria el descuento por el producto, tan simple como: Si tenemos $5000, y buscamos tener el 50%, multiplicamos $5000 por 0.5, restamos ese valor al original $5000 y obtenemos el descuento aplicado.
Por ultimo, si el usuario desea agregar otro producto, basta con escribir "si", simulando como si fuera la caja de un supermercado, donde se ingresa item por item.
            
            
### REFERENCIAS

1. [Sintaxis Markdown usada para realizar el archivo readme del repositorio](https://markdown.es/sintaxis-markdown/): https://markdown.es/sintaxis-markdown/
2. [Nuevos Modelos Computacionales](https://www.computing.es/analytics/opinion/1118527046201/cuales-nuevos-modelos-de-computacion.1.html):
 https://www.computing.es/analytics/opinion/1118527046201/cuales-nuevos-modelos-de-computacion.1.html
