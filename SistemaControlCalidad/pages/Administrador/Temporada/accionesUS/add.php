<?php
	
	$temporada= $_POST['temporada'];
	$temporada = str_replace(" ", "-", $temporada);

	$command = "python ../../../../../ControlDeCalidad/Modules/CCPlanillas/handlerTemporada.py 3 ".$temporada;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Temporada.php");
?>
