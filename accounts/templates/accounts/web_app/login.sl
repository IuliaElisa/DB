

<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="style.css">
</head>

<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<body>


<div id = "sun-center">
<a href="jolie-home.html"><img src="sun.png" alt="sun" width="100" height="100" align="center" margin-left = "60px"></a>
</div>


<link rel="shortcut icon" type="image/x-icon" href="Saturnn.ico">
   <title>Sistemul solar</title>
<div id="contribute" >
<h1 style="text-align:center; font-family:monospace;background-color:white;border-radius:4px;">We need your help!</h1><br><br><br>


 <?php if (isset($_GET['error'])) { ?>

            <p class="error"><?php echo $_GET['error']; ?></p>

        <?php } ?>
        <label>User Name</label>

        <input type="text" name="uname" placeholder="User Name"><br>

        <label>Password</label>
         <br><br>
        <input type="password" name="password" placeholder="  password"><br> <br><br><br>
        <button type="submit">Login</button>
<br><br> <br>

</div>

<br><br> <br>
<div id="response2">
<h3> Contribute to the International Asteroid Warning Network!</h3>
</div>

</body>
</html>