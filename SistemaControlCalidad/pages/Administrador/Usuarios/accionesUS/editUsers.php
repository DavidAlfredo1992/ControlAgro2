<?php

	echo "variable recibida ".$_GET['idArray']."<br>";
	
	#get all information for complet data table
	#get number of user in data bases
	$command = "python ../../../../../ControlDeCalidad/Modules/CCUsers/manageUser.py 1";
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	$numberUser = count($outputArray);
	
	$arrayInformation = explode(";", $outputArray[$_GET['idArray']-1]);#se obtiene nombre de usuario, correo y tipo
	
	#obtener nueva informacion
	$nameUser= $_POST['nameUser'];
	$nameUser = str_replace(' ', '-', $nameUser);
	$email = $_POST['email'];
	$passworod = $_POST['pass'];
	$tipo = $_POST['tipo'];

	$oldUser = str_replace(' ', '-', $arrayInformation[0]);
	$command = "python ../../../../../ControlDeCalidad/Modules/CCUsers/manageUser.py 4 ".$oldUser." ".$arrayInformation[1]." ".$arrayInformation[2]." ".$nameUser." ".$email." ".$passworod;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../usersSystem.php");
	
?>
