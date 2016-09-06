<?php

	echo "variable recibida ".$_GET['idArray']."<br>";
	
	#get all information for complet data table
	#get number of user in data bases
	$command = "python ../../../../../ControlDeCalidad/Modules/CCUsers/handlerJefeCuadrilla.py 1";
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	$numberUser = count($outputArray);
	
	$arrayInformation = explode(";", $outputArray[$_GET['idArray']-1]);#se obtiene nombre de usuario, correo y tipo
	$oldName = str_replace(" ", "-", $arrayInformation[0]);
	
	#obtener nueva informacion
	$nameUser= $_POST['nameUser'];
	$nameUser = str_replace(" ", "-", $nameUser);
	$correo = $_POST['email'];
	$empresa = $_POST['empresa'];
	$phone = $_POST['phone'];

	$command = "python ../../../../../ControlDeCalidad/Modules/CCUsers/handlerJefeCuadrilla.py 4 ".$oldName." ".$arrayInformation[1]." ".$arrayInformation[2]." ".$nameUser." ".$phone." ".$empresa." ".$correo;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../jefeCuadrilla.php");
	
?>
