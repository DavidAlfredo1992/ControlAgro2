<?php

	echo "variable recibida ".$_GET['idArray']."<br>";
	
	#get all information for complet data table
	#get number of user in data bases
	$command = "python ../../../../../ControlDeCalidad/Modules/CCampos/handlerHuerto.py 1";
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	$numberUser = count($outputArray);
	
	$arrayInformation = explode(";", $outputArray[$_GET['idArray']-1]);#se obtiene nombre de usuario, correo y tipo
	
	$oldHuerto = str_replace(" ", "-", $arrayInformation[0]);
	$oldCampo = str_replace(" ", "-", $arrayInformation[1]);
	
	#obtener nueva informacion
	$nameHuerto= $_POST['nameCampo'];
	$nameHuerto = str_replace(" ", "-", $nameHuerto);
	$campo = $_POST['campo'];
	$campo = str_replace(" ", "-", $campo);
	
	$command = "python ../../../../../ControlDeCalidad/Modules/CCampos/handlerHuerto.py 4 ".$oldHuerto." ".$oldCampo. " ".$nameHuerto." ".$campo;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Huerto.php");
	
?>
