SELECT ANIMAL_ID, NAME,
        case when SEX_UPON_INTAKE LIKE 'Neutered_Male%' OR SEX_UPON_INTAKE LIKE 'Spayed%' THEN 'O'
            when SEX_UPON_INTAKE LIKE 'Intact%' THEN 'X'
            END AS '중성화'
FROM ANIMAL_INS
ORDER BY animal_id;