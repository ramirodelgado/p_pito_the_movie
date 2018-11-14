<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

	<head>
		<title>Renders</title>
		<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />

		<style type="text/css">

			HTML {
				padding: 0px;
				margin: 0px;
			}
			BODY {
				font-family: Verdana, Arial, Helvetica, sans-serif;
				font-size: 11px;
				background: #EEE;
				padding: 15px;
				height:100%;
			}

			H1 {
				font-family: Verdana, Arial, Helvetica, sans-serif;
				font-size: 20px;
				font-weight: normal;
			}

			H2 {
				font-family: Verdana, Arial, Helvetica, sans-serif;
				font-size: 16px;
				font-weight: normal;
				margin: 0px 0px 10px 0px;
			}
			H3 {
				font-family: Verdana, Arial, Helvetica, sans-serif;
				font-size: 12px;
				font-weight: normal;
				margin: 0px 0px 10px 0px;
				text-align: justify;
			}
			.right {

				margin: 1%;
				height: 600px;
				width: 50%;
				border-top: solid 1px #BBB;
				border-left: solid 1px #BBB;
				border-bottom: solid 1px #BBB;
				border-right: solid 1px #FFF;
				background: #FFF;
				padding: 5px;


			}
			.container {
				margin: 1%;
				width: 100%;
				height: 100%;


			}

			.banner {
				text-align: justify;
				margin: 1%;
				width: 30%;


			}

			.left {
				margin:1%;
				height:600px;
				width: 35%;
				border-top: solid 1px #BBB;
				border-left: solid 1px #BBB;
				border-bottom: solid 1px #BBB;
				border-right: solid 1px #FFF;
				background: #FFF;
				overflow: scroll;
				padding: 5px;

			}

		</style>


		<script>
		function openWin() {
		    window.open("/add_job.html");
		}
		</script>
		<script>
		function closeWin() {
				window.opener = self
		    window.close();
		}
		</script>




	</head>

	<body>
		<h1>CURRENT JOBS</h1>
		<p>
		<h2>
			<div id="banner">
				&nbsp;&nbsp;Job number
				&nbsp;&nbsp;Job folder
				&nbsp;&nbsp;Job status
				<br>


				&nbsp;&nbsp;<a href="/cjobs.php?&amp;order=job_n&amp;" target="iframe_j"><span title="Order by job number">ASC</span></a>
				&nbsp;&nbsp;<a href="/cjobs.php?&amp;order=job_folder" target="iframe_j"><span title="Order by job folder">ASC</span></a>
				&nbsp;&nbsp;<a href="/cjobs.php?&amp;order=job_status" target="iframe_j"><span title="Order by job status">ASC</span></a>

				<br>
				&nbsp;&nbsp;<a href="/cjobs.php?&amp;order=job_n&amp;way=DESC" target="iframe_j"><span title="Order by job number descending">DESC</span></a>
				&nbsp;&nbsp;<a href="/cjobs.php?&amp;order=job_folder&amp;way=DESC" target="iframe_j"><span title="Order by job folder descending">DESC</span></a>
				&nbsp;&nbsp;<a href="/cjobs.php?&amp;order=job_status&amp;way=DESC" target="iframe_j"><span title="Order by job status descending">DESC</span></a>
			</div>
		</h2>

		<iframe class="left" src="cjobs.php" name="iframe_j"></iframe>


		<iframe class="right"src="get.php?job=1" name="iframe_a"></iframe>
		<br>
		<br>
		<form><input type="button" value="ADD RENDER JOB" onclick="openWin()"></form>




	</body>

</html>
