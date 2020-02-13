ECHO -- Preparing to clean database --

partA="postgresql-"
partB=$(heroku pg:info --app invisiflow-staging | grep postgresql | cut -d "-" -f 3)
partC=$(heroku pg:info --app invisiflow-staging | grep postgresql | cut -d "-" -f 4)

ECHO "DELETE FROM data_allegation;" | heroku pg:psql $partA$partB-$partC --app invisiflow-staging

ECHO -- Inserting data into database --
ECHO "INSERT INTO data_allegation(cr_id, summary, add1, add2, city, is_officer_complaint, location, subjects, created_at, updated_at) VALUES('1003534', '', '', '?', 'CHICAGO ILLINOIS', false, 'other', '{}',  '2019-01-09 12:41:26.530261+08', '2019-01-09 12:41:31.205347+08');" | heroku pg:psql $partA$partB-$partC --app invisiflow-staging
ECHO "INSERT INTO data_allegation(cr_id, summary, add1, add2, city, is_officer_complaint, location, subjects, created_at, updated_at) VALUES('1012534', '', '', '?', 'CHICAGO ILLINOIS', false, '', '{}',  '2019-01-09 12:41:26.530261+08', '2019-01-09 12:41:31.205347+08');" | heroku pg:psql $partA$partB-$partC --app invisiflow-staging
ECHO "INSERT INTO data_allegation(cr_id, summary, add1, add2, city, is_officer_complaint, location, subjects, created_at, updated_at) VALUES('C228886', '', '', '', '', false, '', '{}',  '2019-01-09 12:41:26.530261+08', '2019-01-09 12:41:31.205347+08');" | heroku pg:psql $partA$partB-$partC --app invisiflow-staging
ECHO "INSERT INTO data_allegation(cr_id, summary, add1, add2, city, is_officer_complaint, location, subjects, created_at, updated_at) VALUES('1017528', '', '', '', '', false, 'Private Residence', '{}',  '2019-01-09 12:41:26.530261+08', '2019-01-09 12:41:31.205347+08');" | heroku pg:psql $partA$partB-$partC --app invisiflow-staging
ECHO "INSERT INTO data_allegation(cr_id, summary, add1, add2, city, is_officer_complaint, location, subjects, created_at, updated_at) VALUES('1004179', '', '', '?', 'CHICAGO ILLINOIS', false, 'Highway/Expressway', '{}',  '2019-01-09 12:41:26.530261+08', '2019-01-09 12:41:31.205347+08');" | heroku pg:psql $partA$partB-$partC --app invisiflow-staging

ECHO -- Database loaded --
