<?php 
$servername = "74.207.251.237"; 
$username = "root"; 
$password = "aceveryday2009"; 
$dbname = "IntrusionDB";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) { 
	die("Connection failed: " . $conn->connect_error); 
}

$sql = "SELECT time, picture FROM IntrusionData";
$result = $conn->query($sql);

if ($result->num_rows > 0) { 
	// output data of each row 
	while($row = $result->fetch_assoc()) { 
		echo $row['time']. "<br>";
		echo '<img src="data:image/jpeg;base64,'.base64_encode( $row['picture'] ) . '" />'. "<br>";
		echo "<br>";
	} 
} else { 
	echo "0 results"; 
} 
$conn->close(); 
?>