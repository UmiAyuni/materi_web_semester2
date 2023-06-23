<?php
include 'koneksi.php';
$id=$_POST['id'];
$user=$_POST['username'];
$pass=$_POST['password'];
$sql=mysqli_query($koneksi,"select * from pelanggan where username='$user' and password='$pass' ");
$cek=mysqli_num_rows($sql);

    if ($cek>0)
    {
        $data=mysqli_fetch_array($sql);
        session_start();
        $_SESSION['nama']=$user;
        header('location:tampilmenu.php');
    }
    else
    {
    ?>
    <script type="text/javascript">
        alert ('Username atau Password salah');
        window.location="index.php";
    </script>
<?php
    }
    ?>
