<?php
    // Sender's phone numer
    $from_number = $_REQUEST["From"];
    // Receiver's phone number - Plivo number
    $to_number = $_REQUEST["To"];
    // The SMS text message which was received
    $text = $_REQUEST["Text"];
    // Output the text which was received to the log file.
    error_log("Message received - From: $from_number, To: $to_number, Text: $text");
?>
