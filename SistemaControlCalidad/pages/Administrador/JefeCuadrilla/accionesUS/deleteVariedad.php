<?php
	
	$jefeCuadrilla = $_GET['jefe'];
	$jefeCuadrilla = str_replace(" ", "-", $jefeCuadrilla);
	$nameCampo = $_GET['campo'];
	$nameCampo = str_replace(" ", "-", $nameCampo);
	$nameHuerto = $_GET['huerto'];
	$nameHuerto = str_replace(" ", "-", $nameHuerto);
	$nameSector = $_GET['sector'];
	$nameSector = str_replace(" ", "-", $nameSector);
	$nameCuartel = $_GET['cuartel'];
	$nameCuartel = str_replace(" ", "-", $nameCuartel);
	$nameVariedad = $_GET['variedad'];
	$nameVariedad = str_replace(" ", "-", $nameVariedad);
	
	#execute the remove user...
	$command = "python ../../../../../ControlDeCalidad/Modules/CCUsers/handlerJefeCuadrilla.py 12 ".$jefeCuadrilla." ".$nameCampo." ".$nameHuerto." ".$nameSector." ".$nameCuartel." ".$nameVariedad;
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	echo $command;
	
	// Redirecciono al usuario a la página principal del sitio.
	header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../jefeCuadrilla.php");
?>

