<?php
	
	$idPlanilla= $_GET['idPlanilla'];
	#hacemos la insercion en la planilla y en los defectos para la planilla
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerPlanilla.py 11 ".$idPlanilla;
	#echo $command;
	$defectos = array();
	exec($command, $defectos);
	$numberDefectos = count($defectos);
	
	for ($i=1; $i<=$numberDefectos; $i++){
		
		$dato = "data".$i;
		echo $dato."<br>";
		echo "Imprimiendo la wea de prueba XD ".$_POST[''.$dato.''];
		echo "<br>";
	}
?>
