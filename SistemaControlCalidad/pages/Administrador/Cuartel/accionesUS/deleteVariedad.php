<?php
	
	
	$campo = $_GET['nombreCampo'];
	$campo = str_replace(" ", "-", $campo);
	
	#obtener el nombre de los defectos...
	#get all information for complet data table
	#get number of user in data bases
	$command = "python ../../../../../ControlDeCalidad/Modules/CCampos/handlerCuartel.py 9 ".$campo;
	echo $command."<br>";
	$output = array();
	exec($command, $output);#ejecucion del comando
	$numberUser = count($output);

	$arrayInformation = explode(";", $output[$_GET['variedad']-1]);#se obtiene nombre de usuario, correo y tipo
	
	$defecto = str_replace(" ", "-", $arrayInformation[0]);
	
	#execute the remove user...
	$command = "python ../../../../../ControlDeCalidad/Modules/CCampos/handlerCuartel.py 11 ".$campo." ".$defecto;
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	echo $command;
	
	// Redirecciono al usuario a la página principal del sitio.
	header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Cuartel.php");
?>

