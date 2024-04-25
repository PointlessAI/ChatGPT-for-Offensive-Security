<?php
function add_user_to_dvwa_db($host, $database, $user, $password, $new_user_id, $new_first_name, $new_last_name, $new_username, $new_password, $avatar_url) {
    // Create connection
    $conn = new mysqli($host, $user, $password, $database);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Prepare and bind
    $stmt = $conn->prepare("INSERT INTO users (user_id, first_name, last_name, user, password, avatar, last_login, failed_login) VALUES (?, ?, ?, ?, MD5(?), ?, NOW(), 0)");
    $stmt->bind_param("isssss", $new_user_id, $new_first_name, $new_last_name, $new_username, $new_password, $avatar_url);

    // Execute the statement
    if ($stmt->execute()) {
        echo "User $new_username added successfully.";
    } else {
        echo "Failed to insert into MySQL table: " . $stmt->error;
    }

    // Close statement and connection
    $stmt->close();
    $conn->close();
}

// Example usage
add_user_to_dvwa_db(
    '',                 // Database host
    '',                 // Database name
    '',                 // Database username
    '',                 // Database password
    0,                  // New user_id (example value)
    '',                 // New first name
    '',                 // New last name
    '',                 // New username
    '',                 // New password
    'path/to/.jpg'      // Avatar URL
);

?>