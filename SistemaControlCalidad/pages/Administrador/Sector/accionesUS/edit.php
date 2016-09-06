<?php

	echo "variable recibida ".$_GET['idArray']."<br>";
	
	#get all information for complet data table
	#get number of user in data bases
	$command = "python ../../../../../ControlDeCalidad/Modules/CCampos/handlerSector.py 1";
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	$numberUser = count($outputArray);
	
	$arrayInformation = explode(";", $outputArray[$_GET['idArray']-1]);#se obtiene nombre de usuario, correo y tipo
	
	$oldSector = str_replace(" ", "-", $arrayInformation[0]);
	$oldHuerto = str_replace(" ", "-", $arrayInformation[1]);
	$oldCampo = str_replace(" ", "-", $arrayInformation[2]);
	
	#obtener nueva informacion
	$nameSector = $_POST['nameSector'];
	$nameSector = str_replace(" ", "-", $nameSector);
	$nameHuerto= $_POST['nameHuerto'];
	$nameHuerto = str_replace(" ", "-", $nameHuerto);
	
	$command = "python ../../../../../ControlDeCalidad/Modules/CCampos/handlerSector.py 5 ".$oldSector." ".$oldHuerto." ".$oldCampo." ".$nameSector." ".$nameHuerto;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Sector.php");
	
?>
