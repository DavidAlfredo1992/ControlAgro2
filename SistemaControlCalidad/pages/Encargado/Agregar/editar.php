<?php

	#debemos obtener los sectores del huerto del campo seleccionado
	$campo = $_GET['campo'];
	$campo = str_replace(" ","-", $campo);
	$huerto = $_GET['huerto'];
	$huerto = str_replace(" ", "-", $huerto);
	$sector = $_GET['sector'];
	$sector = str_replace(" ", "-", $sector);
	$cuartel = $_GET['cuartel'];
	$cuartel = str_replace(" ", "-", $cuartel);
	$variedad = $_GET['variedad'];
	$variedad = str_replace(" ", "-", $variedad);
	$cuadrilla = $_GET['cuadrilla'];
	$cuadrilla = str_replace(" ", "-", $cuadrilla);
	$temporada = $_GET['temporada'];
	$temporada = str_replace(" ", "-", $temporada);
	$jefeCuadrilla = $_GET['jefeCuadrilla'];
	$jefeCuadrilla = str_replace(" ", "-", $jefeCuadrilla);
	$idPlanilla = $_GET['idPlanilla'];
	
	$defectosMayores = $_POST['mayores'];
	$defectosMenores = $_POST['menores'];
	
	#hacemos la edicion de los defectos solo con los defectos menores porque por defecto son mayores...
	for ($i=0; $i<count($defectosMenores); $i++){
	
		$defecto = str_replace(" ", "-", $defectosMenores[$i]);
		$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerPlanilla.py 13 ".$defecto. " MAYORES MENORES";
		echo $command;
		$importancias = array();
		exec($command, $importancias);#ejecucion del comando
	}
	
	$send = "Location: etapa10.php?campo=".$_GET['campo']."&huerto=".$_GET['huerto']."&sector=".$_GET['sector']."&cuartel=".$_GET['cuartel']."&variedad=".$_GET['variedad']."&jefeCuadrilla=".$_GET['jefeCuadrilla']."&cuadrilla=".$_GET['cuadrilla']."&temporada=".$_GET['temporada']."&idPlanilla=".$idPlanilla;
	header("HTTP/1.1 302 Moved Temporarily");
	header($send);
?>
