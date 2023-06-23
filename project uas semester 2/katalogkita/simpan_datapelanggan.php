<?php
include 'koneksi.php';
$nama=$_POST['nama'];
$user=$_POST['username'];
$pass=$_POST['password'];
$telp=$_POST['telp'];
$email=$_POST['email'];

$sql=mysqli_query($koneksi,"insert into pelanggan values('$nama','$user','$pass','$telp', '$email')");
if ($sql)
{
    ?>
    <script type="text/javascript">
        alert ('Data Berhasil Disimpan, Silahkan Gunakan Untuk Login');
        window.location="index.php";
    </script>
    <?php
}
?> 
