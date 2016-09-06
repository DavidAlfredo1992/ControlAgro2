<?php
	
	#obtenemos el id del control efectuado
	$idControlCalidad = $_GET['idControl'];
	$idPlanilla = $_GET['idPlanilla'];
	
	#obtener la informacion asociada a la planilla
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerControlCalidad.py 6 ".$idPlanilla." ".$idControlCalidad;
	$informacion = array();
	echo $command;
	#exec($command, $informacion);
	$resumenPlanilla = explode(";", $informacion[0]);

	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    $send = "Location: resumenPlanilla.php?idPlanilla=".$idPlanilla."&idControl=".$idControlCalidad;
    header($send);
?>
