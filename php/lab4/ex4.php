<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .container{
            display: flex;
            align-items: center;
            gap: 10px;
        }
    </style>
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

if (isset($_POST['id']) && isset($_POST['field_name']) && isset($_POST['field_value'])) {
    $id = $_POST['id'];
    $field_name = $_POST['field_name'];
    $field_value = $_POST['field_value'];


    $query = "UPDATE $table SET $field_name='$field_value' WHERE id=$id";
    $result = mysqli_query($conn, $query);
    if (!$result) {
        print "<p>Не удалось обновить $field_value у $field_name с id=$id\n";
    } else {
        print "<p>Обновление прошло успешно\n";
        print "<p><a href='ex3.php'>Посмотреть на результат</a>\n";
    }
}
else if (isset($_POST['id'])) {
    $id = $_POST['id'];
    $fields_num = $_POST['fields_num'];
    $result = mysqli_query($conn, "SELECT * FROM $table WHERE id=$id");

    $column_names = array();
    for ($x = 1; $x < $fields_num; $x++) {
        array_push($column_names, mysqli_fetch_field_direct($result, $x)->name);
    }

    print "<form action='{$_SERVER['PHP_SELF']}' method='post'>\n";
    print "\t<div class=\"container\">\n";
    print "\t\t<input type=\"hidden\" name=\"id\" value=\"$id\">";
    $a_row = mysqli_fetch_row($result);
    print "\t\t<select name=\"field_name\">\n";
    $i = 1;
    foreach ($column_names as $column_name) {
        $value = $a_row[$i++];
        print "\t\t\t<option value=\"$column_name\">$value</option>\n";
    }
    print "\t\t</select>\n";
    print "\t\t<p>введите новое значение</p>\n";
    print "\t\t<input type=\"text\" name=\"field_value\">\n";
    print "\t</div>\n";
    print "\t<input type=\"submit\" value=\"Заменить\">\n</form>\n";

} else {
    $result = mysqli_query($conn, "SELECT * FROM $table");
    $num_fields = mysqli_num_fields($result);
    print "<form action='{$_SERVER['PHP_SELF']}' method='post'>";
    print "<p><table border=\"1\" text-align=\"center\">\n";
    print "<tr>\n";
    for ($x = 0; $x < $num_fields; $x++) {
        $name = mysqli_fetch_field_direct($result, $x)->name;
        print "\t<th>$name</th>\n";
    }
    print "\t<th>исправить</th>\n";
    print "</tr>\n";
    while ($a_row = mysqli_fetch_row($result)) {
        $id = $a_row[0];
        print "<tr>\n";
        foreach ($a_row as $field)
            print "\t<td>$field</td>\n";
        print "\t<td><input type=\"radio\" name=\"id\" value=\"$id\"></td>\n";
        print "</tr>\n";
    }
    print "</table>\n";
    print "<input type=\"hidden\" name=\"fields_num\" value=\"$num_fields\">";
    print "<p><input type='submit' value='Выбрать!'>\n
                    </form>\n";
}
mysqli_close($conn);
?>
</body>
</html>