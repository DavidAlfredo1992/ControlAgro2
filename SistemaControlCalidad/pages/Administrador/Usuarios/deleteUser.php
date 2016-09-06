<?php
	
	#obtengo la informacion del usuario seleccionado...
	$command = "python ../../../../ControlDeCalidad/Modules/CCUsers/manageUser.py 1";
	#echo $command;
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	
	$arrayInformation = explode(";", $outputArray[$_GET['idArray']-1]);#se obtiene nombre de usuario, correo y tipo
	#echo "variable de mierda: ".$_GET['idArray'];
	#print_r($arrayInformation);
	#execute the remove user...
	echo $arrayInformation[0]."<br>";
	$oldUser = str_replace(' ', '-', $arrayInformation[0]);
	$command = "python ../../../../ControlDeCalidad/Modules/CCUsers/manageUser.py 5 ".$oldUser." ".$arrayInformation[1]." ".$arrayInformation[2];
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	echo $command;
	
	// Redirecciono al usuario a la página principal del sitio.
	header("HTTP/1.1 302 Moved Temporarily");
    header("Location: usersSystem.php");
?>
