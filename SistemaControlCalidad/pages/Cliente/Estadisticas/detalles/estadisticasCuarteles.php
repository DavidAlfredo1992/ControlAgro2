<?php
	 
	$idCampo = $_GET['idCampo'];
	$cuartel = $_GET['cuartel'];
	$sector = $_GET['sector'];
	$huerto = $_GET['huerto'];
	$cuartel = str_replace(" ",  "-", $cuartel);
	$sector = str_replace(" ",  "-", $sector);
	$huerto = str_replace(" ",  "-", $huerto);
	
	#echo $cuartel."<br>".$sector."<br>".$huerto;
	$command = "python ../../../../../ControlDeCalidad/Modules/CCStatistics/statisticsCliente.py 15 ".$idCampo. " ".$huerto. " ".$sector." ".$cuartel;
	$dataGraphic1 = array();
	exec($command, $dataGraphic1);
	#$numberUser = count($output);
	
	#controles de muestra 50
	$command = "python ../../../../../ControlDeCalidad/Modules/CCStatistics/statisticsCliente.py 16 ".$idCampo. " ".$huerto. " ".$sector." ".$cuartel." 50";
	$ouput = array();
	#echo $command;
	exec($command, $ouput);
	$controles50 = $ouput[0];
	
	#controles de muestra 100
	$command = "python ../../../../../ControlDeCalidad/Modules/CCStatistics/statisticsCliente.py 16 ".$idCampo. " ".$huerto. " ".$sector." ".$cuartel." 100";
	$ouput = array();
	exec($command, $ouput);
	$controles100 = $ouput[0];
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
    <link href="../../../../bower_components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- MetisMenu CSS -->
    <link href="../../../../bower_components/metisMenu/dist/metisMenu.min.css" rel="stylesheet">

    <!-- Timeline CSS -->
    <link href="../../../../dist/css/timeline.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="../../../../dist/css/sb-admin-2.css" rel="stylesheet">

    <!-- Morris Charts CSS -->
    <link href="../../../../bower_components/morrisjs/morris.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="../../../../bower_components/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">

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
								echo "<a href=\"../index.php?idCampo=".$idCampo."\"><i class=\"fa  fa-leaf  fa-fw fa fa-4x\"></i>   Mi Campo</a>";
							?>
                         </li>
                         <li>
                         <?php
								echo "<a href=\"../defectos.php?idCampo=".$idCampo."\"><i class=\"fa  fa-times-circle  fa-fw fa fa-4x\"></i>   Mis Defectos</a>";
							?>

                        </li> 
                        <li>
                            <?php
							
								echo "<a href=\"../Estadisticas/index.php?idCampo=".$idCampo."\"><i class=\"fa fa-bar-chart-o fa-fw fa fa-4x\"></i>   Mis Estadísticas</a>";
							?>
						</li>
                        <li>
                            <?php
								echo "<a href=\"../Alertas/index.php?idCampo=".$idCampo."\"><i class=\"fa fa-warning  fa-fw fa fa-4x\"></i>Mis Alertas</a>";
							?>

                           
                        </li>
                       <li>
                            <?php
								echo "<a href=\"../Controles/index.php?idCampo=".$idCampo."\"><i class=\"fa fa-check-circle fa-fw fa fa-4x\"></i>Mis Controles</a>";
							?>

                           
                        </li>
                        <li>
                            <a href="../../index.php"><i class="fa fa-fw fa-fw fa-4x fa-home fa-fw"></i>Menú Principal</a>
                            
                        </li>
                        <li>
                            <a href="../../../LoginSystem/login.html"><i class="fa fa-user fa-fw fa fa-4x"></i>Cerrar Sesión</a>
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
					<h1 class="page-header">Controles Efectuados por Cuartel</h1>
				</div>
                <!-- /.col-lg-12 -->
            </div>
			<div class="row">
				<div class="col-lg-3 col-md-6">
                    <div class="panel panel-red">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
                                    <i class="fa fa-check-circle  fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">
										<?php
											echo $controles50;
										?>
                                    </div>
                                    
                                </div>
                            </div>
                        </div>
                        <a href="#">
                            <div class="panel-footer">
                                <span class="pull-left">Con tamaño de muestra 50</span>
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
                                    <i class="fa fa-check-circle  fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">
										<?php
											echo $controles100;
										?>
                                    </div>
                                    
                                </div>
                            </div>
                        </div>
                        <a href="#">
                            <div class="panel-footer">
                                <span class="pull-left">Con tamaño de muestra 100</span>
                                <span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>
                                <div class="clearfix"></div>
                            </div>
                        </a>
                    </div>               
                </div>

             </div>
            
              
            <div class="row">
				<div class="col-lg-12">
					<h1 class="page-header">Defectos evaluados en Controles de Calidad</h1>
				</div>
                <!-- /.col-lg-12 -->
            </div>

			<div class="row">
				<div class="col-lg-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
							Defectos Evaluados en controles de calidad por Cuartel
						</div>
						<!-- /.panel-heading -->
                        <div class="panel-body">
                            <div id="container" style="min-width: 310px; height: 400px; max-width: 600px; margin: 0 auto"></div>
                        </div>
                        <?php
							echo "<a href=\"resumenVariedad.php?idCampo=".$idCampo."&info=".$dataGraphic1[1]."\">";
						?>
                            <div class="panel-footer">
                                <span class="pull-left">Ver Resumen</span>
                                <span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>
                                <div class="clearfix"></div>
                            </div>
                        </a>
                    </div>                    
                </div>                   
            </div>
        </div>
        <!-- /#page-wrapper -->
    </div>
    <!-- /#wrapper -->


   <!-- jQuery -->
    <script src="../../../../bower_components/jquery/dist/jquery.min.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="../../../../bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

    <!-- Metis Menu Plugin JavaScript -->
    <script src="../../../../bower_components/metisMenu/dist/metisMenu.min.js"></script>
	
	<script src="https://code.highcharts.com/highcharts.js"></script>
	<script src="https://code.highcharts.com/modules/exporting.js"></script>

	<script>
		$(function () {

    // Make monochrome colors and set them as default for all pies
    Highcharts.getOptions().plotOptions.pie.colors = (function () {
        var colors = [],
            base = Highcharts.getOptions().colors[0],
            i;

        for (i = 0; i < 10; i += 1) {
            // Start out with a darkened base color (negative brighten), and end
            // up with a much brighter color
            colors.push(Highcharts.Color(base).brighten((i - 3) / 7).get());
        }
        return colors;
    }());

    // Build the chart
    $('#container').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Defectos en Controles Encontrados Por Cuartel'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            name: 'Variedades',
            data: [
                
                <?php echo $dataGraphic1[0]?>
            ]
        }]
    });
});
	</script>
</body>

</html>

