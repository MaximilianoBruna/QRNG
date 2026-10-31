# QRNG
QRNG code for the project of the course: Introduction to quantum computing.

Im lazy so I will update the repo later, for now everything is unorganized but this is important:

## QRNG_Test2.py
This one works, QRNG1 is just a test to make sure that qiskit and the aer_sim work

## ShanonEntr

Entrega dos cosas: 
  La entropía de Shannon: mide la incertidumbre promedio de la fuente.
  min_entr: mide la incertidumbre en el peor caso, es decir, qué tan difícil es adivinar el símbolo más probable.

Para un bit perfectamente aleatorio (p0 = p1 = 0,5), ambas valen 1 bit por bit. Esto aclara la confusión del paper: una min-entropía de 0,0007 sería catastrófica, y lo esperable es un valor cercano a 1.

Luego está la parte de correlación:

El concepto: mide si un bit depende de los bits anteriores. Se compara la secuencia consigo misma desplazada d posiciones. En una secuencia aleatoria, la autocorrelación debe estar cerca de 0 para todos los desfases. Es la fórmula del paper, AC = |A − D| / N, donde A es el número de posiciones iguales y D el de distintas.

los valores deberían oscilar alrededor de 0 con magnitud de unos 0,0008, y casi todos dentro de las líneas rojas. Que 2 o 3 lags de 1024 se salgan es normal, porque con un umbral de 3σ cabe esperar cerca del 0,3 % por azar. Lo preocupante sería una barra grande y repetida, o muchos lags fuera.


Ahora, van a ver que los resultados son buenos siempre porque estamos usando un simulador que internamente genera números con un algoritmo pseudoaleatorio de buena calidad. Estas pruebas no distinguen aleatoriedad cuántica de pseudoaleatoriedad bien hecha, y de hecho ninguna prueba estadística puede hacerlo a partir de los datos solamente. (ideal ver si es posible hacer todo esto en un IBM, pero eso si alcanza el tempo no más)

Por eso lo siguiente que quiero hacer es las pruebas NIST (SP 800-22 y SP 800-90B)

Eso, pónganse a chambear viendo cómo hacer informe de esto
