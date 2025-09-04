-- S3 Suspicious Access
-- Detects unusual S3 GetObject activity from uncommon IPs.
-- logsource: s3_access_logs
SELECT *
FROM s3_access_logs
WHERE eventName = "GetObject" AND not ipAddress in known_ips
ORDER BY eventTime DESC
LIMIT 100; 
