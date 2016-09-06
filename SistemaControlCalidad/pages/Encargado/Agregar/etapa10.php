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
	$defectos = $_POST['defectos'];
	$temporada = $_GET['temporada'];
	$temporada = str_replace(" ", "-", $temporada);
	$jefeCuadrilla = $_GET['jefeCuadrilla'];
	$jefeCuadrilla = str_replace(" ", "-", $jefeCuadrilla);
	$idPlanilla = $_GET['idPlanilla'];
	$ListaDefectos = "";
	
	for ($i=0; $i<count($defectos); $i++){
		
		if ($i == count($defectos)-1){
			
			$ListaDefectos=$ListaDefectos.$defectos[$i];
		}else{
			
			$ListaDefectos=$ListaDefectos.$defectos[$i].":";
		}
	}

	$ListaDefectos = str_replace(" ", "-", $ListaDefectos);

	#tenemos que insertar en la planilla y agregar los defectos...
		
	#hacemos la insercion en la planilla y en los defectos para la planilla
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerPlanilla.py 11 ".$idPlanilla;
	#echo $command;
	$defectos = array();
	exec($command, $defectos);
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
													
												echo $_GET['temporada'];
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
                            Configuración de Importancia de Defectos
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
                                            <th>Importancia</th>
                                            
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
            
             <div class="row">
                <div class="col-lg-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Configuración de Importancia de Defectos: Selección de Rangos de Notas
                        </div>
						<div class="panel-body">
                            <div class="row">
                                <div class="col-lg-6">
									<?php								
										echo "<form role=\"form\" method=\"POST\" action=\"etapaFinal.php?idPlanilla=".$idPlanilla."\">";
                                    ?>
										<h3>Configuración para la Importancia Mayor</h3>
                                        <div class="form-group has-success">
                                            <label class="control-label" for="inputSuccess">Rango 1</label>
											<select class="form-control" id="inputSuccess" name="mayor1" required="true">
												<?php
													for ($i=0; $i<3;$i++){
														echo "<option>".$i."</option>";
													}                                              
                                                ?>
                                            </select>
                                            
                                        </div>
                                        <div class="form-group has-warning">
                                            <label class="control-label" for="inputWarning">Rango 2</label>
                                            <select class="form-control" id="inputWarning" name="mayor2" required="true">
												<?php
													for ($i=0; $i<8;$i++){
														echo "<option>".$i."</option>";
													}                                              
                                                ?>
                                            </select>
                                        </div>
                                        <div class="form-group has-error">
                                            <label class="control-label" for="inputError">Rango 3</label>
                                            <select class="form-control" id="inputError" name="mayor3" required="true">
												<?php
													for ($i=0; $i<15;$i++){
														echo "<option>".$i."</option>";
													}                                              
                                                ?>
                                            </select>
                                        </div>
                                        
                                        <h3>Configuración para la Importancia Menor</h3>
                                        <div class="form-group has-success">
                                            <label class="control-label" for="inputSuccess">Rango 1</label>
											<select class="form-control" id="inputSuccess" name="menor1" required="true">
												<?php
													for ($i=0; $i<10;$i++){
														echo "<option>".$i."</option>";
													}                                              
                                                ?>
                                            </select>
                                            
                                        </div>
                                        <div class="form-group has-warning">
                                            <label class="control-label" for="inputWarning">Rango 2</label>
                                            <select class="form-control" id="inputWarning" name="menor2" required="true">
												<?php
													for ($i=0; $i<16;$i++){
														echo "<option>".$i."</option>";
													}                                              
                                                ?>
                                            </select>
                                        </div>
                                        <div class="form-group has-error">
                                            <label class="control-label" for="inputError">Rango 3</label>
                                            <select class="form-control" id="inputError" name="menor3" required="true">
												<?php
													for ($i=0; $i<20;$i++){
														echo "<option>".$i."</option>";
													}                                              
                                                ?>
                                            </select>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Guardar Configuración</button>
                                    </form>
                        </div>
                    <!-- /.panel -->
                </div>
                <!-- /.col-lg-12 -->
            </div>
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

