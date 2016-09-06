<?php
	
	$idUser = $_GET['idUser'];
	
	$campo = $_POST['campo'];
	$campo = str_replace(" ", "-", $campo);
	$empresa = $_POST['empresa'];
	$telefono = $_POST['telefono'];
	
	$nameUser= $_POST['nameUser'];
	echo $nameUser."<br>";
	$nameUser = str_replace(' ', '-', $nameUser);
	echo $nameUser."<br>Sin espacios";
	
	$email = $_POST['email'];
	$passworod = $_POST['pass'];
	$tipo = $_POST['tipo'];

	$command = "python ../../../../../ControlDeCalidad/Modules/CCUsers/manageUser.py 7 ".$idUser." ".$campo." ".$empresa." ".$telefono;
	#echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
	header("HTTP/1.1 302 Moved Temporarily");
	header("Location: ../usersSystem.php");
?>
