<?php
  session_start();
 
  // Obtengo los datos cargados en el formulario de login.
  $email = $_POST['email'];
  $email = str_replace(" ", "-", $email);
  $password = $_POST['password'];
  
  //ejecutar el script asociado al modelo dispuestos para generar las solicitudes...
  $command = "python ../../../ControlDeCalidad/Modules/CCUsers/user.py ".$email." ".$password." 1";
  
  $output = array();#almacena la salida del comando

  exec($command, $output);#ejecucion del comando
	echo $output[0];

  if ($output[0] == 1){#administrador
    $_SESSION['email'] = $email;
    // Redirecciono al usuario a la página principal del sitio.
    header("HTTP/1.1 302 Moved Temporarily");
    header("Location: ../Administrador/index.php");
  }else{
	  
		if ($output[0] == 2){#digitador
			$_SESSION['email'] = $email;
			// Redirecciono al usuario a la página principal del sitio.
			header("HTTP/1.1 302 Moved Temporarily");
			header("Location: ../Digitador/index.php");
		}else{
			
			if ($output[0] == 3){#encargado...
				$_SESSION['email'] = $email;
				// Redirecciono al usuario a la página principal del sitio.
				header("HTTP/1.1 302 Moved Temporarily");
				header("Location: ../Encargado/index.php");
			}else{
				
				if ($output[0] == 4){#cliente
					
					#debemos obtener el id del campo al que pertence
					$command = "python ../../../ControlDeCalidad/Modules/CCUsers/manageUser.py 8 ".$email." ".$password;
					echo $command;					
					$campo = array();#almacena la salida del comando
					exec($command, $campo);#ejecucion del comando
					$_SESSION['email'] = $email;
					// Redirecciono al usuario a la página principal del sitio.
					$send = "Location: ../Cliente/Campo/index.php?idCampo=".$campo[0];
					header("HTTP/1.1 302 Moved Temporarily");
					header($send);
				}else{
					
					#echo '<script language="javascript">alert("juas");</script>';
					
					header("HTTP/1.1 302 Moved Temporarily");
					header("Location: login.html");
				}
			}
		}
	}


  // Esto se puede remplazar por un usuario real guardado en la base de datos.
  //if($email == 'user' && $password == 'user'){
    // Guardo en la sesión el email del usuario.
   // $_SESSION['email'] = $email;
     
    // Redirecciono al usuario a la página principal del sitio.
    //header("HTTP/1.1 302 Moved Temporarily");
    //header("Location: principal.php");
  //}else{
    //echo 'El email o password es incorrecto, <a href="login.php">vuelva a intenarlo</a>.<br/>';
  //}
?>
