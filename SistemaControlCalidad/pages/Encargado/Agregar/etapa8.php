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
	
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerPlanilla.py 9 ".$campo;
	
	#echo $command;
	$defectos = array();
	exec($command, $defectos);#ejecucion del comando
	$numberDefectos = count($defectos);
	$varClass1 = "<tr class=\"gradeU\">";
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
												echo $_GET['campo'];
												?>
											</td>
											<td>
												<?php
												echo $_GET['huerto'];
												?>
											</td>
											<td>
												<?php
												echo $_GET['sector'];
												?>
											</td>
											<td>
												<?php
												echo $_GET['cuartel'];
												?>
											</td>
											<td>
												<?php
												echo $_GET['variedad'];
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
												echo $_GET['jefeCuadrilla'];
												?>
											</td>
											
											<td>
												<?php
												echo $_GET['cuadrilla'];
												?>
											</td>
											<td>
												<?php
													
												echo $_POST['temporada'];
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
			
				 <!-- /.row -->
            <div class="row">
                <div class="col-lg-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Generación de Nueva Plantilla: Recolección de Defectos
                        </div>
                        <div class="panel-body">
                            <div class="row">
                                <div class="col-lg-6">
									
									<?php
										echo "<form role=\"form\" method=\"POST\" action=\"etapa9.php?campo=".$_GET['campo']."&huerto=".$_GET['huerto']."&sector=".$_GET['sector']."&cuartel=".$_GET['cuartel']."&variedad=".$_GET['variedad']."&jefeCuadrilla=".$_GET['jefeCuadrilla']."&cuadrilla=".$_GET['cuadrilla']."&temporada=".$_POST['temporada']."\">";
									?>	
										
										<div class="form-group">
                                            <label>Seleccione Los Defectos del Campo a Utilizar</label>
                                             <p class="help-block">Pulsando la tecla control puedes seleccionar más de uno</p>
                                            <select multiple class="form-control" name="defectos[]" required=true>
												<?php
													for ($i=0; $i<$numberDefectos; $i++){
														echo "<option>".$defectos[$i]."</option>";
													}
												?>
                                                
                                            </select>
                                        </div>

                                        <button type="submit" class="btn btn-primary">Agregar Defectos</button>
                                        
                                    </form>
                                </div>
                            </div>
                            <!-- /.row (nested) -->
                        </div>
                        <!-- /.panel-body -->
                    </div>
                    <!-- /.panel -->
                </div>
                <!-- /.col-lg-12 -->
            </div>
            <!-- /.row -->
            
        </div>
        <!-- /#page-wrapper -->

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
