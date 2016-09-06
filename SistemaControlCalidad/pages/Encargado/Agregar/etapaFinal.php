<?php

	#recolectamos el id de la planilla
	$idPlanilla = $_GET['idPlanilla'];

	#recolectamos los rangos mayores
	$mayor1 = $_POST['mayor1'];
	$mayor2 = $_POST['mayor2'];
	$mayor3 = $_POST['mayor3'];
	$menor1 = $_POST['menor1'];
	$menor2 = $_POST['menor2'];
	$menor3 = $_POST['menor3'];

	#hacemos la insercion en la planilla y en los defectos para la planilla
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerPlanilla.py 14 ".$idPlanilla." ".$mayor1." ".$mayor2." ".$mayor3." ".$menor1." ".$menor2." ".$menor3;
	echo $command;
	#$defectos = array();
	exec($command, $defectos);
	
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../index.php");

?>
