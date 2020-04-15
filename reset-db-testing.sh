ECHO -- Preparing to clean database --

partA="postgresql-"
partB=$(heroku pg:info --app invisiflow-testing | grep postgresql | cut -d "-" -f 3)
partC=$(heroku pg:info --app invisiflow-testing | grep postgresql | cut -d "-" -f 4)

ECHO "DELETE FROM data_allegation;" | heroku pg:psql $partA$partB-$partC --app invisiflow-testing

ECHO -- Inserting data into database --
ECHO "INSERT INTO data_allegation(cr_id, crid, summary, add1, add2, city, is_officer_complaint, location, subjects, created_at, updated_at) VALUES('C227980', 'C227980', '', '', '', '', false, '', '{}',  '2019-01-09 12:41:26.530261+08', '2019-01-09 12:41:31.205347+08');" | heroku pg:psql $partA$partB-$partC --app invisiflow-testing
ECHO "INSERT INTO data_allegation(cr_id, crid, summary, add1, add2, city, is_officer_complaint, location, subjects, created_at, updated_at) VALUES('1001892','1001892', '', '', '?', 'CHICAGO ILLINOIS', false, '', '{}',  '2019-01-09 12:41:26.530261+08', '2019-01-09 12:41:31.205347+08');" | heroku pg:psql $partA$partB-$partC --app invisiflow-testing
ECHO "INSERT INTO data_allegation(cr_id, crid, summary, add1, add2, city, is_officer_complaint, location, subjects, created_at, updated_at) VALUES('1002393','1002393', '', '60XX', 'South JUSTINE ST', 'CHICAGO ILLINOIS 60636', false, 'street', '{}',  '2019-01-09 12:41:26.530261+08', '2019-01-09 12:41:31.205347+08');" | heroku pg:psql $partA$partB-$partC --app invisiflow-testing
ECHO "INSERT INTO data_allegation(cr_id, crid, summary, add1, add2, city, is_officer_complaint, location, subjects, created_at, updated_at) VALUES('1003121','1003121', '', '', '?', 'CHICAGO ILLINOIS ', false, 'street', '{}',  '2019-01-09 12:41:26.530261+08', '2019-01-09 12:41:31.205347+08');" | heroku pg:psql $partA$partB-$partC --app invisiflow-testing
ECHO "INSERT INTO data_allegation(cr_id, crid, summary, add1, add2, city, is_officer_complaint, location, subjects, created_at, updated_at) VALUES('C228609','C228609', '', '', '', '', false, '', '{}',  '2019-01-09 12:41:26.530261+08', '2019-01-09 12:41:31.205347+08');" | heroku pg:psql $partA$partB-$partC --app invisiflow-testing

ECHO -- Database loaded --
