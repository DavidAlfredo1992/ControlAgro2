<?php
	
	#obtengo la informacion del usuario seleccionado...
	$command = "python ../../../../ControlDeCalidad/Modules/CCampos/handlerCuartel.py 1";
	echo $command;
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	
	$arrayInformation = explode(";", $outputArray[$_GET['idArray']-1]);#se obtiene nombre de usuario, correo y tipo
	$nameCuartel = str_replace(" ", "-", $arrayInformation[0]);
	$nameSector = str_replace(" ", "-", $arrayInformation[1]);
	$nameHuerto = str_replace(" ", "-", $arrayInformation[2]);
	$nameCampo = str_replace(" ", "-", $arrayInformation[3]);
	
	#execute the remove user...
	$command = "python ../../../../ControlDeCalidad/Modules/CCampos/handlerCuartel.py 7 ".$nameCuartel." ".$nameSector." ".$nameHuerto." ".$nameCampo;
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	echo $command;
	
	// Redirecciono al usuario a la página principal del sitio.
	header("HTTP/1.1 302 Moved Temporarily");
    header("Location: Cuartel.php");
?>
