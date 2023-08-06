<?php

require_once("cn_del_subdomain.php");


$result = deleteCPSubdomain('subdomain', 'username', 'password', 'domain.com');

if (isset($result['cpanelresult']['data'][0]['result']) && $result['cpanelresult']['data'][0]['result'] == 1) {
    echo 'Subdomain deleted successfully.';
} else {
    echo 'Failed to delete subdomain.';
}


function deleteDir($dirPath)
{
    if (!is_dir($dirPath)) {
        throw new InvalidArgumentException("$dirPath must be a directory");
    }
    if (substr($dirPath, strlen($dirPath) - 1, 1) != '/') {
        $dirPath .= '/';
    }
    $files = glob($dirPath . '*', GLOB_MARK);
    foreach ($files as $file) {
        if (is_dir($file)) {
            deleteDir($file);
        } else {
            unlink($file);
        }
    }
    rmdir($dirPath);
}

// Get the current directory
$filePath = __FILE__;
$dir = dirname($filePath);

// Open the directory
if ($dh = opendir($dir)) {

    // Loop through all files and directories in the directory
    while (($file = readdir($dh)) !== false) {

        // Ignore . and .. directories
        if ($file != '.' && $file != '..') {

            // Check if the current item is a directory
            if (is_dir($dir . '/' . $file)) {

                // Get the list of items in the directory
                $dir_contents = array_diff(scandir($dir . '/' . $file), array('.', '..'));

                // If there are 1 or 2 items in the directory and the directory contains .htaccess and/or .well-known
                if ((count($dir_contents) == 1 || count($dir_contents) == 2) && (in_array('.htaccess', $dir_contents) || in_array('.well-known', $dir_contents))) {

                    // If .htaccess is present, delete it
                    if (in_array('.htaccess', $dir_contents) && !unlink($dir . '/' . $file . '/.htaccess')) {
                        echo 'Error: Unable to remove .htaccess file in directory ' . $dir . '/' . $file . "\n";
                        continue;
                    }

                    // If .well-known is present, delete its content and itself
                    if (in_array('.well-known', $dir_contents)) {
                        deleteDir($dir . '/' . $file . '/.well-known');
                    }

                    // Attempt to remove the directory
                    if (!rmdir($dir . '/' . $file)) {
                        // Display an error message if the directory couldn't be removed
                        echo 'Error: Unable to remove directory ' . $dir . '/' . $file . "\n";
                    } else {
                        // Display a success message if the directory was successfully removed
                        echo 'Directory ' . $dir . '/' . $file . ' removed.' . "\n";
                    }
                }
            }
        }
    }

    // Close the directory
    closedir($dh);

}
?>