<?php

	echo "variable recibida ".$_GET['idArray']."<br>";
	
	#get all information for complet data table
	#get number of user in data bases
	$command = "python ../../../../../ControlDeCalidad/Modules/CCCuadrillas/handlerCuadrillas.py 1";
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	$numberUser = count($outputArray);
	
	$arrayInformation = explode(";", $outputArray[$_GET['idArray']-1]);#se obtiene nombre de usuario, correo y tipo
	
	$oldCuadrilla = str_replace(" ", "-", $arrayInformation[0]);
	$oldJefe = str_replace(" ", "-", $arrayInformation[1]);
	
	#obtener nueva informacion
	$cuadrilla= $_POST['cuadrilla'];
	$cuadrilla = str_replace(" ", "-", $cuadrilla);
	$jefeCuadrilla = $_POST['jefeCuadrilla'];
	$jefeCuadrilla = str_replace(" ", "-", $jefeCuadrilla);

	$command = "python ../../../../../ControlDeCalidad/Modules/CCCuadrillas/handlerCuadrillas.py 4 ".$oldCuadrilla." ".$oldJefe." ".$cuadrilla." ".$jefeCuadrilla;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Cuadrilla.php");
	
?>
