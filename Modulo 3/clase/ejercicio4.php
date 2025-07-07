<?php

$suma = 0;

for ($i = 1; $i <= 100; $i++) {
    if ($i % 2 != 0) {
        $suma+= $i;
    } 
}

echo "la suma de todos los numeros impares del 1 al 100 es: $suma"
?>