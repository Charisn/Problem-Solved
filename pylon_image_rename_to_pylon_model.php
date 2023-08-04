<?php

require_once $_SERVER['DOCUMENT_ROOT'] . '/config.php';

$mysqli  = new mysqli(DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
$mysqli->set_charset("utf8mb4");


$SQL1 = "SELECT pt.product_id, pt.image, pt.model, pti.image 
FROM `" . DB_PREFIX . "product` pt
LEFT JOIN `" . DB_PREFIX . "product_image` pti
ON  `pt`.product_id = `pti`.product_id";

$SQL2 = "SELECT pt.product_id, pt.image, pt.model, pti.image 
FROM `" . DB_PREFIX . "product` pt
RIGHT JOIN `" . DB_PREFIX . "product_image` pti
ON  `pt`.product_id = `pti`.product_id";

$results1 = $mysqli->query($SQL1);
$results2 = $mysqli->query($SQL2);

$rows1 = mysqli_fetch_all($results1);
$rows2 = mysqli_fetch_all($results2);
$rows = $rows1 + $rows2;

foreach ( $rows as $row) {
    $old_image_path = DIR_IMAGE . 'pylon_images/' . $row[1];
    $png = '.png';
    if(strpos($old_image_path, $png) !== false ){
        $new_image_path = DIR_IMAGE . 'pylon_images/catalog/products/' . $row[2] . '-01-Μεγάλη' . '.png';
    } else {
        $new_image_path = DIR_IMAGE . 'pylon_images/catalog/products/' . $row[2] . '-01-Μεγάλη' . '.jpg';
    }

    if(file_exists($old_image_path)){   
        rename($old_image_path, $new_image_path);
        echo 'FOUND: ' . $old_image_path . '<br>';
    } else {
        echo 'Did not find:' . $old_image_path . '<br>';
    }
}

$mysqli->close();