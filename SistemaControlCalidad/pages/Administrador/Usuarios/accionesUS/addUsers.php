<?php
	
	$nameUser= $_POST['nameUser'];
	echo $nameUser."<br>";
	$nameUser = str_replace(' ', '-', $nameUser);
	echo $nameUser."<br>Sin espacios";
	
	$email = $_POST['email'];
	$passworod = $_POST['pass'];
	$tipo = $_POST['tipo'];

	$command = "python ../../../../../ControlDeCalidad/Modules/CCUsers/manageUser.py 3 ".$nameUser." ".$email." ".$passworod." ".$tipo;
	#echo $command;
	$output = array();
	
	exec($command, $output);
	
	if ($tipo == "Cliente"){
		
		$send = "Location: ../optionCliente.php?idUser=".$output[0];
		// Redirecciono al usuario a la página principal del sitio.
		header("HTTP/1.1 302 Moved Temporarily");
		header($send);
	}else{
		
		// Redirecciono al usuario a la página principal del sitio.
		header("HTTP/1.1 302 Moved Temporarily");
		header("Location: ../usersSystem.php");
	}
?>
