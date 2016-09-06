<?php
	
	$idDefecto = $_GET['idDefecto'];
	$cantidad = $_POST['cantidad'];
	$idPlanilla = $_GET['idPlanilla'];
	$idControl = $_GET['control'];
	
	#hacemos la edicion...
	#obtener la informacion asociada a la planilla
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerControlCalidad.py 5 ".$idDefecto." ".$cantidad." ".$idControl;
	$informacion = array();
	echo $command;
	exec($command, $informacion);
	
	#debo devolverme al completar.php
	$send = "Location: completar.php?idPlanilla=".$idPlanilla."&insert=1";
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header($send);
?>
