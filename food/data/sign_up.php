<?php

session_start();

$con = mysqli_connect('localhost' , 'root', '');

mysqli_select_db($con,'userSignup')

$name = $_POST['name'];
$email = $_POST['Email'];
$pass = $_POST['Password'];

$s = " select * from usertable where username ='$name'";

$result = mysqli_query($con, $s);

$num = mysqli_num_rows($result);

if($num == 1){
    echo" Username Already Taken";
}else{
    $reg = "insert into usertable(username ,email, password) values ('$name','$email','$pass')";
    mysqli_query($con, $reg)
    echo "registration sucessful"

}

?>