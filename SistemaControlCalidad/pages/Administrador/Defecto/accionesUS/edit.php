<?php

	echo "variable recibida ".$_GET['idArray']."<br>";
	
	#get all information for complet data table
	#get number of user in data bases
	$command = "python ../../../../../ControlDeCalidad/Modules/CCPlanillas/handlerDefectos.py 1";
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	$numberUser = count($outputArray);
	
	$arrayInformation = explode(";", $outputArray[$_GET['idArray']-1]);#se obtiene nombre de usuario, correo y tipo
	$oldDefecto = str_replace(" ", "-", $arrayInformation[0]);
	
	#obtener nueva informacion
	$defecto= $_POST['defecto'];
	$defecto = str_replace(" ", "-", $defecto);
	$command = "python ../../../../../ControlDeCalidad/Modules/CCPlanillas/handlerDefectos.py 4 ".$oldDefecto." ".$defecto;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Defecto.php");
	
?>
