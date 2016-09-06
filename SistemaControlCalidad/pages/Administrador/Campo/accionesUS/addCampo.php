<?php
	
	$nameCampo= $_POST['nameCampo'];
	$nameCampo = str_replace(" ", "-", $nameCampo);
	$defectos = $_POST['defectos'];
	$ListaDefectos = "";
	
	for ($i=0; $i<count($defectos); $i++){
		
		if ($i == count($defectos)-1){
			
			$ListaDefectos=$ListaDefectos.$defectos[$i];
		}else{
			
			$ListaDefectos=$ListaDefectos.$defectos[$i].":";
		}
	}

	$ListaDefectos = str_replace(" ", "-", $ListaDefectos);
	
	$command = "python ../../../../../ControlDeCalidad/Modules/CCampos/handlerCampo.py 3 ".$nameCampo." ".$ListaDefectos;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Campo.php");
?>
