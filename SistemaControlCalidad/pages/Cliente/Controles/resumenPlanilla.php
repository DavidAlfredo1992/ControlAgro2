<?php

	$idPlanilla = $_GET['idPlanilla'];
	$idControl = $_GET['idControl'];
	$idCampo = $_GET['idCampo'];
	
	#obtener la informacion asociada a la planilla
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerPlanilla.py 17 ".$idPlanilla;
	$informacion = array();
	#print $command;
	exec($command, $informacion);
	$resumenPlanilla = explode(";", $informacion[0]);
	$varClass1 = "<tr class=\"gradeU\">";
	
	#obtener la informacion asociada al proceso de control de calidad
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerControlCalidad.py 7 ".$idControl;
	$defectos = array();
	#print $command;
	exec($command, $defectos);
	$numberDefectos = count($defectos);
	
	#obtener informacion de la nota y el proceso asociado...
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerControlCalidad.py 8 ".$idControl;
	$infoNota = array();
	#print $command;
	exec($command, $infoNota);
	$informacionNota = explode(";", $infoNota[0]);
	
	#preguntamos por el valor de la nota para determinar el color y el simbolo
	$color="";
	$simbolo="";
	
	if ($informacionNota[0] == 3){
		
		$color = "<div class=\"panel panel-red\">";
		$simbolo= "<i class=\"fa fa-frown-o   fa-5x\"></i>";		
	}else{
		
		if ($informacionNota[0] == 2){
			
			$color = "<div class=\"panel panel-yellow\">";
			$simbolo= "<i class=\"fa  fa-meh-o  fa-5x\"></i>";
		}else{
		
			$color = "<div class=\"panel panel-green\">";
			$simbolo= "<i class=\"fa fa-smile-o fa-5x\"></i>";
		}
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
                            <?php
								echo "<a href=\"../Campo/index.php?idCampo=".$idCampo."\"><i class=\"fa  fa-leaf  fa-fw fa fa-4x\"></i>   Mi Campo</a>";
							?>
                         </li>
                         <li>
                            <?php
								echo "<a href=\"../Campo/defectos.php?idCampo=".$idCampo."\"><i class=\"fa  fa-times-circle  fa-fw fa fa-4x\"></i>   Mis Defectos</a>";
							?>

                        </li> 
                        <li>
                            <a href="../Estadisticas/index.php"><i class="fa fa-bar-chart-o fa-fw fa fa-4x"></i>   Mis Estadísticas</a>
						</li>
                        <li>
                            <?php
								echo "<a href=\"index.php?idCampo=".$idCampo."\"><i class=\"fa fa-warning  fa-fw fa fa-4x\"></i>Mis Alertas</a>";
							?>

                           
                        </li>
                       
                       <li>
                            <a href="#"><i class="fa fa-check-circle fa-fw fa fa-4x"></i>Mis Controles</a>

                           
                        </li>
                        <li>
                            <a href="../index.php"><i class="fa fa-fw fa-fw fa-4x fa-home fa-fw"></i>Menú Principal</a>
                            
                        </li>
                        <li>
                            <a href="../../LoginSystem/login.html"><i class="fa fa-user fa-fw fa fa-4x"></i>Cerrar Sesión</a>
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
                    <h1 class="page-header">Resumen Control de Calidad Efectuado</h1>
                </div>
                <!-- /.col-lg-12 -->
            </div>
            <!-- /.row -->
            
            <!-- /.row -->
            <div class="row">
                <div class="col-lg-3 col-md-6">
                    <?php
						
						echo $color;
                    ?>
                    
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
									
									<?php
										echo $simbolo;
									?>                                    
                                </div>
                                <div class="col-xs-9 text-right">
                                  <div class="huge">
										<?php
											echo $informacionNota[0];
										?>
                                    </div>

                                </div>
                            </div>
                        </div>
                        
							<a href="#">
						
                            <div class="panel-footer">
                                <span class="pull-left">Nota obtenida por el control efectuado</span>
                                <span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>
                                <div class="clearfix"></div>
                            </div>
                        </a>
                    </div>
                </div>
              </div>
              
            <div class="row">
                <div class="col-lg-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Resumen de Información de Campo
                        </div>
                        <div class="panel-body">
                            <div class="row">
                                <div class="col-lg-6">
									
									<!--Agregamos una tabla resumen con la informacion recolectada en la etapa 1-->
									<div class="panel-body">
                            <div class="dataTable_wrapper">
                                <table width="100%" class="table table-striped table-bordered table-hover" id="dataTables-example">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Campo</th>
                                            <th>Huerto</th>
                                            <th>Sector</th>
                                            <th>Cuartel</th>
                                            <th>Variedad</th>
                                        </tr>
									</thead>
									<tbody>
										
										<tr class="gradeU">
											<td>1</td>
											<td>
												<?php
												echo $resumenPlanilla[0];
												?>
											</td>
											<td>
												<?php
												echo $resumenPlanilla[1];
												?>
											</td>
											<td>
												<?php
												echo $resumenPlanilla[2];
												?>
											</td>
											<td>
												<?php
												echo $resumenPlanilla[3];
												?>
											</td>
											<td>
												<?php
												echo $resumenPlanilla[4];
												?>
											</td>
										</tr>
                                    </tbody>
                                </table>
                            </div>
                            <!-- /.table-responsive -->
                        </div>
                        <!-- /.panel-body -->
					</div>
                </div>
                <!-- /.col-lg-12 -->
            </div>
			</div>
			
            <!-- /.row -->
            <div class="row">
                <div class="col-lg-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Resumen de Información de Cuadrilla
                        </div>
						<div class="panel-body">
                            <div class="row">
                                <div class="col-lg-6">
									
									<!--Agregamos una tabla resumen con la informacion recolectada en la etapa 1-->
									<div class="panel-body">
                            <div class="dataTable_wrapper">
                                <table width="100%" class="table table-striped table-bordered table-hover" id="dataTables-example">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Jefe de Cuadrilla</th>
                                            <th>Nombre Cuadrilla</th>
                                            <th>Temporada a Evaluar</th>
                                            
                                        </tr>
									</thead>
									<tbody>
										
										<tr class="gradeU">
											<td>1</td>
											<td>
												<?php
												echo $resumenPlanilla[5];
												?>
											</td>
											
											<td>
												<?php
												echo $resumenPlanilla[8];
												?>
											</td>
											<td>
												<?php
													
												echo $resumenPlanilla[6];
												?>
											</td>
											
										</tr>
                                    </tbody>
                                </table>
                            </div>
                            <!-- /.table-responsive -->
                        </div>
                        <!-- /.panel-body -->
                        </div>
                    <!-- /.panel -->
                </div>
                <!-- /.col-lg-12 -->
            </div>
            <!-- /.row -->
			</div>
 <!-- /.row -->
            <div class="row">
                <div class="col-lg-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Resumen de Importancia de Defectos
                        </div>
						<div class="panel-body">
                            <div class="row">
                                <div class="col-lg-6">
									
									<!--Agregamos una tabla resumen con la informacion recolectada en la etapa 1-->
									<div class="panel-body">
                            <div class="dataTable_wrapper">
                                <table width="100%" class="table table-striped table-bordered table-hover" id="dataTables-example">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Defecto</th>
                                            <th>Valor Observado</th>
                                            <th>% de Muestra</th>                                            
                                        </tr>
									</thead>
									<tbody>
										
										<?php
											for ($i=1; $i<=$numberDefectos; $i++){
												
												echo $varClass1;
												$columnas = explode(";", $defectos[$i-1]);
												echo "<td>".$i."</td>";
												echo "<td>".$columnas[0]."</td>";
												echo "<td>".$columnas[1]."</td>";
												echo "<td>".$columnas[2]."</td>";
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
                    <!-- /.panel -->
                </div>
                <!-- /.col-lg-12 -->
            </div>
            </div>
            
            <div class="row">
                <div class="col-lg-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Resumen de Información del Control de Calidad Efectuado
                        </div>
                        <div class="panel-body">
                            <div class="row">
                                <div class="col-lg-6">
									
									<!--Agregamos una tabla resumen con la informacion recolectada en la etapa 1-->
									<div class="panel-body">
                            <div class="dataTable_wrapper">
                                <table width="100%" class="table table-striped table-bordered table-hover" id="dataTables-example">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Fecha</th>
                                            <th>Digitador</th>
                                            <th>Tamaño Muestra</th>
                                        </tr>
									</thead>
									<tbody>
										
										<tr class="gradeU">
											<td>1</td>
											<td>
												<?php
												echo $informacionNota[1];
												?>
											</td>
											<td>
												<?php
												echo $informacionNota[3];
												?>
											</td>
											<td>
												<?php
												echo $informacionNota[2];
												?>
											</td>									
										</tr>
                                    </tbody>
                                </table>
                            </div>
                            <!-- /.table-responsive -->
                        </div>
                        <!-- /.panel-body -->
					</div>
                </div>
                <!-- /.col-lg-12 -->
            </div>
			</div>
			
		</div>
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

