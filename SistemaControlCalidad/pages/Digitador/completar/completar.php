<?php
	
	#obtener informacion de formulario
	$nameSesion = $_POST['digitador'];
	$nameSesion = str_replace(" ", "-", $nameSesion);
	$idPlanilla = $_GET['idPlanilla'];
	$tamano = $_POST['muestras'];
	$insert=$_GET['insert'];
	
	#obtener la informacion asociada a la planilla
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerPlanilla.py 17 ".$idPlanilla;
	$informacion = array();
	#print $command;
	exec($command, $informacion);
	$resumenPlanilla = explode(";", $informacion[0]);
	$varClass1 = "<tr class=\"gradeU\">";
	
	// Día del mes con 2 dígitos, y con ceros iniciales, de 01 a 31
	$dia= date("d");

	// Mes actual en 2 dígitos y con 0 en caso del 1 al 9, de 1 a 12
	$mes = date("m");
	$ano = date("Y");	
	
	$fecha = $dia."-".$mes."-".$ano;
	
	if ($insert == 0){
		#hacer la insercion en la tabla 
		$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerControlCalidad.py 2 ".$idPlanilla." ".$nameSesion." ".$fecha." ".$tamano;
		$defectos = array();
		exec($command, $defectos);
		$numberDefectos = count($defectos);
		#echo $command;
	}
	
	#obtenemos el id del control de calidad que se esta efectuando...
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerControlCalidad.py 3";
	$conteo = array();
	exec($command, $conteo);
	$idControlCalidad=$conteo[0];
	
	if ($insert != 0){#debo obtener la informacion de la tabla final...
		$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerControlCalidad.py 4 ".$idControlCalidad;
		$defectos = array();
		exec($command, $defectos);
		$numberDefectos = count($defectos);
		
	}
?>

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Sistema de Control de Calidad</title>

	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.5/css/bootstrap.min.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
	
    <!-- Bootstrap Core CSS -->
    <link href="../../../bower_components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- MetisMenu CSS -->
    <link href="../../../bower_components/metisMenu/dist/metisMenu.min.css" rel="stylesheet">

    <!-- Timeline CSS -->
    <link href="../../../dist/css/timeline.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="../../../dist/css/sb-admin-2.css" rel="stylesheet">

    <!-- Morris Charts CSS -->
    <link href="../../../bower_components/morrisjs/morris.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="../../../bower_components/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
	
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>

<body>

    <div id="wrapper">

        <!-- Navigation -->
                <nav class="navbar navbar-default navbar-static-top" role="navigation" style="margin-bottom: 0">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="../index.php">Sistema de Control de Calidad</a>
            </div>
            <!-- /.navbar-header -->

            <!-- /.navbar-static-side -->
         <div class="navbar-default sidebar" role="navigation">
                <div class="sidebar-nav navbar-collapse">
                    <ul class="nav" id="side-menu">
                        <li class="sidebar-search">
                            <div class="input-group custom-search-form">
                                <input type="text" class="form-control" placeholder="Buscar...">
                                <span class="input-group-btn">
                                <button class="btn btn-default" type="button">
                                    <i class="fa fa-search"></i>
                                </button>
                            </span>
                            </div>
                            <!-- /input-group -->
                        </li>
                         <li>
                            <a href="../LoginSystem/login.html"><i class="fa fa-fw fa-fw fa-5x fa-user fa-fw"></i>Cerrar Sesión</a>
                            
                        </li>
                        <li>
                            <a href="../index.php"><i class="fa fa-fw fa-fw fa-5x fa-home fa-fw"></i>Menú Principal</a>
                            
                        </li>
                    </ul>
                </div>
                <!-- /.sidebar-collapse -->
            </div>
            <!-- /.navbar-static-side -->
        </nav>
				<div id="page-wrapper">
            <div class="row">
                <div class="col-lg-12">
                    <h1 class="page-header">Administración de Plantillas</h1>
                </div>
                <!-- /.col-lg-12 -->
            </div>
            <!-- /.row -->            			
 
            <div class="row">
                <div class="col-lg-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Completa la Nómina agregando la cantidad encontrada
                        </div>
						<div class="panel-body">
                            <div class="row">
                                <div class="col-lg-6">
									
									<!--Agregamos una tabla resumen con la informacion recolectada en la etapa 1-->
									<div class="panel-body">
                            <div class="dataTable_wrapper">
                                <table width="100%" class="table striped table-bordered table-hover" id="actual">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Defecto</th>
                                            <th># Observado</th> 
                                            <th>Edit</th>                                                                                       
                                        </tr>
									</thead>
									<tbody>
										
										<?php
											for ($i=1; $i<=$numberDefectos; $i++){
												echo $varClass1;
												$columnas = explode(";", $defectos[$i-1]);
												echo "<td>".$i."</td>";
												echo "<td>".$columnas[1]."</td>";
												echo "<td>".$columnas[2]."</td>";
												echo "<td>
													<a href=\"editar.php?idPlanilla=".$idPlanilla."&nameDefecto=".$columnas[1]."&idDefecto=".$columnas[0]."&control=".$idControlCalidad."\" class=\"btn btn-warning btn-circle\"><i class=\"fa fa-fw fa-pencil \"></i></a>";
												echo "</tr>";
											}
										?>
                                    </tbody>
                                </table>
                                                                
                            </div>
                            <!-- /.table-responsive -->                                    
                        </div>
                        <!-- /.panel-body -->
                    </div>
                <!-- /.col-lg-12 -->
                                     <div class="row">
                <div class="col-lg-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                           Pulse Finlizar proceso para calcular la nota del control efectuado.
                        </div>
						<div class="panel-body">
                            <div class="row">
                                <div class="col-lg-6">
									
									<?php
										echo "<form role=\"form\" method=\"POST\" action=\"completarProceso.php?idPlanilla=".$idPlanilla."&idControl=".$idControlCalidad."\">";
									?>
										
                                        
                                        <button type="submit" class="btn btn-primary">Finalizar proceso</button>
                                        
                                    </form>
                            <!-- /.table-responsive -->                                    
                        </div>
                        <!-- /.panel-body -->
                        </div>
                    <!-- /.panel -->
                    <!-- /.panel -->
                </div>
            </div>
        </div>
        <!-- /#page-wrapper -->
    </div>
    <!-- /#wrapper -->

<!-- jQuery -->
    <script src="../../../bower_components/jquery/dist/jquery.min.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="../../../bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

    <!-- Metis Menu Plugin JavaScript -->
    <script src="../../../bower_components/metisMenu/dist/metisMenu.min.js"></script>
    
    <!-- Custom Theme JavaScript -->
    <script src="../../../dist/js/sb-admin-2.js"></script>
    
    <!-- Custom Theme JavaScript -->
    <script src="../../../dist/js/sb-admin-2.js"></script>
    
    <!-- DataTables JavaScript -->
    <script src="../../../bower_components/datatables/media/js/jquery.dataTables.min.js"></script>
    <script src="../../../bower_components/datatables-plugins/integration/bootstrap/3/dataTables.bootstrap.min.js"></script>
    <script src="../../../bower_components/datatables-responsive/js/dataTables.responsive.js"></script>
	
</body>

</html>
