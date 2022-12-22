{% load static %}

<html>

<head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="{% static '/css/style.css' %}">
</head>

<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<body>

<link rel="shortcut icon" type="image/x-icon" href="Saturnn.ico">
   <title>Sistemul solar</title>



<div id="maincontact" >
<h3 style="text-align:center;font-family:monospace;background-color:#8B0000;border-radius:10px;"> Exprimă-ți opinia ! </h2><br><br><br>

<a href="jolie-home.html"><img src="sun.png" alt="sun" width="150" height="150" align="right"></a>

<div id="contact" name="contact">
  <form action="action_page.php" method="get">
    <label for="nume">Nume</label>
    <input type="text" id="nume" name="nume" placeholder="...">
	
    <label for="prenume">Prenume</label>
    <input type="text" id="prenume" name="prenume" placeholder="...">

	
    <label for="statut">Statut</label>
    <select id="statut" name="statut">
      <option value="Elev la Liceul Teoretic G. Moisil">Elev la Liceul Teoretic G. Moisil</option>
      <option value="Elev la alt liceu">Elev la alt liceu</option>
      <option value="Profesor la Liceul Teoretic G. Moisil">Profesor la Liceul Teoretic G. Moisil</option>
	   <option value="Profesor la Liceul Teoretic G. Moisil">Profesor la alt liceu</option>
	      <option value="Alta optiune">Altă opțiune</option>
    </select>
  
    <label for="tip">Tipul mesajului</label>
    <select id="tip" name="tip">
      <option value="contact">Colaborare/Contact</option>
      <option value="sugestie">Sugestie</option>
	   <option value="opinie">Opinie</option>
      <option value="reclamatie">Reclamație</option>
	  
	      <label for="mesaj">Mesaj</label>
	  <textarea id="mesaj" name="mesaj"  placeholder="Scrie aici mesajul tau..." style="height:200px"> </textarea>
	  
  
    <input type="submit" value="Submit">
	
  </form>
</div>

<?php

$servername = "localhost";

$username = "root";

$password = "1458";

$dbname = "IDima";

// Create connection

$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection

if (!$conn) {

    die("Connection failed: " . mysqli_connect_error());

}

$sql = "SELECT nume,prenume,statut,tip,mesaj FROM ATESTAT ORDER BY RAND() LIMIT 6;";

$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0)

{

    // Output data of each row
echo "<div style='width:70%;position:absolute;top:20%;right:10%;left:30%;'><h3 style='font-family:candara; margin-left:200px;'>Rezultate random   <a href='contact.php' style='margin-left:250px;'>
<i class='fa fa-refresh fa-spin' style='font-size:20px'></i> </h3><br><br><br><br>";
    while($row = mysqli_fetch_assoc($result))
    {
		 if (empty($row["nume"])==FALSE){	 
        echo "<div id='box'><h1 style='color:#131339;'>" .$row["nume"] 
		." " .$row["prenume"]."</h1>"."<h3 style='color:black;'><b>Statut: " .$row["statut"]."</b></h3>".
		"<h4 style='color:black;'> Tip mesaj: " .$row["tip"]."</h4>"."<h3 style='color:#ffb366;'><i>" .$row["mesaj"]."</i></h3></div>";
		    }
    }
echo "</div>";
}

else

{

  echo "0 results";

}

mysqli_close($conn);

?>

<br><br> <br> <br>

<h2 style="padding-left:5px; padding-right:5px; font-family:Monospace;text-align:center; background-image:url('2.png'); border-radius:10px;  background-size: cover;
  background-repeat: no-repeat;background-attachment: fixed; color:white;">
<br>
Date de contact: <br> <br> <br>
Timișoara, Romania <br><br>
Tel: +40123456789 <br><br>
Email:iuliaelisa15@yahoo.com<br><br>

 </h2>
 


</div>
</body>
</html>