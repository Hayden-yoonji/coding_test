SELECT count(id) as FISH_COUNT
FROM FISH_INFO
WHERE YEAR(TIME) = 2021 and id is not null;
