<?php
	
	$jefeCuadrilla = $_GET['jefe'];
	$jefeCuadrilla = str_replace(" ", "-", $jefeCuadrilla);
	$nameCampo = $_POST['campo'];
	$nameCampo = str_replace(" ", "-", $nameCampo);
	$nameHuerto = $_POST['huerto'];
	$nameHuerto = str_replace(" ", "-", $nameHuerto);
	$nameSector = $_POST['sector'];
	$nameSector = str_replace(" ", "-", $nameSector);
	$nameCuartel = $_POST['cuartel'];
	$nameCuartel = str_replace(" ", "-", $nameCuartel);
	$nameVariedad = $_POST['variedad'];
	$nameVariedad = str_replace(" ", "-", $nameVariedad);
	
	$command = "python ../../../../../ControlDeCalidad/Modules/CCUsers/handlerJefeCuadrilla.py 11 ".$jefeCuadrilla." ".$nameCampo." ".$nameHuerto." ".$nameSector." ".$nameCuartel." ".$nameVariedad;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../jefeCuadrilla.php");

?>

