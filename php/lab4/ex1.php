<?php
$mysql_user = "root";
$mysql_pass = "qwerty";
$conn = mysqli_connect("localhost", $mysql_user, $mysql_pass);
if (mysqli_connect_errno()) {
    die("Нет соединения с MySQL: " . mysqli_connect_error());
}

$database = "shopsdb";
if (!mysqli_select_db($conn, $database)) {
    print "Нельзя открыть $database";
    mysqli_close($conn);
    exit;
}
else {
    print "База $database открыта";
    echo "<br>";
}

$new_table_name = "notebook";
$query = "DROP TABLE IF EXISTS " . $new_table_name;

$result = mysqli_query($conn, $query);
if (!$result) {
    print "Не получилось дропнуть таблицу $new_table_name";
    mysqli_close($conn);
    exit;
}
else {
    print "Получилось дропнуть таблицу $new_table_name";
    echo "<br>";
}

$query = "CREATE TABLE " . $new_table_name .
    "(id int NOT NULL AUTO_INCREMENT,
      name varchar(50),
      city varchar(50),
      address varchar(50),
      birthday date,
      mail varchar(50),
      PRIMARY KEY(id))";


$result = mysqli_query($conn, $query);
if (!$result) {
    print "Не получилось создать таблицу $new_table_name";
    mysqli_close($conn);
    exit;
}
else {
    print "Получилось создать таблицу $new_table_name";
    echo "<br>";
}

mysqli_close($conn);
?>