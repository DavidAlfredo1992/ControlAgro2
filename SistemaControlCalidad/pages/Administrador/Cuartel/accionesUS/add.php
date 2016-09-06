<?php
	
	$nameCuartel = $_POST['nameCuartel'];
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
	
	$command = "python ../../../../../ControlDeCalidad/Modules/CCampos/handlerCuartel.py 5 ".$nameCuartel." ".$nameSector." ".$ListaVariedades;
	echo $command;
	$output = array();
	
	exec($command, $output);
	
	// Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Cuartel.php");
?>
