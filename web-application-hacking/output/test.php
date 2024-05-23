<?php
$directory = isset($_GET['dir']) ? $_GET['dir'] : '.';

function listFiles($dir)
{
    if (!is_dir($dir)) return;
    $files = scandir($dir);

    echo '<ul>';
    foreach ($files as $file) {
        if ($file == '.' || $file == '..') continue;
        $fullPath = $dir . DIRECTORY_SEPARATOR . $file;
        if (is_dir($fullPath)) {
            echo '<li><a href="?dir=' . urlencode($fullPath) . '">' . htmlspecialchars($file) . '</a></li>';
        } else {
            echo '<li>' . htmlspecialchars($file) . '</li>';
        }
    }
    echo '</ul>';
}

function breadcrumb($dir)
{
    $parts = array_filter(explode(DIRECTORY_SEPARATOR, $dir));
    $path = '';

    echo '<div class="breadcrumbs">';
    echo '<a href="?dir=">Home</a>';
    foreach ($parts as $part) {
        $path .= DIRECTORY_SEPARATOR . $part;
        echo ' / <a href="?dir=' . urlencode($path) . '">' . htmlspecialchars($part) . '</a>';
    }
    echo '</div>';
}

breadcrumb($directory);
listFiles($directory);
?>
