<?php

	echo "variable recibida ".$_GET['idArray']."<br>";
	
	#get all information for complet data table
	#get number of user in data bases
	$command = "python ../../../../../ControlDeCalidad/Modules/CCPlanillas/handlerImportancia.py 1";
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	$numberUser = count($outputArray);
	
	$arrayInformation = explode(";", $outputArray[$_GET['idArray']-1]);#se obtiene nombre de usuario, correo y tipo
	$oldImportancia = str_replace(" ", "-", $arrayInformation[0]);
	
	#obtener nueva informacion
	$importancia= $_POST['importancia'];
	$importancia = str_replace(" ", "-", $importancia);
	
	$command = "python ../../../../../ControlDeCalidad/Modules/CCPlanillas/handlerImportancia.py 4 ".$oldImportancia." ".$importancia;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Importancia.php");
	
?>
