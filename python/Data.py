SELECT 'user_events' as table_name, COUNT(*) as total_rows FROM dt34_user_events
UNION ALL
SELECT 'transactions', COUNT(*) FROM dt34_transactions
UNION ALL
SELECT 'marketing_spend', COUNT(*) FROM dt34_marketing_spend;

-- Date ranges
SELECT
    'user_events' as table_name,
    MIN(event_timestamp::date) as start_date,
    MAX(event_timestamp::date) as end_date
FROM dt34_user_events
UNION ALL
SELECT
    'transactions',
    MIN(order_date::date),
    MAX(order_date::date)
FROM dt34_transactions
UNION ALL
SELECT
    'marketing_spend',
    MIN(date::date),
    MAX(date::date)
FROM dt34_marketing_spend;

