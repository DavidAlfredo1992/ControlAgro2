<?php
	
	$nameSector= $_POST['nameSector'];
	$nameSector = str_replace(" ", "-", $nameSector);
	$nameHuerto = $_POST['huerto'];
	$nameHuerto = str_replace(" ", "-", $nameHuerto);
	
	$command = "python ../../../../../ControlDeCalidad/Modules/CCampos/handlerSector.py 4 ".$nameSector." ".$nameHuerto;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Sector.php");
?>
