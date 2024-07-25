#! /bin/bash

if [[ $1 == "test" ]]
then
  PSQL="psql --username=postgres --dbname=worldcuptest -t --no-align -c"
else
  PSQL="psql --username=freecodecamp --dbname=worldcup -t --no-align -c"
fi

# Do not change code above this line. Use the PSQL variable above to query your database.

cat games.csv | while IFS="," read YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do
  if [[ $YEAR != "year" ]]
  then
    #find winner team id in database and add it if its not there
    WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER'")

    if [[ -z $WINNER_ID ]]
    then
      ADD_RESULT=$($PSQL "INSERT INTO teams(name) VALUES ('$WINNER')")

      echo team added $ADD_RESULT
    fi
    #get newly added winner id
    WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER'")

    #find opponent team id in database and add it if its not there
    OPPONENT_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT'")

    if [[ -z $OPPONENT_ID ]]
    then
      ADD_RESULT=$($PSQL "INSERT INTO teams(name) VALUES ('$OPPONENT')")
      echo team added $ADD_RESULT
    fi
    
    #get newly added ids
    WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER'")
    OPPONENT_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT'")

    #insert the rest of the data in the games table
    ADD_RESULT=$($PSQL "INSERT INTO games(year, round, winner_goals, opponent_goals, winner_id, opponent_id) VALUES ($YEAR, '$ROUND', $WINNER_GOALS, $OPPONENT_GOALS,$WINNER_ID, $OPPONENT_ID)")
    echo game added $ADD_RESULT

  fi

done


