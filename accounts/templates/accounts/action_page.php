<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="style.css">
</head>
<body>


<link rel="shortcut icon" type="image/x-icon" href="Saturnn.ico">
   <title>Sistemul solar</title>
   
<div id="maincontact" >
<a href="jolie-home.html"><img src="sun.png" alt="sun" width="100" height="100" align="right"></a>




<?php

$servername = "localhost";

$username = "root";

$password = "1458";

$dbname = "IDima";

$conn = new mysqli($servername, $username, $password, $dbname);

$nume=$_GET['nume'];

$prenume=$_GET['prenume'];

$statut=$_GET['statut'];

$tip=$_GET['tip'];

$mesaj=$_GET['mesaj'];

if ($conn->connect_error)

{

die("Connection failed: " . $conn->connect_error);

}

$sql="INSERT INTO ATESTAT (nume,prenume,statut,tip,mesaj) values('$nume','$prenume','$statut' ,'$tip' ,'$mesaj')";

$result = $conn->query($sql);

if ($result == TRUE)

{
//id...class...
echo "<br><br><br><br><div id='response'>".$mesaj." </div><br><br>Mesaj adăugat cu succes!";

}

else

{

echo $conn->error;

}

$conn->close();

?> 

</div>
</body>
</html>