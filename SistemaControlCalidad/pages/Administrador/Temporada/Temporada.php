<?php

	#get all information for complet data table
	#get number of user in data bases
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerTemporada.py 1";
	$output = array();
	exec($command, $output);#ejecucion del comando
	$numberUser = count($output);
	$varClass1 = "<tr class=\"gradeU\">";
	#$varClass2 = "<tr class=\"gradeC\">";
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

    <!-- DataTables CSS -->
    <link href="../../../bower_components/datatables-plugins/integration/bootstrap/3/dataTables.bootstrap.css" rel="stylesheet">

    <!-- DataTables Responsive CSS -->
    <link href="../../../bower_components/datatables-responsive/css/dataTables.responsive.css" rel="stylesheet">

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

            <ul class="nav navbar-top-links navbar-right">
                <!-- /.dropdown -->
                <li class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                        <i class="fa fa-gears  fa-fw"></i>  <i class="fa fa-caret-down"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-user">
                        
                        <li class="divider"></li>
                        <li><a href="addTemporada.php"><i class="fa fa-plus-circle fa-fw"></i>Agregar Temporada</a>
                        </li>
                        <li><a href="Temporada.php"><i class="fa fa-spinner fa-fw"></i>Actualizar</a>
                        </li>
                    </ul>
                    <!-- /.dropdown-user -->
                </li>
                
                <li class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                        <i class="fa fa-user fa-fw"></i>  <i class="fa fa-caret-down"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-user">
                        
                        <li class="divider"></li>
                        <li><a href="../index.php"><i class="fa fa-sign-out fa-fw"></i>Volver atrás</a>
                        </li>
                        <li><a href="../../LoginSystem/login.html"><i class="fa fa-times-circle fa-fw"></i> Cerrar Sesión</a>
                        </li>
                    </ul>
                    <!-- /.dropdown-user -->
                </li>
                <!-- /.dropdown -->
            </ul>
            <!-- /.navbar-top-links -->

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
                            <a href="#"><i class="fa fa-group fa-fw"></i>Configuración de Usuarios<span class="fa arrow"></span></a>
                            <ul class="nav nav-second-level">
                                <li>
                                    <a href="../Usuarios/usersSystem.php">Configuración de Usuarios Sistema del Sistema</a>
                                </li>

                                <li>
                                    <a href="../JefeCampo/jefeCampo.php">Configuración de Jefe de Campo</a>
                                </li>
                                
                                <li>
                                    <a href="../JefeCuadrilla/jefeCuadrilla.php">Configuración de Jefe de Cuadrilla</a>
                                </li>
                            </ul>
                        <li>
                            <a href="#"><i class="fa fa-leaf fa-fw"></i>Configuración de Campos<span class="fa arrow"></span></a>

                            <ul class="nav nav-second-level">
                                <li>
                                    <a href="../Campo/Campo.php">Configuración de Campo</a>
                                </li>

                                <li>
                                    <a href="../Huerto/Huerto.php">Configuración de Huerto</a>
                                </li>
                                <li>
                                    <a href="../Sector/Sector.php">Configuración de Sector</a>
                                </li>
                                <li>
                                    <a href="../Cuartel/Cuartel.php">Configuración de Cuartel</a>
                                </li>

                                <li>
                                    <a href="../Variedad/Variedad.php">Configuración de Variedad</a>
                                </li>
                            </ul>
                        <li>
                            <a href="#"><i class="fa fa-wrench fa-fw"></i>Configuración de Cuadrillas<span class="fa arrow"></span></a>

                            <ul class="nav nav-second-level">
                               <li>
                                    <a href="../Cuadrilla/Cuadrilla.php">Configuración de Cuadrilla</a>
                                </li>

<!--
                                <li>
                                    <a href="SubCuadrilla/SubCuadrilla.php">Configuración de SubCuadrilla</a>
                                </li>
-->

                            </ul>
                        </li>

                        <li>
                            <a href="#"><i class="fa fa-th-large fa-fw"></i>Configuración de Planilla<span class="fa arrow"></span></a>

                            <ul class="nav nav-second-level">
                               <li>
                                    <a href="Temporada.php">Configuración de Temporada</a>
                                </li>

                                <li>
                                    <a href="../Defecto/Defecto.php">Configuración de Defecto</a>
                                </li>

                                <li>
                                    <a href="../Importancia/Importancia.php">Configuración de Importancia</a>
                                </li>
                            </ul>

                        </li>
                        
                        <li>
                            <a href="../index.php"><i class="fa fa-home fa-fw"></i>Inicio</a>
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
                    <h1 class="page-header">Sistema de Administración</h1>
                </div>
                <!-- /.col-lg-12 -->
            </div>
            <!-- /.row -->
            <div class="row">
                <div class="col-lg-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Información general de las Importancias de los Defectos
                           
                        </div>
                        
                        <!-- /.panel-heading -->
                        <div class="panel-body">
                            <div class="dataTable_wrapper">
                                <table width="100%" class="table table-striped table-bordered table-hover" id="dataTables-example">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Nombre Temporada</th>
                                            <th>Opciones</th>
                                        </tr>
									</thead>
									<tbody>
										
                                        <?php
											for ($i=1; $i<=$numberUser; $i++){
												
												echo $varClass1;
												$columnas = explode(";", $output[$i-1]);
												echo "<td>".$i."</td>";
												echo "<td>".$columnas[0]."</td>";
												
												echo "<td>
													<a href=\"editTemporada.php?idArray=".$i."\" class=\"btn btn-warning btn-circle\"><i class=\"fa fa-fw fa-pencil \"></i></a>
													<a href=\"deleteTemporada.php?idArray=".$i."\" class=\"btn btn-danger btn-circle\"><i class=\"fa fa-fw fa-trash-o \"></i></a>";
												
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
        <!-- /#page-wrapper -->

    </div>
    <!-- /#wrapper -->


   <!-- jQuery -->
    <script src="../../../bower_components/jquery/dist/jquery.min.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="../../../bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

    <!-- Metis Menu Plugin JavaScript -->
    <script src="../../../bower_components/metisMenu/dist/metisMenu.min.js"></script>

    <!-- DataTables JavaScript -->
    <script src="../../../bower_components/datatables/media/js/jquery.dataTables.min.js"></script>
    <script src="../../../bower_components/datatables-plugins/integration/bootstrap/3/dataTables.bootstrap.min.js"></script>
    <script src="../../../bower_components/datatables-responsive/js/dataTables.responsive.js"></script>
    
    <!-- Custom Theme JavaScript -->
    <script src="../../../dist/js/sb-admin-2.js"></script>

    <!-- Page-Level Demo Scripts - Tables - Use for reference -->
    <script>
    $(document).ready(function() {
        $('#dataTables-example').DataTable({
                responsive: true
        });
    });
    </script>
</body>

</html>
