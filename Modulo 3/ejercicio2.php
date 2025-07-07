<?php


$metododepago = "efectivo";

switch ($metododepago) {
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