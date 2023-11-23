<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ex3</title>
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

$result = mysqli_query($conn, "SELECT * FROM $table");
print "<p>Вывод всех строк таблицы $table";
$num_fields = mysqli_num_fields($result);
print "<p><table border=\"1\" text-align=\"center\">\n";
print "<tr>\n";
for ($x = 0; $x < $num_fields; $x++) {
    $name = mysqli_fetch_field_direct($result, $x)->name;
    print "\t<th>$name</th>\n";
}
print "</tr>\n";
while ($a_row = mysqli_fetch_row($result)) {
    print "<tr>\n";
    foreach ($a_row as $field)
        print "\t<td>$field</td>\n";
    print "</tr>\n";
}
print "</table>\n";
mysqli_close($conn);
?>
</body>
</html>