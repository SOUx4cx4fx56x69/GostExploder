<?php
require_once("../config.php");
require_once("../classes/Explorer.php");
require_once("../classes/Searcher.php");
?>
<!doctype html>
<html>
 <head>
  <meta charset=utf-8>
  <link rel=stylesheet href="../style/main.css">
  <script src="/style/js/main.js"></script>
  <title>GostExplorer</title>
 </head>
 <body>
<div id=loader>
<div class=spinner></div>
<noscript><h2>Ahtung you don't have JS in browser, if you are paranoid, sorry.</h2></noscript>
</div>
<header id=header>
     <div id=banner>
     <span class='brand'><a href=#></a></span>
	<ul class=nav>
		<li><a href=/blocks> Blocks</a></li>
	</ul>
	<ul class=rightnav>
		<form action=/Search.php METHOD=POST>
			<input type=textarea name=what placeholder="Search">
		</form>
	</ul>
    </div>
</header>
<div id="wrap" class="container">

<?php
if(!isset($_GET['id']))
{
print "<h1 class=center-text>Latest Blocks</h1>";
$Explorer = new Explorer();
$Explorer->GetLastBlocks(30);
}
else{
print "<h1 class=center-text>Block id of ".$_GET['id']."</h1>";
$Searcher = new Searcher();
$Searcher->GetFullInfoOfBlock($_GET['id']);
}
?>
</div>
</body>
</html>

