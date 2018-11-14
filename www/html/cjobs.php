<html>

<style type="text/css">
h1{
  margin: 1%;
  width: 100%;
  background: #FFF;
  font-family: Verdana, Arial, Helvetica, sans-serif;
  font-size: 12px;
  font-weight: normal;


}
</style>
<body>






<?php
$servername = 'localhost';
$username = "root";
$password = "pepito1234";
$dbname = "render";
$table = "test";
#echo"test";
if(!empty($_GET['order'])){
  #echo "order exist";
  $order=$_GET['order'];
}
else{
  $order='job_n';
  #echo $order;
  #echo "order do not exist";
}

if(!empty($_GET['way'])){
  #echo "way exist";
  $way=$_GET['way'];
}
else{
  $way='ASC';
  #echo "way do not exist";
}
//////////////////////////////////////////////////


// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
   die("Connection failed: " . $conn->connect_error);
}

#$sql = "SELECT TASKNUMBER,TASKDATE,TASKSCENE,TASKDIR,TASKBLEND,TASKTIME,TASKSTATUS,TASKIP FROM %s" % $cjob;
$sql = "SELECT * FROM $table ORDER BY $order $way";
$result = $conn->query($sql);
#echo $sql;
if ($result->num_rows > 0) {
   // output data of each row
   #echo "Job -- Blend ---- SCENE---------STATUS ----- FRAME INICIAL ----- FRAME FINAL ----- FOLDER"."" ."<br>";
   #echo "TASKNUMBER,TASKDATE,TASKSCENE,TASKDIR,TASKBLEND,TASKTIME,TASKSTATUS,TASKIP FROM $job"."<br><br>";

   while($row = $result->fetch_assoc()) {
     $rstring= " job_".$row["job_n"]." | ".$row["job_scene"]." | "
     . $row["job_blend"]." | ".$row["job_status"] ." |".$row["job_frame_i"]
     ." - " . $row["job_frame_f"]." ";
     $arrayruta=explode('|', $rstring);
     $array= implode("   ", $arrayruta);
     $x=$row["job_n"];
     //$x1="job_".$row["job_n"];
     //echo "<a href=\"/get.php?job=".$x."\" target=\"iframe_a\">".$x."</a><br>";
     echo "<h1><a href=\"/get.php?job=".$x."\" target=\"iframe_a\">".$array."</a><h1><br>";

     //echo "<a href=\"/get.php?job=".$row["job_n"].">c</a>"."<br>";
     //echo "<a href='get.php?&amp;job='".$row["job_n"]"".$array."</a>";
       #echo "Job: " . $row["job_n"]. " - Blend: " . $row["job_blend"]. " " . $row["job_status"] ." " . $row["job_frame_i"]." " . $row["job_frame_f"]." ".$row["job_folder"]." "."<br>";
   }
} else {
   echo "No existe la tabla del $job, o no se puede hacer conexion".$conn->connect_error;
}
$conn->close();
?>
</body>

</html>
