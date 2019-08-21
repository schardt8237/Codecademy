/*
Here's the first-touch query, in case you need it
*/

WITH first_touch AS (
    SELECT user_id,
        MIN(timestamp) as first_touch_at
    FROM page_visits
    GROUP BY user_id),
ft_attr AS (
SELECT ft.user_id,
    ft.first_touch_at,
    pv.utm_source,
		pv.utm_campaign
FROM first_touch ft
JOIN page_visits pv
    ON ft.user_id = pv.user_id
    AND ft.first_touch_at = pv.timestamp
),
last_touch AS (
    SELECT user_id,
        MIN(timestamp) as last_touch_at
    FROM page_visits
  	WHERE page_name = '4 - purchase'
    GROUP BY user_id),
lt_attr AS (
SELECT lt.user_id,
    lt.last_touch_at,
    pv.utm_source,
		pv.utm_campaign
FROM last_touch lt
JOIN page_visits pv
    ON lt.user_id = pv.user_id
    AND lt.last_touch_at = pv.timestamp
)

/*SELECT COUNT(DISTINCT utm_campaign) AS number_of_campaigns FROM page_visits;
SELECT COUNT(DISTINCT utm_source) AS number_of_sources FROM page_visits;
SELECT DISTINCT utm_campaign, utm_source FROM page_visits;
SELECT DISTINCT page_name FROM page_visits;
SELECT ft_attr.utm_source,
       ft_attr.utm_campaign,
       COUNT(*)
FROM ft_attr
GROUP BY 1, 2
ORDER BY 3 DESC;*/
SELECT lt_attr.utm_source,
       lt_attr.utm_campaign,
       COUNT(*)
FROM lt_attr
GROUP BY 1, 2
ORDER BY 3 DESC;
SELECT COUNT(*) FROM page_visits WHERE page_name = '4 - purchase';