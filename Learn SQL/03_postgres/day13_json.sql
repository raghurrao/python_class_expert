-- Day 13: Advanced JSON Querying Script

SELECT 
    event_id,
    json_extract(payload, '$.user') AS user_name,
    json_extract(payload, '$.action') AS action,
    ingested_at
FROM staging_raw_events;
