<html>
<head>
    <meta charset="UTF-8">
    <title>Листинг 11-2. Добавление в базу данных информации, введенной пользователем</title>
</head>
<body>
<?php

function Add_to_database($name, $city, $address, $birthday, $mail, &$dberror) {
    $user = "root";
    $pass = "qwerty";
    $db = "shopsdb";
    $table = "notebook";

    $conn = mysqli_connect("localhost", $user, $pass);
    if (!$conn) {
        $dberror = "Нет соединения с MySQL сервером";
        return false;
    }
    if (!mysqli_select_db($conn, $db)) {
        $dberror = mysqli_error($conn);
        mysqli_close($conn);
        return false;
    }
    $query = "INSERT INTO $table (name, city, address, birthday, mail) VALUES('$name', $city, $address, $birthday, '$mail')";
    if (!mysqli_query($conn, $query)) {
        $dberror = mysqli_error($conn);
        mysqli_close($conn);
        return false;
    }
    mysqli_close($conn);
    return true;
}

function Write_form() {
    print "<form action='{$_SERVER['PHP_SELF']}' method='post'>";
    print "<p>Введите фамилию и имя [*]:";
    print "<input type='text' name='name'>\n";
    print "<p>Введите город:";
    print "<input type='text' name='city'>\n";
    print "<p>Введите адрес:";
    print "<input type='text' name='address'>\n";
    print "<p>Введите дату рождения в формате ГГГГ-ММ-ДД:";
    print "<input type='text' name='birthday'>\n";
    print "<p>Введите e-mail [*]:";
    print "<input type='text' name='mail'>\n";
    print "<p><input type='submit' value='Записать! '>\n
                </form>\n";
    print "<p>Поля, помеченные [*], являются обязательными для заполнения!";
}

if ($_POST['name'] != "" && $_POST['mail'] != "") {
    $dberror = "";
    if ($_POST['city'] != "") {
        $city = "'" . $_POST['city'] . "'";
    } else {
        $city = "NULL";
    }

    if ($_POST['address'] != "") {
        $address = "'" . $_POST['address'] . "'";
    } else {
        $address = "NULL";
    }

    if ($_POST['birthday'] != "") {
        $birthday = "'" . $_POST['birthday'] . "'";
    } else {
        $birthday = "NULL";
    }


    $ret = Add_to_database($_POST['name'], $city, $address, $birthday, $_POST['mail'], $dberror);
    if (!$ret) {
        print "Ошибка: $dberror<br>";
    } else {
        print "Спасибо ";
    }
}
else Write_form();
?>
</body>
</html>