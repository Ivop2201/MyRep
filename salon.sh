#! /bin/bash

PSQL="psql --username=freecodecamp --dbname=salon --tuples-only -c"



MENU(){
  if [[ $1 ]]
  then 
    echo -e "\n$1"
  fi

  echo -e "\n\n~~~~~ MY SALON ~~~~~\n\n"
  echo Welcome to My Salon, how can I help you?


  SERVICES=$($PSQL "SELECT service_id, name FROM services WHERE name IS NOT NULL ORDER BY service_id") 
  echo "$SERVICES" | while read SERVICE BAR NAME
  do
    echo "$SERVICE) $NAME"
  done
  read SERVICE_ID_SELECTED

  #check selection on service table
  SERVICE_NAME=$($PSQL "SELECT name FROM services WHERE service_id=$SERVICE_ID_SELECTED")

  #if service is not fund
  if [[ -z $SERVICE_NAME ]]
  then
    #return again to menu
    MENU "I could not find that service. What would you like today?"
  else
    #ask for phione to identify customer
    echo -e "\nWhat's your phone number?"
    read CUSTOMER_PHONE

    #search for customer in customers table
    CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE phone='$CUSTOMER_PHONE'")

    #if customer not found
    if [[ -z $CUSTOMER_NAME ]]
    then
      #ask for name and add customer to customers table
      echo -e "\nI don't have a record for that phone number, what's your name?"
      read CUSTOMER_NAME
      INSERT_RESULT=$($PSQL "INSERT INTO customers(phone,name) VALUES('$CUSTOMER_PHONE','$CUSTOMER_NAME')")
    fi



    #select time for appointment
    echo -e "\nWhat time would you like your $SERVICE_NAME, $CUSTOMER_NAME?"
    read SERVICE_TIME

    CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone='$CUSTOMER_PHONE'")
    INSERT_RESULT=$($PSQL "INSERT INTO appointments(customer_id,service_id,time) VALUES('$CUSTOMER_ID','$SERVICE_ID_SELECTED','$SERVICE_TIME')")
    
    echo -e "I have put you down for a $SERVICE_NAME at $SERVICE_TIME, $CUSTOMER_NAME."

  fi

}

MENU