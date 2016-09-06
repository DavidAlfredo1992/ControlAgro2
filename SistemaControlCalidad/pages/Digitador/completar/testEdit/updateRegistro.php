<?php
	
	 $file = fopen("archivo.txt", "w");
	
	$information = $_GET;
	fwrite($file, "Esto es una nueva linea de texto" . PHP_EOL);

	fwrite($file, "Otra más" . PHP_EOL);
	fwrite($file, count($information));
	fclose($file);
?>


