<?php
$username=$_POST['username']
$password=$_POST['password']
$gender=$_POST['gender']
$email=$_POST['email']

if(!empty($username) || !empty($password) || !empty($email)){
	$host="localhost"
	$dbUsername="root"
	$dbPassword=""
	$dbName="test"

	$conn=new mysql($host,$dbUsername,$dbPassword,$dbName);

	if(mysqli_connect_error()){
		die('Connect Error('. mysqli_connect_errno() .')'. mysqli_connect_error());
	}else{
		$SELECT="SELECT email From users Where email=? Limit 1";
		$INSERT="INSERT into users (username,password,gender,email) values(?,?,?,?)"

		$stmt=$conn->prepare($SELECT);
		$stmt->bind_param("s",$email);
		$stmt->execute();
		$stmt->bind_result($email);
		$stmt->store_result();
		$rnum = $stmt->num-rows;

		if($rnum==0){
			$stmt=$conn->prepare($INSERT);
			$stmt->bind_param("ssss",$username,$password,$gender,$email);
			$stmt->execute();
			echo "new record"

		}else{
			echo "already used email"
		}
		$stmt->close();
		$conn->close();
	}


}else{
	echo "All required fields are ok"
}
