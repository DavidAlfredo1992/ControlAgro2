<?php
	
	$nameUser= $_POST['nameUser'];
	$nameUser = str_replace(" ", "-", $nameUser);
	$empresa = $_POST['empresa'];
	$phone = $_POST['phone'];
	$correo = $_POST['email'];
	
	$command = "python ../../../../../ControlDeCalidad/Modules/CCUsers/handlerJefeCuadrilla.py 3 ".$phone." ".$empresa." ".$nameUser." ".$correo;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../jefeCuadrilla.php");
?>
