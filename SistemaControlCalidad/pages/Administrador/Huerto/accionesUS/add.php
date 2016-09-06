<?php
	
	$nameCampo= $_POST['nameCampo'];
	$nameCampo = str_replace(" ", "-", $nameCampo);
	$campo = $_POST['campo'];
	$campo = str_replace(" ", "-", $campo);
	
	$command = "python ../../../../../ControlDeCalidad/Modules/CCampos/handlerHuerto.py 3 ".$nameCampo." ".$campo;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Huerto.php");
?>
