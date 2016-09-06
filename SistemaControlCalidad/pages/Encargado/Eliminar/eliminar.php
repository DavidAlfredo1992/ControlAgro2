<?php

	$idPlanilla = $_GET['idPlanilla'];
	
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerPlanilla.py 18 ".$idPlanilla;
	echo $command;
	$defectos = array();
	exec($command, $defectos);
	
	header("HTTP/1.1 302 Moved Temporarily");
    header("Location: EliminarPlantillas.php");
?>
