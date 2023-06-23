<!DOCTYPE html>
<html>
<head>
    <title>Tugas Pertemuan 4</title>
</head>
<body>
    <p><b>NIM : 12210773 <br> Nama : Umi Ayuni <br> Kelas : 12.2C.15</b></p>
<?php
//konstanta untuk judul
define("Judul","Hitung Luas Lingkaran");
//konstanta nilai phi
define("PHI", 3.14);
echo Judul;
$r=14;
echo "<br> jari-jari = $r cm <br>";
$luas=PHI*$r*$r;
echo "Luas Lingkaran adalah = $luas cm2";

?>
</body>
</html>