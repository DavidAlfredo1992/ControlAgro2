<?php
	
	$importancia= $_POST['importancia'];
	$importancia = str_replace(" ", "-", $importancia);

	$command = "python ../../../../../ControlDeCalidad/Modules/CCPlanillas/handlerImportancia.py 3 ".$importancia;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Importancia.php");
?>
