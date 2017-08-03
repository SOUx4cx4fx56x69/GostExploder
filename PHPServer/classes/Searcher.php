<?php
class Searcher extends Explorer{
/*ShitClass*/
/*На отъебись*/

public function __construct(){
	parent::__construct();
}
public function search($what){
	$what = mysqli_real_escape_string($this->sql,$what);
	$return = $this->sql->query("SELECT * FROM Blocks where id like '%".$what."%' or prevhash like '%".$what."%' or MerkleRoot like '%".$what."%';");
	$return = $return->fetch_assoc();
	if(is_null($return['id'])) return False;
	return $return['id'];
}

public function GetFullInfoOfBlock($block){
	if(!is_numeric($block)) return False;
	$block = mysqli_real_escape_string($this->sql,$block);
	$thisBlocks = $this->sql->query("SELECT * FROM Blocks where id='".$block."';");
	$thisTransactions = $this->sql->query("SELECT * FROM Blocks_Transactions where id='".$block."';");
	$thisTransactionsInput = $this->sql->query("SELECT * FROM Blocks_Transactions_Input where from_id='".$block."';");
	$thisTransactionsOutput = $this->sql->query("SELECT * FROM Blocks_Transactions_Output where from_id='".$block."';");
		print "<hr><h2 class=center-text>BlockHeader</h2>";
		print "<table style=font-size:0.3em>";
		print <<<EOF
		   <tr>
		    <th>ID</th>
		    <th>Size</th>
		    <th>Version</th>
		    <th>Magic</th>
		    <th>PrevHash</th>
		    <th>MerkleRoot</th>
		    <th>Difficulty</th>
		    <th>Nonce</th>
		    <th>Date</th>
   		   </tr>
EOF;
		$Block = $thisBlocks->fetch_assoc();
		print "<tr>";
		print "<td>".$Block['id']."</td>";
		print "<td>".$Block['size']."</td>";
		print "<td>".$Block['version']."</td>";
		print "<td>".$Block['magic']."</td>";
		print "<td>".$Block['prevhash']."</td>";
		print "<td>".$Block['MerkleRoot']."</td>";
		print "<td>".$Block['Difficulty']."</td>";
		print "<td>".$Block['nonce']."</td>";
		print "<td>".$Block['date']."</td>";
		print "</tr>";
		print "</table><hr>";


		print "<hr><h2 class=center-text>TransactionsInputs</h2>";
		print "<table style=font-size:0.3em>";
		print <<<EOF
		   <tr>
		    <th>txOutId</th>
		    <th>seqNo</th>
		    <th>prevhash</th>
		    <th>scriptSig(base64)</th>
		    <th>scriptlen</th>
   		   </tr>
EOF;
		while($trans = $thisTransactionsInput->fetch_assoc()){
		print "<tr>";
		print "<td>".$trans['txOutId']."</td>";
		print "<td>".$trans['seqNo']."</td>";	
		print "<td>".$trans['prevhash']."</td>";	
		print "<td>".$trans['scriptSig']."</td>";	
		print "<td>".$trans['scriptlen']."</td>";	
		print "</tr>";
		}	
		print "</table><hr>";
		print "<hr><h2 class=center-text>TransactionsOutputs</h2>";
		print "<table style=font-size:0.3em>";
		print <<<EOF
		   <tr>
		    <th>pubkey</th>
		    <th>value</th>
		    <th>scriptlen</th>
   		   </tr>
EOF;
		while($trans = $thisTransactionsOutput->fetch_assoc()){
		print "<tr>";
		print "<td>".$trans['pubkey']."</td>";
		print "<td>".$trans['value']."</td>";	
		print "<td>".$trans['scriptlen']."</td>";	
		print "</tr>";
		}	
		print "</table><hr>";



}


}
?>
