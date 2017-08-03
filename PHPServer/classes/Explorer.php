<?php
/*ShitClass*/
/*На отъебись*/
class Explorer{
protected $sql = null;
protected $countBlocks = 0;
protected $countTransactions = 0;

public function __construct(){
$this->sql = mysqli_connect(MySQL_HOST, MySQL_USER, MySQL_PASS, MYSQL_DATABASE);
if (mysqli_connect_errno())
    exit(0);
}


public function UpdateCountBlocks(){
 $tmp  = $this->sql->query("SELECT COUNT(*) as 'total' from Blocks;");
 $tmp =  $tmp->fetch_assoc();
 $this->countBlocks = $tmp["total"];
}

public function GetLastBlocks($last=15)
{
	$this->UpdateCountBlocks();
	if($this->countBlocks < 15)
		$lastBlocks = $this->sql->query("SELECT * FROM Blocks;");
	else
	 $lastBlocks = $this->sql->query("SELECT * FROM Blocks limit ".($this->countBlocks-15).",".$this->countBlocks);
		print "<table>";
		print <<<EOF
		   <tr>
		    <th>ID</th>
		    <th>Size</th>
		    <th>Difficulty</th>
		    <th>Date</th>
   		   </tr>
EOF;
	while($Block = $lastBlocks->fetch_assoc()){
		print "<tr>";
		print "<td><a href=/blocks?id=".$Block['id'].">".$Block['id']."</a></td>";
		print "<td>".$Block['size']."</td>";
		print "<td>".$Block['Difficulty']."</td>";
		print "<td>".$Block['date']."</td>";
		print "</tr>";
	}
		print "</table>";
}public function GetLastTransactions($last=15)
{
	$this->UpdateCountBlocks();
	if($this->countBlocks < 15){
		$lastTransactions = $this->sql->query("SELECT * FROM Blocks_Transactions;");
		$lastTransactionsInput = $this->sql->query("SELECT * FROM Blocks_Transactions_Input;");
		$lastTransactionsOutput = $this->sql->query("SELECT * FROM Blocks_Transactions_Output;");
	}else{
		$lastTransactions = $this->sql->query("SELECT * FROM Blocks_Transactions limit ".($this->countBlocks-15).",".$this->countBlocks);
	 $lastTransactionsOutput = $this->sql->query("SELECT * FROM Blocks_Transactions_Output limit ".($this->countBlocks-15).",".$this->countBlocks);
	}
		print "<table>";
		print <<<EOF
		   <tr>
		    <th>ID of block</th>
		    <th>Count</th>
		    <th>Value</th>
   		   </tr>
EOF;
	while($Transactions = $lastTransactions->fetch_assoc()){
		print "<tr>";
		print "<td><a href=/blocks?id=".$Transactions['id'].">".$Transactions['id']."</a></td>";
		print "<td>".$Transactions['Count_inputs']."</td>";
		print "<td>".$lastTransactionsOutput->fetch_assoc()['value']."</td>";
		print "</tr>";
	}
		print "</table>";
}




}
?>
