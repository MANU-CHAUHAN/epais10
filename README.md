# epais10

#### Topics:
>Tuples as a Data Structure

>Named Tuple

>Named Tuple - Modifying & Extending

>Named Tuple - DocString & Default Values

Tuples are immutable data structures which come handy when the data is not required to be modified. Examples include fetching data from database, the records will have same column names as the DB's schema. 

Named tuples provide user with the flexibility and ease of use in case there are many fields to keep track of in a tuple or record and referencing with position or associating meaning with individual position is not the Pythonic way and often leads to errors in code. Named tuples also give the feature of storing, modifying and having default values for fields.

Although Classes could be used to overcome the default tuple behaviour and adding flexibility, however, classes come with lot of overhead.

Named tuples provide a way of overcoming the broken use-case scenarios in case of unpacking as well. They `subclass` `tuple` and have added feature of having property names to positional elements. Named tuple's data can be accessed by *1)Index 2)slice 3)itearting

>The `rename` argument helps to rectify any naming errors for named tuples and converts to `_position` where position starts from 0.

> The `_fileds` attribute helps to retrieve all fields from a named tuple.
