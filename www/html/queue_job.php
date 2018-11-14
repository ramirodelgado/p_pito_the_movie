<?php
$servername = 'localhost';
$username = "root";
$password = "pepito1234";
$dbname = "render";
$table = "test";


### Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
#echo "conectado"

### GET VARIABLES FROM WEBFORM
#$job = "job_".$_GET['job'];

$ruta=$_POST["ruta"];
$jscene=$_POST['ofolder'];
$fi=$_POST['fi'];
$ff=$_POST['ff'];
$jpriority=$_POST['priority'];

$textstring=$ruta;
$items = preg_split("/\//",$textstring);
$jblend = array_values(array_slice($items, -1))[0];
$arrayruta=explode('/', $textstring, -1);
$jfolder = implode("/", $arrayruta);
//$bfile=end($items);
// print_r( $jfolder."<br>");
// print_r( $jblend."<br>");
// print_r($fi."<br>");
// print_r($ff."<br>");
// print_r($jscene."<br>");


//$fi=19;
//$ff=105;
$jobframes=$ff-$fi+1;
//$jscene='testscene';
//$jblend='testblend';
$jstatus='EN_COLA';
//$jfolder='mnt/z/_FOTO';
if ($jobframes<1){
  echo "Elija un rango valido de frames<br>";
  echo "<a href=\"add_job.html\">Ir a pagina</a>";
  //<a href="add_job.html">regresa</a>
  //<a href="https://www.w3schools.com">Visit W3Schools</a>
}else{


### Check connection
  if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
  }
  $sql = "SELECT * FROM  $table ";
  $result = $conn->query($sql);
  #echo $sql;
  
     #$x=0#echo "si hay";
  $rowcount=mysqli_num_rows($result);
  $rowcount=$rowcount;
  $njobtable="job_".$rowcount;
  $sql_nt="CREATE TABLE ".$njobtable." (TASKNUMBER  INT(20),TASKDATE  CHAR(22),TASKSCENE CHAR(33),TASKFRAME INT(22),TASKDIR CHAR(55),TASKBLEND CHAR(55),TASKTIME TIME(2),TASKSTATUS CHAR(22),TASKIP CHAR(22))";
  ### CREA TABLA
  if(mysqli_query($conn, $sql_nt)){
      echo "Table created successfully.<br>";
      ### AGREGA ROWS
      for ($n = 0; $n < $jobframes; $n++){
        #echo $n."\n";
        $jframe=$n+$fi;
        #ADD JOB
        $sql_ntask="INSERT INTO ".$njobtable." (TASKNUMBER,TASKDATE,TASKSCENE,TASKFRAME,TASKDIR,TASKBLEND,TASKTIME,TASKSTATUS,TASKIP) VALUES ($n,'0','$jscene','$jframe','$jfolder','$jblend','0','$jstatus','0')";
        if(mysqli_query($conn, $sql_ntask)){
          echo "";
          #echo "row $n created successfully";
          #echo $sql_ntask;
        }
        else
        {
          echo "row $n was not created successfully.<br> ". $conn->error;
        }





      }
      echo"ADDED $n FRAMES TO $njobtable, $fi - $ff, OUTPUT FOLDER - $jscene, $jfolder,$jblend .<br>";

      $sql_embedtask="INSERT INTO ".$table." (job_n, job_blend,job_scene, job_status, job_frame_i, job_frame_f, job_folder,job_priority) VALUES ('$rowcount','$jblend','$jscene','$jstatus','$fi','$ff','$jfolder',$jpriority)";
      #echo $sql_embedtask;
      if(mysqli_query($conn, $sql_embedtask)){
        echo "\nJOB $rowcount ADDED.<br>";
      }
      else {
        echo "ERROR AL INSERTAR job $sql_embedtask en $table   <br>". $conn->error;
      }

    }

    else{
      echo "conneccion fallida<br>". $conn->error;
    }
  
}

?>
