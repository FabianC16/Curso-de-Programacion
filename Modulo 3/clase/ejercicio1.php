<?php

$pares = 0;
$impares = 0;

for ($i = 1; $i <= 50; $i++) {
    if ($i % 2 == 0) {
        echo "$i es par";
        $pares++;
    } else {
        echo "$i es impar";
        $impares++;
    }
}
echo "cantidad de numeros pares: $pares";
echo "cantidad de numeros impares $impares";
?>