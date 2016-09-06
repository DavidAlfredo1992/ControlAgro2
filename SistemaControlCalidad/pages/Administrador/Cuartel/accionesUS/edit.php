<?php

	echo "variable recibida ".$_GET['idArray']."<br>";
	
	#get all information for complet data table
	#get number of user in data bases
	$command = "python ../../../../../ControlDeCalidad/Modules/CCampos/handlerCuartel.py 1";
	$outputArray = array();
	exec($command, $outputArray);#ejecucion del comando
	$numberUser = count($outputArray);
	
	$arrayInformation = explode(";", $outputArray[$_GET['idArray']-1]);#se obtiene nombre de usuario, correo y tipo
	$oldCuartel = str_replace(" ", "-", $arrayInformation[0]);
	$oldSector = str_replace(" ", "-", $arrayInformation[1]);
	$oldHuerto = str_replace(" ", "-", $arrayInformation[2]);
	$oldCampo = str_replace(" ", "-", $arrayInformation[3]);
	
	$nameCuartel = $_POST['cuartel'];
	$nameCuartel = str_replace(" ", "-", $nameCuartel);
	$nameSector= $_POST['sector'];
	$nameSector = str_replace(" ", "-", $nameSector);
	$variedades = $_POST['variedad'];
	$ListaVariedades = "";
	
	for ($i=0; $i<count($variedades); $i++){
		
		if ($i == count($variedades)-1){
			
			$ListaVariedades=$ListaVariedades.$variedades[$i];
		}else{
			
			$ListaVariedades=$ListaVariedades.$variedades[$i].":";
		}
	}
	
	echo $ListaVariedades;
	$ListaVariedades = str_replace(" ", "-", $ListaVariedades);
	
	$command = "python ../../../../../ControlDeCalidad/Modules/CCampos/handlerCuartel.py 6 ".$oldCuartel." ".$oldSector." ".$oldHuerto." ".$oldCampo." ".$nameCuartel." ".$nameSector." ".$ListaVariedades;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Cuartel.php");
	
?>
