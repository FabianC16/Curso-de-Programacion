<?php



$numero1 = 10;
$numero2 = 15;

echo "Suma: " . ($numero1 + $numero2) . "\n";          
echo "Resta: " . ($numero1 - $numero2) . "\n";         
echo "Multiplicación: " . ($numero1 * $numero2) . "\n"; 
echo "División: " . ($numero1 / $numero2) . "\n";       
echo "Módulo: " . ($numero1 % $numero2) . "\n\n";         


$metododepago = "efectivo";

switch ($metodoDePago) {
    case "tarjeta":
        echo "Pago con tarjeta de débito/crédito seleccionado. Inserta o desliza la tarjeta.\n";
        break; 

    case "efectivo":
        echo "Pago en efectivo seleccionado. Prepara el monto exacto.\n";
        break;

    case "transferencia":
        echo "Pago por transferencia seleccionado. Muestra el comprobante.\n";
        break;
        
    default:
        echo "Método de pago no válido o no seleccionado.\n";
        break;
}


?>