<!DOCTYPE html>
<html lang="en">
<head>

    <title>Form Input Mahasiswa</title>
</head>
<body bgcolor="green">
<b>Pengelolaan Data Mahasiswa</b>
<br>
<form action="tampilmahasiswa.php" method="POST">
<pre>
Nama            :<input type="text" name="nama" maxlength="50">
Alamat          :<input type="text" name="alamat" maxlength="100">
Jenis Kelamin   :<input type="radio" name="jeniskel" value="Laki-laki">Laki-laki<input type="radio" name="jeniskel" value="Perempuan">Perempuan
Pekerjaan       :<select name="pekerjaan">
                 <option value="PILIH">PILIH</option>
                 <option value="Pelajar">Pelajar</option>
                 <option value="Karyawan">Karyawan</option>
                 <option value="Wirausaha">Wirausaha</option>
                 <option value="lain-lain">Lain-lain</option>
                 </select>
Hobby           :<input type="checkbox" name="hobi1" value="Olahraga">Olahraga<input type="checkbox" name="hobi2" value="Musik">Musik<input type="checkbox" name="hobi3" value="Jalan-jalan">Jalan-jalan
</pre>
                 <br>
<input type="submit" value="Kirim"><input type="Reset" value="Batal">
    
</body>
</html>