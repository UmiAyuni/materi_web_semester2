<!DOCTYPE html>
<html>
<head>
    <title>Contoh IF Majemuk</title>
</head>
<body>
   <?php
   $nilai = 90;
   if (($nilai >=0)&& ($nilai<50))
   {$grade = "E" ; }
   if (($nilai >=50)&& ($nilai<60))
   {$grade = "D" ; }
   if (($nilai >=60)&& ($nilai<75))
   {$grade = "C" ; }
   if (($nilai >=75)&& ($nilai<85))
   {$grade = "B" ; }
   if (($nilai >=85)&& ($nilai<100))
   {$grade = "A" ; }
   else
    {$grade ="Nilai diluar Jangkauan" ;}
   echo "Nilai Anda : $nilai, dikonversikan menjadi $grade" ;

   ?> 
</body>
</html>