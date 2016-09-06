<?php
	
	$nameVariedad= $_POST['nameVariedad'];
	$nameVariedad = str_replace(" ", "-", $nameVariedad);
	

	$command = "python ../../../../../ControlDeCalidad/Modules/CCampos/handlerVariedad.py 3 ".$nameVariedad;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Variedad.php");
?>
