<?php

// get the reletive path
$doc_root = $_SERVER['DOCUMENT_ROOT'];
$current_dir = __DIR__;
$reletive_path = str_replace($doc_root, '', $current_dir) . '/';

$nav_links = [
    'Home' => $reletive_path . 'index.php',
]
?>
