<?php
	
	$nameUser= $_POST['nameUser'];
	$nameUser = str_replace(" ", "-", $nameUser);
	$campo = $_POST['campo'];
	$campo = str_replace(" ", "-", $campo);	$empresa = $_POST['empresa'];
	$phone = $_POST['phone'];
	$correo = $_POST['correo'];
	
	$command = "python ../../../../../ControlDeCalidad/Modules/CCUsers/handlerJefeCampo.py 3 ".$phone." ".$empresa." ".$nameUser." ".$campo. " ".$correo;
	#echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../jefeCampo.php");
?>
