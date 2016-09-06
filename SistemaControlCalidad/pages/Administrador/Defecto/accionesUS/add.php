<?php
	
	$defecto= $_POST['defecto'];
	$defecto = str_replace(" ", "-", $defecto);

	$command = "python ../../../../../ControlDeCalidad/Modules/CCPlanillas/handlerDefectos.py 3 ".$defecto;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Defecto.php");
?>
