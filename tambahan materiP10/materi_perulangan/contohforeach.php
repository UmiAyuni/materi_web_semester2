<!DOCTYPE html>
<html>
<head>
    <title>Penggunaan FOREACH</title>
</head>
<body>
  Menggunakan foreach <br>
  <?php
  $warna  = array("merah", "biru", "hijau", "kuning");
  foreach($warna as $nilai){
      echo $nilai ." ";
  }
  ?>
</body>
</html>