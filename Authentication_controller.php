<?php

class Authentication_model extends CI_Model {
    public function register($data) {
        $sql = "SELECT * FROM `signup`;";

        if ($sql) {
            return $sql;
        } else {
            return FALSE;
        }
        
    }

    public function login($email) {
        $sql = $this -> db -> query("SELECT * FROM `signup` WHERE `email` = '$email'");
        
        if ($sql) {
            return $sql -> result();
        } else {
            return FALSE;
        }
        
    }
    
    public function updatePassword($password, $email) {
        $check_data_select = $this -> db -> query("UPDATE `users_registration` SET `password`='$password' WHERE `email` = '$email'");
        
    }
}
