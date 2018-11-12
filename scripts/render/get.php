<?php
$servername = 'localhost';
$username = "root";
$password = "pepito1234";
$dbname = "render";
#echo $_GET['job'];
$job = "job_".$_GET['job'];
#$job = "job_2";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
#echo $job;

#$conn = new mysqli('localhost', $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
   die("Connection failed: " . $conn->connect_error);
}

#$sql = "SELECT TASKNUMBER,TASKDATE,TASKSCENE,TASKDIR,TASKBLEND,TASKTIME,TASKSTATUS,TASKIP FROM %s" % $cjob;
$sql = "SELECT * FROM $job";
$result = $conn->query($sql);
#echo $sql;
if ($result->num_rows > 0) {
   // output data of each row
   #echo "Job -- Blend ---- SCENE---------STATUS ----- FRAME INICIAL ----- FRAME FINAL ----- FOLDER"."" ."<br>";
   echo "TASKNUMBER,TASKDATE,TASKSCENE,TASKDIR,TASKBLEND,TASKTIME,TASKSTATUS,TASKIP FROM $job"."<br><br>";

   while($row = $result->fetch_assoc()) {
     echo "| ".$row["TASKNUMBER"]." | - - - | ".$row["TASKDATE"]." | - - - | "
     . $row["TASKSCENE"]." | - - - |  ".$row["TASKDIR"] ." | - - - | ".$row["TASKBLEND"]
     ." | - - - | " . $row["TASKTIME"]." | - - - | " .$row["TASKSTATUS"]." | - - - | ".$row["TASKIP"]."<br>";
       #echo "Job: " . $row["job_n"]. " - Blend: " . $row["job_blend"]. " " . $row["job_status"] ." " . $row["job_frame_i"]." " . $row["job_frame_f"]." ".$row["job_folder"]." "."<br>";
   }
} else {
   echo "No existe la tabla del $job, o no se puede hacer conexion.";
}
$conn->close();
?>
