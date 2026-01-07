<?php
$upload_dir = "uploads/";
$flag_file  = "flag.txt";

if (!is_dir($upload_dir)) {
    mkdir($upload_dir, 0777, true);
}

echo "<!DOCTYPE html><html><head><title>Upload Result</title>
<style>
body { background:#111; color:#fff; font-family:Arial; padding:20px; }
a { color:#00bcd4; }
pre { background:#222; padding:10px; }
</style>
</head><body>";

if (isset($_FILES["file"]) && !empty($_FILES["file"]["name"])) {

    $file_name = $_FILES["file"]["name"];   // USER CONTROLLED
    $file_tmp  = $_FILES["file"]["tmp_name"];
    $file_type = $_FILES["file"]["type"];   // USER CONTROLLED

    // ❌ Weak validation (intentional)
    if (strpos($file_type, "image") !== false) {

        move_uploaded_file($file_tmp, $upload_dir . $file_name);

        echo "<h3>✅ Upload successful</h3>";
        echo "<p>File: <b>$file_name</b></p>";
        echo "<p>MIME: <b>$file_type</b></p>";

        // 🎯 FLAG CONDITION
        if (strpos($file_name, ".php") !== false) {
            echo "<h2>🎉 FLAG</h2>";
            echo "<pre>" . file_get_contents($flag_file) . "</pre>";
        } else {
            echo "<p>❌ This looks like a normal image.</p>";
        }

    } else {
        echo "<p>❌ Only image files allowed</p>";
    }

} else {
    echo "<p>No file uploaded</p>";
}

echo "<br><a href='index.html'>← Go Back</a>";
echo "</body></html>";
?>
