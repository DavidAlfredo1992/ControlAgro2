<?php

#obtener numero de campos
$command = "python ../../../ControlDeCalidad/Modules/CCStatistics/statisticsIndex.py 1";
$output = array();
exec($command, $output);#ejecucion del comando
$campos = $output[0];

#obtener numero de variedades
$command = "python ../../../ControlDeCalidad/Modules/CCStatistics/statisticsIndex.py 2";
$output = array();
exec($command, $output);#ejecucion del comando
$variedades = $output[0];

#obtener numero de alertas
$command = "python ../../../ControlDeCalidad/Modules/CCStatistics/statisticsIndex.py 3";
$output = array();
exec($command, $output);#ejecucion del comando
$alertas = $output[0];

#obtener numero de alertas
$command = "python ../../../ControlDeCalidad/Modules/CCStatistics/statisticsIndex.py 4";
$output = array();
exec($command, $output);#ejecucion del comando
$controles = $output[0];

#obtener información del sistema de notificaciones
$command = "python ../../../ControlDeCalidad/Modules/CCStatistics/statisticsIndex.py 5";
$output = array();
exec($command, $output);#ejecucion del comando
$notificaciones = count($output);

$varClass1 = "<i class=\"fa fa-comment fa-fw\"></i>";
$varClass2 = "<span class=\"pull-right text-muted small\">";
$var4 = "#";
$varClass3 = "<a href=\"".$var4."\""."class=\"list-group-item\">";
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
    <link href="../../bower_components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- MetisMenu CSS -->
    <link href="../../bower_components/metisMenu/dist/metisMenu.min.css" rel="stylesheet">

    <!-- Timeline CSS -->
    <link href="../../dist/css/timeline.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="../../dist/css/sb-admin-2.css" rel="stylesheet">

    <!-- Morris Charts CSS -->
    <link href="../../bower_components/morrisjs/morris.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="../../bower_components/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">

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
                <a class="navbar-brand" href="index.php">Sistema de Control de Calidad</a>
            </div>
            <!-- /.navbar-header -->

            <ul class="nav navbar-top-links navbar-right">
                <!-- /.dropdown -->
                <li class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                        <i class="fa fa-user fa-fw"></i>  <i class="fa fa-caret-down"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-user">
                        
                        <li class="divider"></li>
                        <li><a href="index.php"><i class="fa fa-sign-out fa-fw"></i>Volver atrás</a>
                        </li>
                        <li><a href="../LoginSystem/login.html"><i class="fa fa-times-circle"></i> Cerrar Sesión</a>
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
                                    <a href="Usuarios/usersSystem.php">Configuración de Usuarios Sistema del Sistema</a>
                                </li>

                                <li>
                                    <a href="JefeCampo/jefeCampo.php">Configuración de Jefe de Campo</a>
                                </li>
                                
                                <li>
                                    <a href="JefeCuadrilla/jefeCuadrilla.php">Configuración de Jefe de Cuadrilla</a>
                                </li>
                            </ul>
                        <li>
                            <a href="#"><i class="fa fa-leaf fa-fw"></i>Configuración de Campos<span class="fa arrow"></span></a>

                            <ul class="nav nav-second-level">
                                <li>
                                    <a href="Campo/Campo.php">Configuración de Campo</a>
                                </li>

                                <li>
                                    <a href="Huerto/Huerto.php">Configuración de Huerto</a>
                                </li>
                                <li>
                                    <a href="Sector/Sector.php">Configuración de Sector</a>
                                </li>
                                <li>
                                    <a href="Cuartel/Cuartel.php">Configuración de Cuartel</a>
                                </li>

                                <li>
                                    <a href="Variedad/Variedad.php">Configuración de Variedad</a>
                                </li>
                            </ul>
                        <li>
                            <a href="#"><i class="fa fa-wrench fa-fw"></i>Configuración de Cuadrillas<span class="fa arrow"></span></a>

                            <ul class="nav nav-second-level">
                               <li>
                                    <a href="Cuadrilla/Cuadrilla.php">Configuración de Cuadrilla</a>
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
                                    <a href="Temporada/Temporada.php">Configuración de Temporada</a>
                                </li>

                                <li>
                                    <a href="Defecto/Defecto.php">Configuración de Defecto</a>
                                </li>

                                <li>
                                    <a href="Importancia/Importancia.php">Configuración de Importancia</a>
                                </li>
                            </ul>

                        </li>
                        
                        <li>
                            <a href="index.php"><i class="fa fa-home fa-fw"></i>Inicio</a>
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
                <div class="col-lg-3 col-md-6">
                    <div class="panel panel-primary">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
                                    <i class="fa fa-comments fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">
										<?php
											echo $campos;
										?>
                                    </div>
                                    <div>Campos Inscritos</div>
                                </div>
                            </div>
                        </div>
                        <a href="#">
                            <div class="panel-footer">
                                <span class="pull-left">Cantidad de Campos inscritos en Sistema de Control</span>
                                <span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>
                                <div class="clearfix"></div>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="panel panel-green">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
                                    <i class="fa fa-tasks fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">
										<?php
											echo $variedades;
										?>
                                    </div>
                                    <div>Variedades Existentes</div>
                                </div>
                            </div>
                        </div>
                        <a href="#">
                            <div class="panel-footer">
                                <span class="pull-left">Variedades existentes en el sistema</span>
                                <span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>
                                <div class="clearfix"></div>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="panel panel-yellow">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
                                    <i class="fa fa-support fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">
										<?php
											echo $controles;
										?>
                                    </div>
                                    <div>Controles Efectuados</div>
                                </div>
                            </div>
                        </div>
                        <a href="#">
                            <div class="panel-footer">
                                <span class="pull-left">Cantidad de controles efectuados a la fecha</span>
                                <span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>
                                <div class="clearfix"></div>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="panel panel-red">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
                                    <i class="fa fa-shopping-cart fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">
										<?php
											echo $alertas;
										?>
                                    </div>
                                    <div>Alertas Enviadas</div>
                                </div>
                            </div>
                        </div>
                        <a href="#">
                            <div class="panel-footer">
                                <span class="pull-left">Cantidad de Alertas generadas</span>
                                <span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>
                                <div class="clearfix"></div>
                            </div>
                        </a>
                    </div>
                </div>
                
            </div>
            <!-- /.row -->
            <div class="row">
                
                <!-- /.col-lg-8 -->
                <div class="col-lg-4">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <i class="fa fa-bell fa-fw"></i> Alertas Enviadas
                        </div>
                        <!-- /.panel-heading -->
                        <div class="panel-body">
                            <div class="list-group">
								
								<?php
									
									for ($i=1; $i<=$notificaciones; $i++){
										
										echo $varClass3;
										echo $varClass1;
										$columnas = explode(";", $output[$i-1]);
										echo " ".$columnas[0];
										echo $varClass2;
										echo "<em>".$columnas[1]."</em>";
										echo "</span>";
										echo "</a>";
									}
								?>
								
                            </div>
                            <!-- /.list-group -->
                            <a href="#" class="btn btn-default btn-block">View All Alerts</a>
                        </div>
                        <!-- /.panel-body -->
                    </div>
                    <!-- /.panel -->

                    <!-- /.panel -->

                    <!-- /.panel .chat-panel -->
                </div>
                <!-- /.col-lg-4 -->
            </div>
            <!-- /.row -->
        </div>
        <!-- /#page-wrapper -->

    </div>
    <!-- /#wrapper -->

<!-- jQuery -->
    <script src="../../bower_components/jquery/dist/jquery.min.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="../../bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

    <!-- Metis Menu Plugin JavaScript -->
    <script src="../../bower_components/metisMenu/dist/metisMenu.min.js"></script>
    
    <!-- Custom Theme JavaScript -->
    <script src="../../dist/js/sb-admin-2.js"></script>
    
    <!-- Custom Theme JavaScript -->
    <script src="../../dist/js/sb-admin-2.js"></script>
</body>

</html>
