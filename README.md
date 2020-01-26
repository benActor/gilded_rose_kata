This project is made to fullfill the gilded Rose kata requirements.

it has been developed using python3, and there is no specific requirement to run the project,

just make sure python3 interpreter is installed on the system and you are ready to go.

it uses built in library for testing and system variables manipulations such as datetime so
don't worry about dependancies python handles all.


the project propose many classes to handle all the use cases of the requirement.

and offers for every type of item  a service to update the quality.


althouh must of the use cases have been implemented and tested we recommend each item to be updated 
with the appropriate service offered. eg. for Backstage passes use BackstageService class
other service may not be able to update accordingly different services.

item with no specific behaviour can be updated with the standarItemService class and 

if up comming items with specific behaviour just add it to the special_items_list and implement
a class to handle its cases you can rely on ItemService Class that propose some generic treatments
for all items

in case  of problem check the tests.   test saves the day.
 

