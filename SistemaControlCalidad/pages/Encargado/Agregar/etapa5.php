<?php

	#debemos obtener los sectores del huerto del campo seleccionado
	$campo = $_GET['campo'];
	$campo = str_replace(" ","-", $campo);
	$huerto = $_GET['huerto'];
	$huerto = str_replace(" ", "-", $huerto);
	$sector = $_GET['sector'];
	$sector = str_replace(" ", "-", $sector);
	$cuartel = $_POST['cuartel'];
	$cuartel = str_replace(" ", "-", $cuartel);
	
	$command = "python ../../../../ControlDeCalidad/Modules/CCPlanillas/handlerPlanilla.py 5 ".$campo." ".$huerto." ".$sector." ".$cuartel;
	
	#echo $command;
	$variedades = array();
	exec($command, $variedades);#ejecucion del comando
	$numberVariedades = count($variedades);
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
                            Generación de Nueva Plantilla: Recolección de Información de Campo
                        </div>
                        <div class="panel-body">
                            <div class="row">
                                <div class="col-lg-6">
									
									<?php
										echo "<form role=\"form\" method=\"POST\" action=\"etapa6.php?campo=".$_GET['campo']."&huerto=".$_GET['huerto']."&sector=".$_GET['sector']."&cuartel=".$_POST['cuartel']."\">";
									?>	
										<fieldset disabled>
                                            
                                            <div class="form-group">
                                                <label for="disabledSelect">Campo Seleccionado</label>
                                                <select id="disabledSelect" class="form-control" name ="campoSelected">
                                                    <option>
														<?php
															echo $_GET['campo'];
														?>
                                                    </option>
                                                </select>
                                            </div>
                                            
                                            <div class="form-group">
                                                <label for="disabledSelect">Huerto Seleccionado</label>
                                                <select id="disabledSelect" class="form-control" name ="huertoSelected">
                                                    <option>
														<?php
															echo $_GET['huerto'];
														?>
                                                    </option>
                                                </select>
                                            </div>
                                            <div class="form-group">
                                                <label for="disabledSelect">Sector Seleccionado</label>
                                                <select id="disabledSelect" class="form-control" name ="sectorSelected">
                                                    <option>
														<?php
															echo $_GET['sector'];
														?>
                                                    </option>
                                                </select>
                                            </div>
                                            
                                            <div class="form-group">
                                                <label for="disabledSelect">Cuartel Seleccionado</label>
                                                <select id="disabledSelect" class="form-control" name ="cuartelSelected">
                                                    <option>
														<?php
															echo $_POST['cuartel'];
														?>
                                                    </option>
                                                </select>
                                            </div>
                                        </fieldset>
										<div class="form-group">
                                            <label>Seleccione Variedad</label>
                                            <select class="form-control" name="variedad" required=true>
												<?php
													for ($i=0; $i<$numberVariedades; $i++){
														echo "<option>".$variedades[$i]."</option>";
													}
												?>
                                                
                                            </select>
                                        </div>

                                        <button type="submit" class="btn btn-primary">Agregar Variedad</button>
                                        
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
</body>

</html>