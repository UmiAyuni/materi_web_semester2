<!DOCTYPE html>
<html>
<head>
    <title>Menghitung Luas Lingkaran</title>
</head>
<body>
<?php
//konstanta untuk judul
define("Judul","Hitung Luas Lingkaran");
//konstanta nilai phi
define("PHI", 3.14);
echo Judul;
$r=10;
echo "<br> jari-jari = $r cm <br>";
$luas=PHI*$r*$r;
echo "Luas Lingkaran adalah = $luas cm2";

?>
</body>
</html>