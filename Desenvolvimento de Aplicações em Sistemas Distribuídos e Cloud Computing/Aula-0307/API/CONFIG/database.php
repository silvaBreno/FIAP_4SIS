<?php
class Database{
 
    // dados para acesso ao banco de dados
    private $host = "sql10.freemysqlhosting.net";
    private $db_name = "sql10689476";
    private $username = "sql10689476";
    private $password = "v3vQyMYRQX";
    public $conn;
 
    // método responsável por realizar a conexão com o banco.
	//faz a conexão e retorna a conexão ativa.
    public function getConnection(){
 
        $this->conn = null;
 
        try{
            $this->conn = new PDO("mysql:host=" . $this->host . ";dbname=" . $this->db_name, $this->username, $this->password);
            $this->conn->exec("set names utf8");
        }catch(PDOException $exception){
            echo "Connection error: " . $exception->getMessage();
        }
 
        return $this->conn;
    }
}
?>