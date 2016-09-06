<?php

	echo "variable recibida ".$_GET['idArray']."<br>";
	
	#get all information for complet data table
	#get number of user in data bases
	$command = "python ../../../../../ControlDeCalidad/Modules/CCUsers/handlerJefeCampo.py 1";
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	$numberUser = count($outputArray);
	
	$arrayInformation = explode(";", $outputArray[$_GET['idArray']-1]);#se obtiene nombre de usuario, correo y tipo
	
	#obtener nueva informacion
	$nameUser= $_POST['nameUser'];
	$nameUser = str_replace(" ", "-", $nameUser);
	$campo = $_POST['campo'];
	$campo = str_replace(" ", "-", $campo);
	$empresa = $_POST['empresa'];
	$phone = $_POST['phone'];
	$correo = $_POST['correo'];
	
	$oldjefe = str_replace(" ", "-", $arrayInformation[0]);
	$oldcampo = str_replace(" ", "-", $arrayInformation[1]);
	
	$command = "python ../../../../../ControlDeCalidad/Modules/CCUsers/handlerJefeCampo.py 4 ".$oldjefe." ".$oldcampo." ".$arrayInformation[2]." ".$arrayInformation[3]." ".$nameUser." ".$campo." ".$phone." ".$empresa." ".$correo;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../jefeCampo.php");
	
?>
