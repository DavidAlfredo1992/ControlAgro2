<?php
	
	$cuadrilla= $_POST['cuadrilla'];
	$cuadrilla = str_replace(" ", "-", $cuadrilla);
	$jefeCuadrilla = $_POST['jefeCuadrilla'];
	$jefeCuadrilla = str_replace(" ", "-", $jefeCuadrilla);

	$command = "python ../../../../../ControlDeCalidad/Modules/CCCuadrillas/handlerCuadrillas.py 3 ".$cuadrilla." ".$jefeCuadrilla;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Cuadrilla.php");
?>
