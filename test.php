<?php   
        //By Joe
        //This script is now vulnerable to SQL Injection

        include("admin/config/dbCon.php"); //DB credentials

        session_start(); //Start session

        $attempts = 5;

        if (!isset($_SESSION["logAtt"])) { 
            $_SESSION["logAtt"] = 0;
            $_SESSION["remainingAtt"] = ($attempts - $_SESSION["logAtt"]); //5 login attempts
            $_SESSION["login_time_stamp"] = time();

        } else {
            if ((time() - $_SESSION["login_time_stamp"]) > 150) { //Session timeout
                echo "Session timeout, please refresh";
                session_unset();
                session_destroy();
                exit();
            }
        }

        if ($_SESSION["logAtt"] >= $attempts) { 
            echo "Access Denied, too many attempts";
            exit();
        } else {
            $_SESSION["logAtt"]++; 
            $_SESSION["remainingAtt"]--;
        }

        // Fetch data from form
        $username = $_POST["username"];  
        $password = $_POST["password"]; 
        
        try { // Error handling
            $hashPass = hash("sha256", $password);

            
            $sql = "SELECT `Password` FROM `user` WHERE `Username` = '$username' AND `Password` = '$hashPass'";  
            
            $result = mysqli_query($con, $sql); 

            if (mysqli_num_rows($result) == 1) {
                $_SESSION["auth"] = True; 
                $_SESSION["username"] = $username;
                header("Location: ../Secure-Soft/landingPage.php");

            } else {
                echo "Incorrect log-in details :(";
            }

            mysqli_close($con);
            exit();

        } catch (Exception $e) {
            echo "Oops, something catastrophic has happened :(";
        }
?>
