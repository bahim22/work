Send-MailMessage -From 'User01 <user01@fabrikam.com>' -To 'User02 <user02@fabrikam.com>', 'User03 <user03@fabrikam.com>' -Subject 'Sending the Attachment' -Body "Forgot to send the attachment. Sending now." -Attachments .\data.csv -Priority High -DeliveryNotificationOption OnSuccess, OnFailure -SmtpServer 'smtp.fabrikam.com'

Send-MailMessage -From 'User01 <user01@fabrikam.com>' -To 'ITGroup <itdept@fabrikam.com>' -Cc 'User02 <user02@fabrikam.com>' -Bcc 'ITMgr <itmgr@fabrikam.com>' -Subject "Don't forget today's meeting!" -Credential domain01\admin01 -UseSsl

<#
        The Credential parameter specifies a domain administrator's credentials are used to send the message. The UseSsl parameter specifies that Secure Socket Layer (SSL) creates a secure connection.

        -Port The default value is 25, which is the default SMTP port.

        
    -SmtpServer Specifies the name of the SMTP server that sends the email message.

        The default value is 25, ($PSEmailServer) which is the default SMTP port.

#>