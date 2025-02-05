<?php
$servername = "localhost";
$username = "pu";
$password = "password";
$dbname = "test";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = 'INSERT INTO email (email, url) VALUES ("'.($_GET['email']??'').'", "'.($_GET['url']??'').'")';
$result = $conn->query($sql);

$conn->close();
?>