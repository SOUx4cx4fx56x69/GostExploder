<?php
if(!isset($_POST['what'])) return header("Location: index.php");
require_once("config.php");
require_once("classes/Explorer.php");
require_once("classes/Searcher.php");
$Searcher = new Searcher();
$search = $Searcher->search($_POST['what']);
if($search == false)
 return header("Location: index.php");
return header("Location: /blocks/?id=".$search);
?>

