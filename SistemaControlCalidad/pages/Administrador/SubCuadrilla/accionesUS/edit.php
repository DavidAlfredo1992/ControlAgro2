<?php

	echo "variable recibida ".$_GET['idArray']."<br>";
	
	#get all information for complet data table
	#get number of user in data bases
	$command = "python ../../../../../ControlDeCalidad/Modules/CCCuadrillas/handlerCuadrillas.py 1";
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	$numberUser = count($outputArray);
	
	$arrayInformation = explode(";", $outputArray[$_GET['idArray']-1]);#se obtiene nombre de usuario, correo y tipo
	
	#obtener nueva informacion
	$cuadrilla= $_POST['cuadrilla'];
	$jefeCuadrilla = $_POST['jefeCuadrilla'];

	$command = "python ../../../../../ControlDeCalidad/Modules/CCCuadrillas/handlerCuadrillas.py 4 ".$arrayInformation[0]." ".$arrayInformation[1]." ".$cuadrilla." ".$jefeCuadrilla;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Cuadrilla.php");
	
?>
