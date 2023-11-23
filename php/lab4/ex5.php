<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
$user = "root";
$pass = "qwerty";
$db = "shopsdb";
$table = "notebook";

$conn = mysqli_connect("localhost", $user, $pass);
if (!$conn) {
    print "Нет соединения с MySQL сервером";
    exit;
}

if (!mysqli_select_db($conn, $db)) {
    mysqli_close($conn);
    exit;
}

$query = "INSERT INTO $table (name, city, address, birthday, mail) VALUES('Петр', 'Новосибирск', 'Улица Демакова 1', '2021-06-05', 'petr7777@mail.ru'), ('Иван', 'Владимир', 
        'Улица Пирогова 1', '2003-04-03', 'ivan@mail.ru'), ('Роман', 'Москва', 'Улица Ленина 32', '1999-09-11', 'roman@mail.ru')";
if (!mysqli_query($conn, $query)) {
    $dberror = mysqli_error($conn);
    mysqli_close($conn);
    exit(-1);
}

print "Всё прошло успешно";
mysqli_close($conn);
?>
</body>
</html>